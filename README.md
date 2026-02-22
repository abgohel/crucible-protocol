# 🔥 The Crucible Protocol v2

[![Security: VirusTotal](https://img.shields.io/badge/VirusTotal-0%2F94%20Clean-brightgreen)](https://www.virustotal.com/gui/url/27532596893da212f488f7f1b579c4b0348191dfdefbb05560966bb6678eac60)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Adversarial refinement for ideas. Transform rough concepts into battle-tested diamonds — or kill them mercifully.

## Quick Start

```bash
# Quick mode (10s) - single devil's advocate
python crucible.py --quick "Your idea here"

# Deep mode (60-90s) - full 5-agent protocol  
python crucible.py "Your idea here"
```

## Two Modes

| Mode | Time | Agents | Use For |
|------|------|--------|---------|
| **Quick** | 10s | 1 (Devil's Advocate) | Daily decisions |
| **Deep** | 60-90s | 5 (Steelman → Skeptic/Pragmatist/Contrarian → Synthesizer) | Big bets |

## Verdicts

- 💎 **DIAMOND** — Idea survived and improved. Ship it.
- 🔧 **REFINED** — Core valid, needs specific changes.
- ⚠️ **WEAK** — Risky but might work with caution.
- 🪦 **KILLED** — Fatal flaw (unanimous). Pivot or abandon.

## Kill Condition

If all three attackers (Skeptic, Pragmatist, Contrarian) identify the SAME fatal flaw, the idea is KILLED. No forced diamonds from garbage.

## Requirements

- Python 3.8+
- Anthropic API key (set `ANTHROPIC_API_KEY` env var)

## Full Protocol

See [crucible.md](crucible.md) for the complete protocol specification.

## Origin

Created via meta-crucible: the protocol was used to refine itself. Based on @teej_m's insight that asking AI to critique its own solutions consistently produces better outputs.

## License

MIT
