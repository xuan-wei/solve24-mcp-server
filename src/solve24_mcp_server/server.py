from fastmcp import FastMCP

from .solver import all_solutions_24, solve_24, verify_24

mcp = FastMCP(
    name="solve24-mcp-server",
    instructions="A MCP server that solves the 24-point card game. "
    "Given four numbers, find arithmetic expressions that evaluate to 24.",
)


@mcp.tool()
def solve(cards: list[int]) -> str:
    """Find one arithmetic expression using four numbers that equals 24.

    Args:
        cards: A list of exactly 4 integers (1-13).

    Returns:
        An arithmetic expression that equals 24, or a message if no solution exists.
    """
    if len(cards) != 4:
        return "Error: exactly 4 numbers required"
    result = solve_24(cards)
    if result is None:
        return f"No solution found for {cards}"
    return result


@mcp.tool()
def solve_all(cards: list[int]) -> str:
    """Find all distinct arithmetic expressions using four numbers that equal 24.

    Args:
        cards: A list of exactly 4 integers (1-13).

    Returns:
        All distinct solutions, one per line.
    """
    if len(cards) != 4:
        return "Error: exactly 4 numbers required"
    results = all_solutions_24(cards)
    if not results:
        return f"No solution found for {cards}"
    return f"Found {len(results)} solution(s):\n" + "\n".join(results)


@mcp.tool()
def verify(expression: str) -> str:
    """Verify whether an arithmetic expression equals 24.

    Args:
        expression: An arithmetic expression string (e.g., "(1+2+3)*4").

    Returns:
        Whether the expression equals 24 and its actual value.
    """
    try:
        is_24, value = verify_24(expression)
    except (ValueError, SyntaxError) as e:
        return f"Invalid expression: {e}"
    if is_24:
        return f"Correct! {expression} = {value}"
    return f"Incorrect. {expression} = {value}, not 24"
