import itertools
import re


def solve_24(cards: list[int]) -> str | None:
    for nums in itertools.permutations(cards):
        for ops in itertools.product("+-*/", repeat=3):
            exprs = _build_expressions(nums, ops)
            for expr in exprs:
                try:
                    if abs(eval(expr) - 24) < 1e-9:
                        return expr
                except ZeroDivisionError:
                    continue
    return None


def all_solutions_24(cards: list[int]) -> list[str]:
    seen: set[str] = set()
    results: list[str] = []
    for nums in itertools.permutations(cards):
        for ops in itertools.product("+-*/", repeat=3):
            exprs = _build_expressions(nums, ops)
            for expr in exprs:
                try:
                    if abs(eval(expr) - 24) < 1e-9 and expr not in seen:
                        seen.add(expr)
                        results.append(expr)
                except ZeroDivisionError:
                    continue
    return results


def verify_24(expression: str) -> tuple[bool, float]:
    if not re.match(r"^[\d\s+\-*/().]+$", expression):
        raise ValueError("Expression contains invalid characters")
    result = eval(expression)
    return abs(result - 24) < 1e-9, round(result, 6)


def _build_expressions(nums: tuple, ops: tuple) -> list[str]:
    a, b, c, d = nums
    o1, o2, o3 = ops
    return [
        f"(({a}{o1}{b}){o2}{c}){o3}{d}",
        f"({a}{o1}{b}){o2}({c}{o3}{d})",
        f"({a}{o1}({b}{o2}{c})){o3}{d}",
        f"{a}{o1}(({b}{o2}{c}){o3}{d})",
        f"{a}{o1}({b}{o2}({c}{o3}{d}))",
    ]
