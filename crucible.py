#!/usr/bin/env python3
"""
🔥 The Crucible Protocol v2
Adversarial refinement with Quick/Deep modes and kill conditions

Usage:
    python crucible.py "Your idea here"              # Deep mode
    python crucible.py --quick "Your idea here"     # Quick mode
    python crucible.py --json "Your idea here"      # JSON output
"""

import sys
import json
import subprocess
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# === AGENTS ===

STEELMAN = {
    "name": "steelman",
    "emoji": "💪",
    "role": "Defender",
    "prompt": """You are the Steelman. Your job is to present the STRONGEST possible case FOR this idea.

Assume the idea works. What's the best-case scenario? Why is this actually brilliant?
Don't be sycophantic — be genuinely persuasive. Make the case a smart advocate would make.

Idea:
{idea}

Present the steelmanned version in 3-4 sentences. Be compelling."""
}

SKEPTIC = {
    "name": "skeptic",
    "emoji": "🔍",
    "role": "Logic Hunter",
    "prompt": """You are the Skeptic analyzing an idea that has been steelmanned.

STEELMANNED IDEA:
{steelman}

Your job: Find every logical flaw, edge case, hidden assumption, and contradiction.
Attack the BEST version of this idea, not a strawman. Be surgical.

Give your critique in 100-150 words."""
}

PRAGMATIST = {
    "name": "pragmatist", 
    "emoji": "⚙️",
    "role": "Reality Check",
    "prompt": """You are the Pragmatist stress-testing an idea that has been steelmanned.

STEELMANNED IDEA:
{steelman}

Your job: Check against reality.
- Who builds this? With what resources? How long?
- What do people ACTUALLY do vs what the idea assumes?
- What's the 80/20? What breaks first?

Give your reality check in 100-150 words. Be brutally practical."""
}

CONTRARIAN = {
    "name": "contrarian",
    "emoji": "😈", 
    "role": "Opposition",
    "prompt": """You are the Contrarian arguing against an idea that has been steelmanned.

STEELMANNED IDEA:
{steelman}

Your job: Argue the OPPOSITE position as strongly as possible.
- Why might a completely different approach be better?
- What would a smart person who disagrees build instead?

Make the strongest case AGAINST in 100-150 words."""
}

QUICK_DEVIL = {
    "name": "devil",
    "emoji": "⚡",
    "role": "Quick Devil's Advocate",
    "prompt": """You are a Devil's Advocate doing a QUICK critique of an idea.

Idea:
{idea}

In 50-75 words, identify:
1. The MAIN risk or flaw
2. One secondary concern

Then give a verdict: PROCEED | PROCEED WITH GATES | PAUSE & RETHINK | KILL

Format:
Main risk: [one sentence]
Secondary: [one sentence]
Verdict: [VERDICT] — [3-5 word reason]"""
}

SYNTHESIZER_PROMPT = """You are the Synthesizer judging an idea after adversarial review.

ORIGINAL IDEA:
{idea}

STEELMAN (best case for the idea):
{steelman}

SKEPTIC'S CRITIQUE:
{skeptic}

PRAGMATIST'S REALITY CHECK:
{pragmatist}

CONTRARIAN'S COUNTER-ARGUMENT:
{contrarian}

FRIENDLY FIRE (agents critiquing each other):
{friendly_fire}

Your job:
1. Check if ALL THREE attackers identified the SAME fatal flaw → if yes, verdict is KILLED
2. Otherwise, extract what survived and render verdict

VERDICTS:
- 💎 DIAMOND — Idea survived and improved, ship it
- 🔧 REFINED — Core valid but needs specific changes
- ⚠️ WEAK — Risky but might work with caution
- 🪦 KILLED — Fatal flaw (unanimous), pivot or abandon

Format your response EXACTLY like this:

## 💎 VERDICT: [DIAMOND/REFINED/WEAK/KILLED]

[If DIAMOND/REFINED/WEAK:]
**The Diamond:** [Refined idea in 2-3 sentences]

**🔥 Burned:** 
- [What didn't survive]

**💪 Hardened:**
- [What got stronger]

**🚧 Gates:**
- [Conditions/guardrails needed before shipping]

[If KILLED:]
**Fatal Flaw:** [What killed it — the unanimous critique]

**Pivot Options:**
- [Alternative approach 1]
- [Alternative approach 2]"""

FRIENDLY_FIRE_PROMPT = """Three critics have attacked an idea. Now they critique EACH OTHER.

SKEPTIC said: {skeptic}
PRAGMATIST said: {pragmatist}  
CONTRARIAN said: {contrarian}

In 2-3 sentences each:
1. What's WRONG with the Skeptic's critique?
2. What's WRONG with the Pragmatist's critique?
3. What's WRONG with the Contrarian's critique?

Be brief. Find the weakness in each critique."""


