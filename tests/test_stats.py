import pytest
from textutils.stats import word_count, char_count, sentence_count


class TestWordCount:
    def test_empty_string(self):
        assert word_count("") == 0

    def test_whitespace_only(self):
        assert word_count("   ") == 0

    def test_single_word(self):
        assert word_count("hello") == 1

    def test_multiple_words(self):
        assert word_count("hello world foo") == 3

    def test_extra_spaces_between_words(self):
        assert word_count("hello   world") == 2

    def test_newlines_count_as_separators(self):
        assert word_count("hello\nworld") == 2


class TestCharCount:
    def test_empty_string(self):
        assert char_count("") == 0

    def test_with_spaces_included(self):
        assert char_count("hello world") == 11

    def test_without_spaces(self):
        assert char_count("hello world", include_spaces=False) == 10

    def test_only_spaces_excluded(self):
        assert char_count("   ", include_spaces=False) == 0

    def test_single_char(self):
        assert char_count("a") == 1


class TestSentenceCount:
    def test_empty_string(self):
        assert sentence_count("") == 0

    def test_whitespace_only(self):
        assert sentence_count("   ") == 0

    def test_single_sentence_with_period(self):
        assert sentence_count("Hello world.") == 1

    def test_single_sentence_no_punctuation(self):
        assert sentence_count("Hello world") == 1

    def test_multiple_sentences(self):
        assert sentence_count("Hello world. How are you? I am fine!") == 3

    def test_exclamation_and_question(self):
        assert sentence_count("Really? Yes!") == 2
