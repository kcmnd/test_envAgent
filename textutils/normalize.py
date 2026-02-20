import re
import unicodedata


def normalize_whitespace(text: str) -> str:
    """Collapse all whitespace runs into a single space and strip the result."""
    return re.sub(r"\s+", " ", text).strip()


def remove_punctuation(text: str) -> str:
    """Remove all punctuation characters from text."""
    return re.sub(r"[^\w\s]", "", text)


def to_slug(text: str) -> str:
    """Convert text to a lowercase, hyphen-separated URL slug.

    Accented characters are transliterated to ASCII equivalents.
    Non-alphanumeric characters (other than hyphens) are dropped.
    """
    # Normalise unicode to decomposed form then encode to ASCII, dropping accents
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = ascii_text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")
