from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    excepted = 1
    assert actual == excepted

def test_fibonacci_three():
    actual = fibonacci(3)
    excepted = 2
    assert actual == excepted

def test_fibonacci_six():
    actual = fibonacci(6)
    excepted = 8
    assert actual == excepted


def test_lucas_0():
    actual = fibonacci(0)
    excepted = 2
    assert actual == excepted
def test_lucas_one():
    actual = fibonacci(1)
    excepted = 1
    assert actual == excepted
def test_lucas_two():
    actual = fibonacci(2)
    excepted = 3
    assert actual == excepted
def test_lucas_three():
    actual = fibonacci(3)
    excepted = 4
    assert actual == excepted
def test_lucas_six():
    actual = fibonacci(6)
    excepted = 18
    assert actual == excepted


def test_sum_series_one():
    actual = fibonacci(1)
    excepted = 1
    assert actual == excepted
def test_sum_series_two():
    actual = fibonacci(2)
    excepted = 3
    assert actual == excepted
def test_sum_series_three():
    actual = fibonacci(3)
    excepted = 4
    assert actual == excepted
def test_sum_series_six():
    actual = fibonacci(6)
    excepted = 18
    assert actual == excepted