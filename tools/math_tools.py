def add_numbers(x: int,y: int) -> int:
    """Add two numbers"""
    return x + y


def multiply_numbers(x: int,y: int) -> int:
    """Multiply two numbers"""
    return x * y


def subtract_numbers(x: int,y: int) -> int:
    """Subtract two numbers"""
    if x > 0:
        return x + y
    else:
        return y - x 
