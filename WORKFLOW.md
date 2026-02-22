# 🔥 The Crucible Protocol

**Adversarial refinement for ideas.** Transform rough concepts into battle-tested diamonds — or kill them fast.

---

## The Problem

You have an idea. You think it's good. But you're emotionally attached, so you don't see the flaws.

**Solution:** Force the idea through structured adversarial pressure. What survives is steel.

---

## Two Modes

### ⚡ Quick Mode (10 seconds)

Single devil's advocate. Catches obvious flaws fast.

```
You: "Quick crucible: AI-generated blog posts for my medical site"

Agent: 
Main risk: Medical misinformation liability — AI health content 
without physician review violates guidelines and creates malpractice exposure.
Secondary: Google EEAT penalizes AI content in health niches.

Verdict: PROCEED WITH GATES (physician review + disclosure required)
```

**Use for:** Daily decisions, quick sanity checks, "is this stupid?"

---

### 🔥 Deep Mode (60-90 seconds)

Full 5-agent protocol. For decisions that matter.

```
┌─────────────────────────────────────────────────────────┐
│  ROUND 1: STEELMAN                                       │
│  └── Makes the STRONGEST case FOR your idea              │
│      (so attacks target the best version, not a strawman)│
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  ROUND 2: ADVERSARIAL ASSAULT (parallel)                 │
│  ├── 🔍 Skeptic: Logic flaws, edge cases, assumptions   │
│  ├── ⚙️ Pragmatist: Reality check, resources, timeline  │
│  └── 😈 Contrarian: Argues the opposite position        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  ROUND 3: FRIENDLY FIRE                                  │
│  └── Agents critique EACH OTHER's critiques              │
│      (removes weak attacks, strengthens valid ones)      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  ROUND 4: SYNTHESIS & VERDICT                            │
│  └── Synthesizer weighs all input, renders judgment      │
│                                                          │
│  VERDICTS:                                               │
│  💎 DIAMOND — Ship it                                    │
│  🔧 REFINED — Valid with changes                         │
│  ⚠️ WEAK — Proceed with caution                          │
│  🪦 KILLED — Fatal flaw, pivot or abandon                │
└─────────────────────────────────────────────────────────┘
```

---

## The Kill Condition

Most "devil's advocate" exercises force a positive conclusion. Crucible doesn't.

**If all three attackers identify the SAME fatal flaw → the idea is KILLED.**

No forced diamonds from garbage. Some ideas should die fast so you can move on.

---

## Output Format

```
## 💎 VERDICT: REFINED

**The Diamond:** 
[Your idea, refined — incorporating valid critiques]

**🔥 Burned:** 
- Assumption that didn't survive
- Feature that was impractical

**💪 Hardened:**
- Element that got stronger under pressure
- Insight from Contrarian that improved it

**🚧 Gates:**
- Condition that must be true before shipping
- Guardrail to add
```

---

## When to Use

✅ **Use Crucible for:**
- New product/feature ideas
- Business strategy decisions  
- Content angles (blogs, tweets, videos)
- Technical architecture choices
- Anything you're emotionally attached to (most important)

❌ **Skip Crucible for:**
- Simple factual questions
- Tasks that need execution, not validation
- Ideas already validated by market/data
- Time-critical decisions (ship and learn faster)

---

## The Meta-Insight

This protocol was created by running Crucible on itself.

The original v1 had 3 attackers → synthesizer. Meta-crucible revealed:
- Missing Steelman (attacks targeted strawman)
- No Quick mode (overkill for daily decisions)
- No Kill condition (forcing diamonds from garbage)
- No Friendly Fire (weak critiques survived)

v2 fixed all of these. **The best way to improve a framework is to use it on itself.**

---

## Try It

```bash
# Requires: Python 3.8+, ANTHROPIC_API_KEY env var

# Quick mode
python crucible.py --quick "Your idea here"

# Deep mode  
python crucible.py "Your idea here"
```

**Repo:** [github.com/abgohel/crucible-protocol](https://github.com/abgohel/crucible-protocol)

---

*Based on @teej_m's insight: asking AI to critique its own solutions consistently produces better outputs. Crucible operationalizes this into a repeatable protocol.*
