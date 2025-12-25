def word_count(text: str) -> dict:
    """
    Count number of words in a given text.
    """
    words = text.split()
    return {
        "word_count": len(words)
    }
