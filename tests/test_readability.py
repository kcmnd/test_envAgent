import pytest
from textutils.readability import average_word_length, average_sentence_length, lexical_diversity


class TestAverageWordLength:
    def test_empty_string(self):
        assert average_word_length("") == 0.0

    def test_whitespace_only(self):
        assert average_word_length("   ") == 0.0

    def test_single_word(self):
        assert average_word_length("hello") == 5.0

    def test_equal_length_words(self):
        assert average_word_length("cat dog fox") == pytest.approx(3.0)

    def test_mixed_length_words(self):
        # "hi" (2) + "there" (5) = 7 / 2 = 3.5
        assert average_word_length("hi there") == pytest.approx(3.5)

    def test_punctuation_stripped(self):
        # "hello," -> "hello" (5), "world!" -> "world" (5)
        assert average_word_length("hello, world!") == pytest.approx(5.0)

    def test_returns_float(self):
        assert isinstance(average_word_length("test"), float)


class TestAverageSentenceLength:
    def test_empty_string(self):
        assert average_sentence_length("") == 0.0

    def test_whitespace_only(self):
        assert average_sentence_length("   ") == 0.0

    def test_single_sentence(self):
        assert average_sentence_length("Hello world.") == pytest.approx(2.0)

    def test_two_equal_sentences(self):
        # "Hello world" (2 words), "Foo bar" (2 words) -> avg 2.0
        assert average_sentence_length("Hello world. Foo bar.") == pytest.approx(2.0)

    def test_unequal_sentences(self):
        # "Hello" (1), "How are you" (3) -> avg 2.0
        assert average_sentence_length("Hello! How are you?") == pytest.approx(2.0)

    def test_no_terminal_punctuation(self):
        assert average_sentence_length("Hello world") == pytest.approx(2.0)

    def test_returns_float(self):
        assert isinstance(average_sentence_length("test"), float)


class TestLexicalDiversity:
    def test_empty_string(self):
        assert lexical_diversity("") == 0.0

    def test_whitespace_only(self):
        assert lexical_diversity("   ") == 0.0

    def test_all_unique_words(self):
        assert lexical_diversity("the cat sat") == pytest.approx(1.0)

    def test_all_same_word(self):
        assert lexical_diversity("the the the") == pytest.approx(1 / 3)

    def test_case_insensitive(self):
        # "Hello", "hello", "HELLO" are all the same word
        assert lexical_diversity("Hello hello HELLO") == pytest.approx(1 / 3)

    def test_partial_repetition(self):
        # "a" x2, "b" x1 -> 2 unique / 3 total
        assert lexical_diversity("a b a") == pytest.approx(2 / 3)

    def test_range_is_zero_to_one(self):
        score = lexical_diversity("the quick brown fox jumps over the lazy dog")
        assert 0.0 <= score <= 1.0

    def test_returns_float(self):
        assert isinstance(lexical_diversity("test"), float)