def call_llm(prompt: str, max_tokens: int = 500) -> str:
    """Call Claude Sonnet via Anthropic API."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if not api_key:
        # Read from OpenClaw config
        config_file = Path.home() / ".openclaw" / "openclaw.json"
        if config_file.exists():
            try:
                config = json.loads(config_file.read_text())
                api_key = config.get("env", {}).get("vars", {}).get("ANTHROPIC_API_KEY")
            except:
                pass
    
    if not api_key:
        return "[Error: No API key found]"
    
    try:
        result = subprocess.run(
            ["curl", "-s", "https://api.anthropic.com/v1/messages",
             "-H", "Content-Type: application/json",
             "-H", f"x-api-key: {api_key}",
             "-H", "anthropic-version: 2023-06-01",
             "-d", json.dumps({
                 "model": "claude-sonnet-4-20250514",
                 "max_tokens": max_tokens,
                 "messages": [{"role": "user", "content": prompt}]
             })],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            response = json.loads(result.stdout)
            if "content" in response:
                return response["content"][0]["text"]
            elif "error" in response:
                return f"[API Error: {response['error'].get('message', 'Unknown')}]"
        return f"[Error: {result.stderr}]"
    except Exception as e:
        return f"[Error: {e}]"


def run_quick_crucible(idea: str) -> dict:
    """Quick mode: single devil's advocate."""
    print("⚡ QUICK CRUCIBLE\n", file=sys.stderr)
    
    prompt = QUICK_DEVIL["prompt"].format(idea=idea)
    result = call_llm(prompt, max_tokens=200)
    
    return {
        "mode": "quick",
        "idea": idea,
        "critique": result,
        "timestamp": datetime.now().isoformat()
    }


def run_deep_crucible(idea: str) -> dict:
    """Deep mode: full 5-agent protocol."""
    results = {
        "mode": "deep",
        "idea": idea,
        "timestamp": datetime.now().isoformat(),
        "rounds": {}
    }
    
    print("🔥 CRUCIBLE v2 — DEEP MODE\n", file=sys.stderr)
    
    # Round 1: Steelman
    print("💪 Round 1: Steelman Defense...", file=sys.stderr)
    steelman_prompt = STEELMAN["prompt"].format(idea=idea)
    steelman = call_llm(steelman_prompt, max_tokens=200)
    results["rounds"]["steelman"] = steelman
    
    # Round 2: Adversarial Assault (parallel)
    print("⚔️  Round 2: Adversarial Assault...", file=sys.stderr)
    
    attackers = [SKEPTIC, PRAGMATIST, CONTRARIAN]
    attacks = {}
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {}
        for agent in attackers:
            prompt = agent["prompt"].format(steelman=steelman)
            futures[executor.submit(call_llm, prompt, 250)] = agent["name"]
        
        for future in as_completed(futures):
            name = futures[future]
            attacks[name] = future.result()
            print(f"   {name}: done", file=sys.stderr)
    
    results["rounds"]["attacks"] = attacks
    
    # Round 3: Friendly Fire
    print("🔄 Round 3: Friendly Fire...", file=sys.stderr)
    ff_prompt = FRIENDLY_FIRE_PROMPT.format(
        skeptic=attacks["skeptic"],
        pragmatist=attacks["pragmatist"],
        contrarian=attacks["contrarian"]
    )
    friendly_fire = call_llm(ff_prompt, max_tokens=300)
    results["rounds"]["friendly_fire"] = friendly_fire
    
    # Round 4: Synthesis
    print("💎 Round 4: Synthesis & Verdict...", file=sys.stderr)
    synth_prompt = SYNTHESIZER_PROMPT.format(
        idea=idea,
        steelman=steelman,
        skeptic=attacks["skeptic"],
        pragmatist=attacks["pragmatist"],
        contrarian=attacks["contrarian"],
        friendly_fire=friendly_fire
    )
    synthesis = call_llm(synth_prompt, max_tokens=600)
    results["synthesis"] = synthesis
    
    print("", file=sys.stderr)
    return results


def format_quick_output(results: dict) -> str:
    """Format quick mode output."""
    return f"""⚡ QUICK CRUCIBLE

{results['critique']}
"""


def format_deep_output(results: dict) -> str:
    """Format deep mode output."""
    rounds = results.get("rounds", {})
    attacks = rounds.get("attacks", {})
    
    lines = [
        "═" * 50,
        "🔥 CRUCIBLE v2 — DEEP MODE",
        "═" * 50,
        "",
        "## 💪 STEELMAN",
        rounds.get("steelman", "[No steelman]"),
        "",
        "## ⚔️ THE ATTACKS",
        "",
        "### 🔍 Skeptic",
        attacks.get("skeptic", "[No critique]"),
        "",
        "### ⚙️ Pragmatist",
        attacks.get("pragmatist", "[No critique]"),
        "",
        "### 😈 Contrarian",
        attacks.get("contrarian", "[No critique]"),
        "",
        "## 🔄 FRIENDLY FIRE",
        rounds.get("friendly_fire", "[No friendly fire]"),
        "",
        "─" * 50,
        "",
        results.get("synthesis", "[No synthesis]"),
        "",
        "═" * 50
    ]
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="🔥 Crucible Protocol v2")
    parser.add_argument("idea", nargs="*", help="Idea to crucible")
    parser.add_argument("--quick", "-q", action="store_true", help="Quick mode (single agent)")
    parser.add_argument("--json", "-j", action="store_true", help="JSON output")
    
    args = parser.parse_args()
    
    if not args.idea:
        print("Usage: crucible.py [--quick] 'Your idea here'")
        print("       crucible.py -q 'Quick check this idea'")
        return 1
    
    idea = " ".join(args.idea)
    
    if args.quick:
        results = run_quick_crucible(idea)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(format_quick_output(results))
    else:
        results = run_deep_crucible(idea)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(format_deep_output(results))
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
