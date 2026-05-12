import os

from .server import mcp


def main():
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "8000"))
    if transport in ("http", "streamable-http", "sse"):
        mcp.run(transport=transport, host=host, port=port)
    else:
        mcp.run(transport="stdio")
