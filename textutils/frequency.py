import re
from collections import Counter


def word_frequency(text: str) -> dict[str, int]:
    """Return a mapping of each word to its frequency in text.

    Words are lowercased and stripped of punctuation before counting.
    """
    if not text or not text.strip():
        return {}
    words = text.lower().split()
    words = [re.sub(r"[^\w]", "", w) for w in words]
    words = [w for w in words if w]
    return dict(Counter(words))


def most_common_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """Return the n most common words and their counts, sorted by frequency."""
    freq = word_frequency(text)
    return Counter(freq).most_common(n)
