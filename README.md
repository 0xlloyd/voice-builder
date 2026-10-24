# voice-builder

A Claude skill that builds you a personal voice skill, so your AI writes and talks like you rather than like a chatbot.

It works even if you rarely write. Most of the material comes from a short, conversational interview (about 30 minutes, mostly talking), plus any messages or voice notes you already have.

## What it does

1. **Gather:** you talk through three or four short pieces (a story, an opinion, an explanation), one at a time.
2. **Probe:** quick tests catch what free talk misses. You pick between pairs of phrasings, word a few everyday moments, mark which common AI phrases make you cringe, and confirm how your writing differs from your speech.
3. **Analyse:** your signature phrases, swaps, connectors, hedges and rhythm are pulled out. Each comes with a verbatim quote and a dose (everyday, occasional or rare), so the result doesn't turn into a caricature. You strike anything that isn't you.
4. **Test:** a blind test mixes generated pieces with your real excerpts. Whatever gives a fake away becomes a new rule.
5. **Build:** you get your own skill (`SKILL.md` + lexicon + examples). It triggers whenever you ask for something written on your behalf, and it offers to learn from every edit you make.

## Install

Add `SKILL.md` as a skill in Claude (or drop the folder into your skills directory), then say something like "build my voice" or "make my AI sound like me".

## Notes

- Your words may become examples in your finished skill. Names, numbers and private details are removed first.
- The run ends by reviewing itself with a `session-self-learning` skill if you have one installed. Otherwise it suggests improvements directly.
