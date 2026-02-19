import re


def word_count(text: str) -> int:
    """Return the number of words in text."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def char_count(text: str, include_spaces: bool = True) -> int:
    """Return the number of characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def sentence_count(text: str) -> int:
    """Return the approximate number of sentences in text."""
    if not text or not text.strip():
        return 0
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])
