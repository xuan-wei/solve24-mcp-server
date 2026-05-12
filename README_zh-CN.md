# solve24-mcp-server

一个用于算 **24 点** 的 [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) 服务器。

输入四个数字，找出能算出 24 的四则运算表达式。

## 工具列表

| 工具 | 描述 |
|------|------|
| `solve` | 给定 4 个数字，返回一个 24 点解法 |
| `solve_all` | 给定 4 个数字，返回所有不重复的解法 |
| `verify` | 验证一个算式是否等于 24 |

## 安装

```bash
pip install solve24-mcp-server
```

或从源码安装：

```bash
git clone https://github.com/xuan-wei/solve24-mcp-server.git
cd solve24-mcp-server
pip install -e .
```

## 使用方法

### 作为 MCP 服务器

在 MCP 客户端配置中添加：

```json
{
  "mcpServers": {
    "solve24": {
      "command": "solve24-mcp-server"
    }
  }
}
```

或使用 uvx（无需安装）：

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

### 直接运行

```bash
solve24-mcp-server
# 或
python -m solve24_mcp_server
```

## 示例

**solve** `[3, 8, 8, 9]` → `8/(9-8/3)`

**solve_all** `[1, 2, 3, 4]` → 返回所有等于 24 的不同表达式

**verify** `(1+2+3)*4` → `正确！(1+2+3)*4 = 24`

## 许可证

Apache-2.0
