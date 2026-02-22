# 🔥 The Crucible Protocol v2

**Purpose:** Transform rough ideas into refined diamonds — or kill them mercifully.

**Triggers:** 
- "Crucible this: [idea]" → Deep mode (full protocol)
- "Quick crucible: [idea]" → Quick mode (single agent, 10s)
- "Pressure test [idea]" → Deep mode
- "Attack this idea: [idea]" → Quick mode

---

## Quick Mode (10 seconds)

Single Devil's Advocate agent. Fast, cheap, catches obvious flaws.

```
Input: "Quick crucible: AI-generated blog posts for Gujarat Epilepsy"

Output:
⚡ QUICK CRUCIBLE

Main risk: Medical misinformation liability. AI-generated health content 
without physician review violates NMC guidelines and creates malpractice 
exposure. Secondary: Google's EEAT penalizes AI content in YMYL niches.

Verdict: PROCEED WITH GATES (physician review + disclosure)
```

**Verdicts:** PROCEED | PROCEED WITH GATES | PAUSE & RETHINK | KILL

---

## Deep Mode (60-90 seconds)

Full adversarial protocol with 5 agents.

### The Five Fires

| Agent | Role | Attack Vector |
|-------|------|---------------|
| **Steelman** | Defender | Makes the STRONGEST case FOR the idea first |
| **Skeptic** | Logic hunter | Edge cases, contradictions, hidden assumptions |
| **Pragmatist** | Reality check | Feasibility, resources, "who actually does this?" |
| **Contrarian** | Opposition | Steel-mans the counter-argument |
| **Synthesizer** | Judge | Weighs all input, renders verdict |

### The Process

```
Round 1: Steelman Defense (10s)
└── Steelman presents the strongest version of the idea

Round 2: Adversarial Assault (parallel, 20s)
├── Skeptic attacks the steelmanned idea
├── Pragmatist attacks the steelmanned idea
└── Contrarian argues the opposite position

Round 3: Friendly Fire (parallel, 15s)
├── Skeptic critiques Pragmatist's concerns
├── Pragmatist critiques Contrarian's position
└── Contrarian critiques Skeptic's logic

Round 4: Synthesis & Verdict (15s)
├── Synthesizer reviews all rounds
├── Checks for unanimous fatal flaw (→ KILL)
├── Extracts what survived
└── Renders final verdict
```

---

## Kill Condition

If ALL THREE attackers (Skeptic, Pragmatist, Contrarian) identify the SAME fatal flaw:

```
🪦 KILLED

Fatal flaw (unanimous): [description]

The idea cannot survive this. Pivot or abandon.

Pivot options:
- [alternative 1]
- [alternative 2]
```

No forced diamond. Some ideas should die fast.

---

## Output Format (Deep Mode)

```
## 💪 STEELMAN
[Strongest case FOR the idea — 2-3 sentences]

## ⚔️ THE ATTACKS

### 🔍 Skeptic
[Logical flaws, edge cases — 100-150 words]

### ⚙️ Pragmatist  
[Reality check — 100-150 words]

### 😈 Contrarian
[Counter-argument — 100-150 words]

## 🔄 FRIENDLY FIRE
[Key inter-agent conflicts — 50 words]

## 💎 VERDICT: [DIAMOND | REFINED | WEAK | KILLED]

[If DIAMOND/REFINED:]
**The Diamond:** [Refined idea — 2-3 sentences]

**Burned:** [What didn't survive]
**Hardened:** [What got stronger]  
**Gates:** [Conditions/guardrails needed]

[If WEAK:]
**Proceed if:** [Specific conditions]
**Kill if:** [Red lines]

[If KILLED:]
**Fatal flaw:** [What killed it]
**Pivot options:** [Alternatives]
```

---

## Verdicts

| Verdict | Meaning | Action |
|---------|---------|--------|
| **💎 DIAMOND** | Idea survived and improved | Ship it |
| **🔧 REFINED** | Core valid, needs changes | Implement gates |
| **⚠️ WEAK** | Risky but might work | Proceed with caution |
| **🪦 KILLED** | Fatal flaw, unanimous | Pivot or abandon |

---

## Human Escalation

After any crucible, option to escalate:

```
Want human review? 
[Escalate to advisor] — sends summary to trusted human critic
```

LLM crucibles catch 80%. Humans catch the subtle 20%.

---

## Integration

Crucible is triggered by natural language in any Meow conversation:

- "crucible this" / "crucible:" → Deep mode
- "quick crucible" / "qc:" → Quick mode  
- "pressure test" / "stress test" → Deep mode
- "attack this" / "poke holes" → Quick mode

No separate script needed. Just talk.

---

## When to Use

✅ **Use Crucible for:**
- New product/feature ideas
- Business strategy decisions
- Content angles (blogs, tweets)
- Technical architecture choices
- Anything you're emotionally attached to

❌ **Skip Crucible for:**
- Simple factual questions
- Tasks that need execution, not validation
- Ideas already validated by market data
- Time-critical decisions (ship and learn)

---

## Token Costs

| Mode | Agents | ~Tokens | ~Time |
|------|--------|---------|-------|
| Quick | 1 | 500 | 10s |
| Deep | 5 | 2500 | 60-90s |

Quick mode for daily decisions. Deep mode for big bets.
