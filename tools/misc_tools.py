import random
from datetime import datetime


def random_quote() -> str:
    """
    Return a random motivational quote.
    """
    quotes = [
        "Small steps lead to big results.",
        "Consistency beats intensity.",
        "Learning never exhausts the mind.",
        "Build first, optimize later."
    ]
    return random.choice(quotes)


def current_time() -> str:
    """
    Return current local time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
