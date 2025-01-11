from main import solve_quadratic

def test_two_roots():
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)

def test_one_root():
    assert solve_quadratic(1, 2, 1) == (-1.0, None)

def test_no_root():
    assert solve_quadratic(1, 0, 1) == None

def test_float_coefficients():
    assert solve_quadratic(0.5, -1.5, 1) == (2.0, 1.0)

def test_a_is_zero():
    assert solve_quadratic(0, 2, -4) == (2.0, None)
