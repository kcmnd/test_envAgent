import re


def average_word_length(text: str) -> float:
    """Return the average number of characters per word.

    Punctuation attached to words is stripped before measuring.
    Returns 0.0 for empty or whitespace-only input.
    """
    if not text or not text.strip():
        return 0.0
    words = text.split()
    words = [re.sub(r"[^\w]", "", w) for w in words]
    words = [w for w in words if w]
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def average_sentence_length(text: str) -> float:
    """Return the average number of words per sentence.

    Sentences are split on '.', '!' or '?'. Returns 0.0 for empty input.
    """
    if not text or not text.strip():
        return 0.0
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    if not sentences:
        return 0.0
    total_words = sum(len(s.split()) for s in sentences)
    return total_words / len(sentences)


def lexical_diversity(text: str) -> float:
    """Return the ratio of unique words to total words (type-token ratio).

    Words are lowercased before comparison. Returns 0.0 for empty input.
    A value of 1.0 means every word is unique; lower values indicate repetition.
    """
    if not text or not text.strip():
        return 0.0
    words = [re.sub(r"[^\w]", "", w).lower() for w in text.split()]
    words = [w for w in words if w]
    if not words:
        return 0.0
    return len(set(words)) / len(words)
