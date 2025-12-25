### 🚀 MCP Projects with FastMCP

This repository contains hands-on projects, experiments, and examples built using FastMCP, a lightweight framework for creating Model Context Protocol (MCP) servers and tools.
The goal of this repo is to explore how MCP enables structured, tool-driven interactions between LLMs and external capabilities—focusing on clarity, simplicity, and extensibility.

📌 What is MCP?
Model Context Protocol (MCP) is a standard that allows Large Language Models to:

- Discover tools
- Call tools with structured inputs
- Receive typed, deterministic outputs

MCP helps bridge the gap between LLM reasoning and real-world actions.

⚡ Why FastMCP?
FastMCP simplifies MCP server development by:

- Reducing boilerplate
- Providing a clean decorator-based API
- Making tools easy to define and test
- Supporting rapid prototyping of MCP servers


This repository uses FastMCP exclusively to build MCP-compatible tools and services.

🧩 Project Structure
fastmcp-demo-server/
│
├── server.py
│
├── tools/
│   ├── math_tools.py
|   |-- misc_tools.py
│   ├── text_tools.py
│
├── agents/
│   ├── agent_ready_mcp.py
│
├── experiments/
│   ├── tool_chaining.py
│
├── requirements.txt
└── README.md


🛠 Example: Simple FastMCP Server
from fastmcp import FastMCP
import random

mcp = FastMCP("demo server")

@mcp.tool()
def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def get_random_number(start: int, end: int) -> int:
    """Get a random number between start and end"""
    return random.randint(start, end)

if __name__ == "__main__":
    mcp.run()

This exposes:

- add_two_numbers
- get_random_number
as MCP-compliant tools that can be consumed by LLM agents.

▶️ Running the MCP Server
1️⃣ Install dependencies
pip install fastmcp

or
pip install -r requirements.txt

2️⃣ Start the server
python basic/02_simple_tools.py

The MCP server will start and wait for tool invocations.

🔍 Testing with MCP Debugger
You can test tools using:

- MCP Debugger
- MCP-compatible agents
- LangChain / custom agent wrappers
