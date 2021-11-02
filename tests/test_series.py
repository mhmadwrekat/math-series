from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_lucas():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_sum_seriesA():
    expected = 1
    actual = sum_series(1)
    assert actual == expected

def test_sum_seriesB():
    expected = 2
    actual = sum_series(0, 2, 1)
    assert actual == expected