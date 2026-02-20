from .stats import word_count, char_count, sentence_count
from .frequency import word_frequency, most_common_words
from .normalize import normalize_whitespace, remove_punctuation, to_slug
from .readability import average_word_length, average_sentence_length, lexical_diversity

__all__ = [
    "word_count", "char_count", "sentence_count",
    "word_frequency", "most_common_words",
    "normalize_whitespace", "remove_punctuation", "to_slug",
    "average_word_length", "average_sentence_length", "lexical_diversity",
]
