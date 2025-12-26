from fastmcp import FastMCP

from tools.math_tools import add_numbers, multiply_numbers, subtract_numbers
from tools.text_tools import word_count
from tools.misc_tools import random_quote, current_time, server_info

mcp = FastMCP("math-mcp-server")

# Register tools
mcp.tool()(add_numbers)
mcp.tool()(multiply_numbers)
mcp.tool()(subtract_numbers)
mcp.tool()(word_count)
mcp.tool()(random_quote)
mcp.tool()(current_time)
mcp.resource("info://server")(server_info)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) #streamable
    #mcp.run()
