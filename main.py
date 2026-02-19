from textutils import word_count, char_count, sentence_count


def main():
    sample = "Hello world. This is a test. How many words are here?"
    print(f"Words: {word_count(sample)}")
    print(f"Characters (with spaces): {char_count(sample)}")
    print(f"Characters (no spaces): {char_count(sample, include_spaces=False)}")
    print(f"Sentences: {sentence_count(sample)}")


if __name__ == "__main__":
    main()
