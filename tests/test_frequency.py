import pytest
from textutils.frequency import word_frequency, most_common_words


class TestWordFrequency:
    def test_empty_string(self):
        assert word_frequency("") == {}

    def test_whitespace_only(self):
        assert word_frequency("   ") == {}

    def test_single_word(self):
        assert word_frequency("hello") == {"hello": 1}

    def test_repeated_words(self):
        result = word_frequency("the cat sat on the mat the")
        assert result["the"] == 3
        assert result["cat"] == 1
        assert result["mat"] == 1

    def test_case_insensitive(self):
        result = word_frequency("Hello hello HELLO")
        assert result == {"hello": 3}

    def test_strips_trailing_punctuation(self):
        result = word_frequency("hello, world!")
        assert "hello" in result
        assert "world" in result
        assert "hello," not in result
        assert "world!" not in result

    def test_all_words_present(self):
        result = word_frequency("a b c")
        assert set(result.keys()) == {"a", "b", "c"}

    def test_returns_dict(self):
        assert isinstance(word_frequency("test"), dict)


class TestMostCommonWords:
    def test_empty_string(self):
        assert most_common_words("") == []

    def test_returns_top_n(self):
        text = "the the the cat cat dog"
        result = most_common_words(text, n=2)
        assert len(result) == 2
        assert result[0] == ("the", 3)
        assert result[1] == ("cat", 2)

    def test_default_n_is_five(self):
        text = "a b c d e f g"
        result = most_common_words(text)
        assert len(result) == 5

    def test_n_larger_than_vocabulary(self):
        result = most_common_words("hello world", n=10)
        assert len(result) == 2

    def test_returns_list_of_tuples(self):
        result = most_common_words("hello hello world")
        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    def test_sorted_by_frequency_descending(self):
        text = "a a a b b c"
        result = most_common_words(text, n=3)
        counts = [count for _, count in result]
        assert counts == sorted(counts, reverse=True)
