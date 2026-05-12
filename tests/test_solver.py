from solve24_mcp_server.solver import all_solutions_24, solve_24, verify_24


def test_solve_24_basic():
    result = solve_24([1, 2, 3, 4])
    assert result is not None
    assert abs(eval(result) - 24) < 1e-9


def test_solve_24_classic():
    result = solve_24([3, 8, 8, 9])
    assert result is not None
    assert abs(eval(result) - 24) < 1e-9


def test_solve_24_no_solution():
    assert solve_24([1, 1, 1, 1]) is None


def test_all_solutions():
    results = all_solutions_24([1, 2, 3, 4])
    assert len(results) > 1
    for expr in results:
        assert abs(eval(expr) - 24) < 1e-9


def test_all_solutions_no_duplicates():
    results = all_solutions_24([1, 2, 3, 4])
    assert len(results) == len(set(results))


def test_verify_correct():
    is_24, value = verify_24("(1+2+3)*4")
    assert is_24
    assert abs(value - 24) < 1e-9


def test_verify_incorrect():
    is_24, value = verify_24("1+2+3+4")
    assert not is_24
    assert abs(value - 10) < 1e-9


def test_verify_invalid():
    try:
        verify_24("import os")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
