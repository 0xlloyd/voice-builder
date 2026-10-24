#!/usr/bin/env python3
"""Rough voice stats for a user's own text: sentence rhythm, contractions,
function words and punctuation. Evidence to sit beside quotes, not a verdict.

Usage: python3 voice_stats.py file1.txt [file2.txt ...]   (or pipe text in)
"""
import re
import statistics
import sys
from collections import Counter

FUNCTION_WORDS = [
    "i", "we", "you", "they", "it", "the", "a", "and", "but", "so", "or",
    "because", "just", "really", "actually", "basically", "like", "well",
    "that", "this", "very", "quite", "maybe", "probably", "think", "mean",
]


def load_text(paths):
    if not paths:
        return sys.stdin.read()
    parts = []
    for path in paths:
        with open(path, encoding="utf-8", errors="replace") as f:
            parts.append(f.read())
    return "\n".join(parts)


def split_sentences(text):
    pieces = re.split(r"(?<=[.!?…])\s+|\n+", text)
    return [p.strip() for p in pieces if re.search(r"[A-Za-z]", p)]


def split_words(text):
    return re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", text)


def compute(text):
    sentences = split_sentences(text)
    words = split_words(text)
    n = len(words) or 1
    lengths = [len(split_words(s)) for s in sentences] or [0]
    lower = Counter(w.lower() for w in words)
    per_k = lambda count: round(count * 1000 / n, 1)
    return {
        "words": len(words),
        "sentences": len(sentences),
        "avg_sentence_words": round(statistics.mean(lengths), 1),
        "sentence_spread": round(statistics.pstdev(lengths), 1),
        "questions_pct": round(100 * sum(s.endswith("?") for s in sentences) / (len(sentences) or 1)),
        "contractions_per_100": round(100 * sum("'" in w or "’" in w for w in words) / n, 1),
        "function_words_per_1000": {w: per_k(lower[w]) for w in FUNCTION_WORDS if lower[w]},
        "punctuation_per_1000": {
            mark: per_k(text.count(mark))
            for mark in ["!", "?", ";", ":", "—", "–", "…", "(", '"']
            if text.count(mark)
        },
        "all_caps_words": sum(1 for w in words if len(w) > 1 and w.isupper() and w != "I"),
        "emoji": len(re.findall(r"[\U0001F300-\U0001FAFF☀-➿]", text)),
    }


def report(stats):
    print(f"Words: {stats['words']}   Sentences: {stats['sentences']}")
    if stats["words"] < 1000:
        print("Note: under 1,000 words, so treat these numbers as rough hints.")
    print(f"Average sentence: {stats['avg_sentence_words']} words "
          f"(spread {stats['sentence_spread']}; higher = more mixed short and long)")
    print(f"Questions: {stats['questions_pct']}% of sentences")
    print(f"Contractions: {stats['contractions_per_100']} per 100 words")
    top = sorted(stats["function_words_per_1000"].items(), key=lambda kv: -kv[1])[:12]
    print("Top function words per 1,000: " + ", ".join(f"{w} {r}" for w, r in top))
    marks = stats["punctuation_per_1000"]
    print("Punctuation per 1,000 words: " + (", ".join(f"{m} {r}" for m, r in marks.items()) or "none"))
    print(f"ALL-CAPS words: {stats['all_caps_words']}   Emoji: {stats['emoji']}")


if __name__ == "__main__":
    report(compute(load_text(sys.argv[1:])))
