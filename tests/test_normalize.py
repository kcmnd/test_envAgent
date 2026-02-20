import pytest
from textutils.normalize import normalize_whitespace, remove_punctuation, to_slug


class TestNormalizeWhitespace:
    def test_empty_string(self):
        assert normalize_whitespace("") == ""

    def test_no_change_needed(self):
        assert normalize_whitespace("hello world") == "hello world"

    def test_collapses_multiple_spaces(self):
        assert normalize_whitespace("hello   world") == "hello world"

    def test_collapses_tabs(self):
        assert normalize_whitespace("hello\t\tworld") == "hello world"

    def test_collapses_newlines(self):
        assert normalize_whitespace("hello\n\nworld") == "hello world"

    def test_strips_leading_and_trailing(self):
        assert normalize_whitespace("  hello  ") == "hello"

    def test_mixed_whitespace(self):
        assert normalize_whitespace("  foo \t bar\n  baz  ") == "foo bar baz"


class TestRemovePunctuation:
    def test_empty_string(self):
        assert remove_punctuation("") == ""

    def test_no_punctuation(self):
        assert remove_punctuation("hello world") == "hello world"

    def test_removes_period(self):
        assert remove_punctuation("Hello world.") == "Hello world"

    def test_removes_multiple_punctuation(self):
        assert remove_punctuation("Hello, world! How are you?") == "Hello world How are you"

    def test_keeps_alphanumeric(self):
        result = remove_punctuation("abc123")
        assert result == "abc123"

    def test_removes_quotes(self):
        assert remove_punctuation('"quoted"') == "quoted"


class TestToSlug:
    def test_empty_string(self):
        assert to_slug("") == ""

    def test_simple_lowercase(self):
        assert to_slug("hello world") == "hello-world"

    def test_uppercase_lowercased(self):
        assert to_slug("Hello World") == "hello-world"

    def test_multiple_spaces_become_single_hyphen(self):
        assert to_slug("hello   world") == "hello-world"

    def test_removes_special_characters(self):
        assert to_slug("hello, world!") == "hello-world"

    def test_accented_characters_transliterated(self):
        assert to_slug("café résumé") == "cafe-resume"

    def test_no_leading_or_trailing_hyphens(self):
        slug = to_slug("  hello  ")
        assert not slug.startswith("-")
        assert not slug.endswith("-")

    def test_numbers_preserved(self):
        assert to_slug("python 3") == "python-3"
