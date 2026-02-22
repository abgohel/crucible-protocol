

# 🔥 The Crucible Protocol

**Adversarial refinement for ideas.** Transform rough concepts into battle-tested diamonds—or kill them fast.

---

## The Problem

You have an idea. You think it's brilliant. But because you are emotionally attached to it, you are blind to its flaws.

**The Solution:** Force the idea through structured adversarial pressure. Whatever survives is steel.

---

## Two Modes of Operation

### ⚡ Quick Mode (10 Seconds)

Deploys a single devil's advocate to catch obvious flaws immediately.

> **You:** "Quick crucible: AI-generated blog posts for my medical site."
> **Agent:** > * **Main Risk:** Medical misinformation liability. Publishing AI health content without physician review violates guidelines and creates severe malpractice exposure.
> * **Secondary Risk:** Google's E-E-A-T guidelines heavily penalize AI-generated content in health and YMYL (Your Money or Your Life) niches.
> 
> 
> **Verdict:** PROCEED WITH GATES (Physician review + explicit disclosure required).

**Best for:** Daily decisions, quick sanity checks, and answering, "Is this a terrible idea?"

---

### 🔥 Deep Mode (60–90 Seconds)

Executes the full 5-agent protocol. Built for decisions that actually matter.

```text
┌───────────────────────────────────────────────────────────────┐
│  ROUND 1: STEELMAN                                            │
│  └── Makes the STRONGEST case FOR your idea                   │
│      (Ensures attackers target the best version,              │
│      not a strawman)                                          │
└───────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│  ROUND 2: ADVERSARIAL ASSAULT (Parallel)                      │
│  ├── Skeptic: Logic flaws, edge cases, assumptions            │
│  ├── Pragmatist: Reality check, resources, timeline           │
│  └── Contrarian: Argues the exact opposite position           │
└───────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│  ROUND 3: FRIENDLY FIRE                                       │
│  └── Agents critique EACH OTHER'S critiques                   │
│      (Removes weak attacks, strengthens valid ones)           │
└───────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌───────────────────────────────────────────────────────────────┐
│  ROUND 4: SYNTHESIS & VERDICT                                 │
│  └── Synthesizer weighs all inputs and renders judgment       │
│                                                               │
│  VERDICTS:                                                    │
│  [DIAMOND] - Ship it.                                         │
│  [REFINED] - Valid, but requires changes.                     │
│  [WEAK]    - Proceed with extreme caution.                    │
│  [KILLED]  - Fatal flaw discovered; pivot or abandon.         │
└───────────────────────────────────────────────────────────────┘

```

---

## 💀 The Kill Condition

Most "devil's advocate" exercises force a positive conclusion. The Crucible does not.

**If all three attackers independently identify the SAME fatal flaw → the idea is KILLED.**

We don't force diamonds out of garbage. Some ideas need to die quickly so you can move on to better ones.

---

## Output Format

When a Deep Mode cycle completes, you receive a standardized breakdown:

> ## 💎 VERDICT: REFINED
> 
> 
> **The Diamond:** > [Your refined idea—now incorporating valid critiques]
> 
> **🔥 Burned:** > * [Assumption that didn't survive the pressure]
> * [Feature that was deemed impractical]
> 
> 
> **💪 Hardened:**
> * [Element that became stronger under scrutiny]
> * [Insight from the Contrarian that improved the concept]
> 
> 
> **🚧 Gates:**
> * [Condition that must be met before shipping]
> * [Specific guardrail to implement]
> 
> 

---

## When to Use It

✅ **Run the Crucible for:**

* New product or feature ideas
* Major business strategy decisions
* Content angles (blogs, threads, videos)
* Technical architecture choices
* **Anything you are emotionally attached to** (Most Important)

❌ **Skip the Crucible for:**

* Simple, factual questions
* Tasks that require execution, not validation
* Ideas that are already validated by hard data or the market
* Time-critical decisions where shipping and learning is faster

---

## The Meta-Insight

This protocol was created by running the Crucible on itself.

The original `v1` featured 3 attackers feeding into a synthesizer. A meta-crucible run revealed severe flaws:

* **Missing Steelman:** Attackers were tearing down strawman arguments.
* **No Quick Mode:** The full process was overkill for daily decisions.
* **No Kill Condition:** The system kept trying to force bad ideas into "diamonds."
* **No Friendly Fire:** Weak critiques were surviving to the final synthesis.

Version 2 fixed all of these issues. **The best way to improve a framework is to run it through itself.**

---

## Try It

```bash
# Prerequisites: Python 3.8+, ANTHROPIC_API_KEY environment variable

# Run Quick Mode (10s)
python crucible.py --quick "Your idea here"

# Run Deep Mode (60-90s)
python crucible.py "Your idea here"

```

**Repository:** [github.com/abgohel/crucible-protocol](https://github.com/abgohel/crucible-protocol)

*(Based on @teej_m's insight: asking AI to critique its own solutions consistently produces better outputs. The Crucible operationalizes this into a repeatable, automated protocol.)*
