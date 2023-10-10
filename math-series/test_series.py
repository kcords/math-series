import pytest

from series import fibonacci, lucas, sum_series

def test_sum_series_one():
    expected = 0
    actual = sum_series(1)
    assert expected == actual

def test_sum_series_two():
    expected = 1
    actual = sum_series(2)
    assert expected == actual

def test_sum_series_three():
    expected = 1
    actual = sum_series(3)
    assert expected == actual

def test_sum_series_four():
    expected = 2
    actual = sum_series(4)
    assert expected == actual

def test_sum_series_ten():
    expected = 34
    actual = sum_series(10)
    assert expected == actual

def test_sum_series_large_number():
    expected = 218922995834555169026
    actual = sum_series(100)
    assert expected == actual

def test_sum_series_one_with_optional_params():
    expected = 2
    actual = sum_series(1, 2, 1)
    assert expected == actual

def test_sum_series_two_with_optional_params():
    expected = 1
    actual = sum_series(2, 2, 1)
    assert expected == actual

def test_sum_series_three_with_optional_params():
    expected = 3
    actual = sum_series(3, 2, 1)
    assert expected == actual

def test_sum_series_four_with_optional_params():
    expected = 4
    actual = sum_series(4, 2, 1)
    assert expected == actual

def test_sum_series_ten_with_optional_params():
    expected = 76
    actual = sum_series(10, 2, 1)
    assert expected == actual

def test_sum_series_large_number_with_optional_params():
    expected = 489526700523968661124
    actual = sum_series(100, 2, 1)
    assert expected == actual

def test_sum_series_and_fibonacci_same_result_ten():
    expected = 34
    fibonacci_actual = fibonacci(10)
    sum_series_actual = sum_series(10)
    assert expected == fibonacci_actual == sum_series_actual

def test_fibonacci_five():
    expected = 3
    actual = fibonacci(5)
    assert expected == actual

def test_sum_series_and_lucas_same_result_ten():
    expected = 76
    lucas_actual = lucas(10)
    sum_series_actual = sum_series(10, 2, 1)
    assert expected == lucas_actual == sum_series_actual

def test_lucas_five():
    expected = 7
    actual = lucas(5)
    assert expected == actual
