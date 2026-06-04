from collections import Counter

INPUT_FILE = "sample-text.txt"
OUTPUT_FILE = "analysis-report.txt"


def clean_text(text):
    """Return normalized text (trimmed, lowercase, condensed spaces)."""
    # TODO: normalize whitespace and lowercase the text
    return text


def text_stats(text):
    """Return a dictionary with character and word counts."""
    # TODO: compute and return {'characters': ..., 'words': ...}
    return {
        "characters": 0,
        "words": 0,
    }


def replace_phrase(text, target, replacement):
    """Return text with all target phrases replaced."""
    # TODO: perform phrase replacement
    return text


def most_common_word(text):
    """Return the most common word and its count."""
    # TODO: split text into words, count frequencies, and return (word, count)
    return "", 0


def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as infile:
            raw_text = infile.read()
    except FileNotFoundError:
        print(f"Could not find input file: {INPUT_FILE}")
        return

    cleaned = clean_text(raw_text)
    stats = text_stats(cleaned)
    common_word, common_count = most_common_word(cleaned)

    print("Text Summary")
    print("------------")
    print(f"Characters: {stats['characters']}")
    print(f"Words: {stats['words']}")
    print(f"Most common word: {common_word} ({common_count})")

    report = (
        "Text Analysis Report\n"
        "====================\n"
        f"Characters: {stats['characters']}\n"
        f"Words: {stats['words']}\n"
        f"Most common word: {common_word} ({common_count})\n\n"
        "Cleaned Text:\n"
        f"{cleaned}\n"
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        outfile.write(report)

    print(f"Report saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
