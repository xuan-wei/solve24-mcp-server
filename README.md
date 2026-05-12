# solve24-mcp-server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that solves the **24-point card game**.

Given four numbers, it finds arithmetic expressions that evaluate to 24.

## Tools

| Tool | Description |
|------|-------------|
| `solve` | Find one solution for 4 given numbers |
| `solve_all` | Find all distinct solutions for 4 given numbers |
| `verify` | Verify if an expression equals 24 |

## Installation

```bash
pip install solve24-mcp-server
```

Or install from source:

```bash
git clone https://github.com/xuan-wei/solve24-mcp-server.git
cd solve24-mcp-server
pip install -e .
```

## Usage

### As a MCP server

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "solve24": {
      "command": "solve24-mcp-server"
    }
  }
}
```

Or with uvx (no install needed):

```json
{
  "mcpServers": {
    "solve24": {
      "command": "uvx",
      "args": ["solve24-mcp-server"]
    }
  }
}
```

### Run directly

```bash
solve24-mcp-server
# or
python -m solve24_mcp_server
```

## Examples

**solve** `[3, 8, 8, 9]` → `8/(9-8/3)` (or similar)

**solve_all** `[1, 2, 3, 4]` → all distinct expressions equaling 24

**verify** `(1+2+3)*4` → `Correct! (1+2+3)*4 = 24`

## License

Apache-2.0
