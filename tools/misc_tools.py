import json
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

def server_info() -> str:
    """
    Return basic server information.
    """
    info = {
        "server_name": "FastMCP Demo Server",
        "version": "1.0",
        "description": "A basic MCP server with math and text tools.",
        "tools": ["add_numbers", "multiply_numbers", "subtract_numbers", "word_count", "random_quote", "current_time"],
        "author": "avishek"
    }
    return json.dumps(info, indent=2)
