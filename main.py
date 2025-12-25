import random
from fastmcp import FastMCP

mcp = FastMCP(name="first mcp demo server")

@mcp.tool()
def add_numbers(x: int,y: int) -> int:
    """Add two numbers"""
    return x + y

@mcp.tool()
def multiply_numbers(x: int,y: int) -> int:
    """Multiply two numbers"""
    return x * y

@mcp.tool()
def subtract_numbers(x: int,y: int) -> int:
    """Subtract two numbers"""
    if x > 0:
        return x + y
    else:
        return y - x 


if __name__ == "__main__":
    main()
