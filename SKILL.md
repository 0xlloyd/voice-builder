---
name: "voice-builder"
description: "Build a personal voice skill that makes an LLM write and talk like the user, drawing mainly on a short, conversational interview plus any writing they already have, so it works even for people who rarely write. Use it whenever the user wants their AI to sound like them, capture their voice or writing style, stop sounding like ChatGPT, or build a \"write like me\" skill, even if they never say the word \"skill\"."
---

# Voice Builder

## Purpose

The run ends with a ready-to-install voice skill folder (a SKILL.md, a lexicon and real examples) that the user's own LLM loads to write and talk like them.
Voice lives mostly in small habits people don't notice in themselves (favourite phrases and swaps, connecting words, hedges, rhythm, things they'd never say), so the run draws those habits out through talk and quick tests rather than asking the user to describe their style.
The bar is that someone who knows the user would believe they wrote the output; aim for that rather than perfection, because no prompt-based method fully closes the gap to the real person.

## Setup

Start by telling the user what to expect: about 30 minutes, mostly talking rather than writing, where voice dictation or typing the way they'd text a friend both work well.
Check whether the user already has a voice skill; if they do, read it and switch to update mode, gathering only new material and editing the existing files instead of starting over.
Let the user know that their words may become examples in the finished skill, and remove names, numbers and private details from those examples before they go in.
If a file this skill points to (a prompt list, template or script) is missing, carry on with your own best version of it rather than stopping, and mention the gap at the end of the run.

## Gather raw material

Gather speech first, because people watch their words when they know they're being studied and stop watching once they're caught up in telling a story.
Ask for three or four short spoken-style pieces, one at a time, on topics the user picks because they could talk about them all day, steering gently so the set covers a story, an opinion and an explanation; offer prompts from `references/interview-prompts.md` only if they get stuck, and let them talk without interrupting.
Invite any voice notes, dictation or call transcripts they already have, and treat these as the strongest evidence after the interview itself.
If they have any to hand, also ask for real messages they've sent (texts, emails, chats, social posts), which show their voice better than polished published writing because editing tends to strip voice out; if they don't, carry on without.
Aim for roughly 1,500 words of the user's own language across at least three situations, because less leaves the analysis guessing; if they can't get there, carry on and tell them the skill will start thinner and sharpen as it learns from their edits.

## Probe

Once the raw material is in, run a short round of quick tests to catch what free talk misses.
Offer pairs of phrasings that mean the same thing (such as "keep a record" and "keep the receipts") and ask which one they'd actually say, or what they'd say instead, because people pick far more accurately than they describe.
Ask how they'd word a few everyday moments the material didn't cover, choosing ones that fit their real role and life (such as chasing a reply, saying no to a request or saying thanks), asking them in a separate message from the phrasing pairs so they don't get skipped, and keep their answers word for word.
Show them the common AI words, phrases and habits in `references/ai-tells.md` (such as "let's dive in", "game-changer", "delve", "unlock", "robust", "in today's fast-paced world", "it's not just X, it's Y" and heavy use of em dashes) and ask which ones make them cringe, so the never-say list reflects their taste rather than a generic ban list.
Check whether anything shifts when they write rather than talk (swearing, emoji, length, formality) by stating your own read from what they've shared and asking them to confirm or correct it, since an open question here is easy to skip, so the single blended voice still respects the lines they won't cross in writing.

## Analyse

Read everything gathered and pull the voice apart layer by layer: signature phrases and swaps, connecting words and fillers, hedges and how sure they sound, sentence length and rhythm, how they open and close, punctuation and formatting habits, humour and attitude, and things they'd never say.
Back every item with at least one verbatim quote from the user and a rough note of how often it appears, because a rule without evidence drifts and a phrase used once isn't yet a habit.
When quoting speech, drop the ums and false starts but keep the user's words, rhythm and grammar as they are, since the aim is how they sound on a good day, not a raw transcript.
Turn each frequency into a dose, marking every signature phrase as everyday, occasional or rare, because overusing someone's catchphrases is the fastest way to turn their voice into a caricature.
If `scripts/voice_stats.py` can run, use it on the gathered text for average sentence length, contraction rate, top function words and punctuation habits, but let the quotes lead, since these counts on their own don't reliably tell people apart.
Play back the top ten or so findings as a short list with their quotes, and let the user strike or correct anything that doesn't feel like them before it goes any further.

## Test

Write three short pieces in the user's voice, each retelling the topic of one of their real excerpts from a plain summary of what they said rather than their own words, so the user has to judge by voice and not by recognising the story.
Mix them unlabelled and in random order with the three real excerpts they retell, and ask the user to pick out which are really theirs, because only the user can judge their own voice, while an LLM checking its own output just rewards the traits it already extracted.
For every generated piece they spot, ask what gave it away, and turn the answer into a rule edit, a new lexicon entry or a never-say item.
Run up to two rounds, stopping early once the user can't reliably tell the generated pieces from their own or says they'd send them as they are.

## Build

Ask the user what to call their skill, suggesting `my-voice`, and build its folder from the three templates: `templates/voice-skill.md` becomes its SKILL.md, alongside a lexicon from `templates/lexicon.md` and examples from `templates/examples.md`.
Fill the SKILL.md with the confirmed rules, each followed by its supporting quote, plus the dosage guide and the anti-AI rules, keeping it short enough that the model reads all of it every time.
Fill the lexicon with the swaps, signature phrases and their doses, connecting words and hedges, and the never-say list.
For the examples file, pick three to five real excerpts that cover different situations rather than the most colourful ones, since more than five adds little and colourful picks push the model toward caricature, then add two before-and-after rewrites from the test rounds.
Keep the template's learning loop, so whenever the user edits or corrects a draft, their voice skill offers to save the fix to its own files and keeps getting closer over time.
Write the new skill's description so it triggers whenever the user asks for anything written or said on their behalf (emails, messages, posts, scripts, replies), not only when they mention their voice.

## Deliver

Deliver the finished skill however the environment allows (a save card where one is offered, otherwise a zipped folder to download) with a one-line note on where to install it.
If the save card only stores a SKILL.md, fold the lexicon and examples into it as their own sections so nothing is lost, and offer the three-file folder as a zip alongside it.
Suggest they try it straight away on something real they need to send, since their first edits are what the learning loop feeds on.

## Close

End by running `session-self-learning` on `voice-builder` itself, not on the voice skill just built (which improves through its own learning loop), so it reviews how this run went and proposes evidence-backed edits for the user to approve; if `session-self-learning` isn't installed, suggest any improvements to `voice-builder` directly instead.
