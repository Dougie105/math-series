from series import fibonacci, lucas, sum_series

################################# Fibonacci Tests #################################

def test_one():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_two():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_three():
    expected = 1
    actual = fibonacci(2)
    assert expected == actual

def test_four():
    expected = 2
    actual = fibonacci(3)
    assert expected == actual

def test_five():
    expected = 3
    actual = fibonacci(4)
    assert expected == actual

def test_six():
    expected = 5
    actual = fibonacci(5)
    assert expected == actual

################################# Lucas Tests #################################

def test_seven():
    expected = 2
    actual = lucas(0)
    assert expected == actual

def test_eight():
    expected = 1
    actual = lucas(1)
    assert expected == actual

def test_nine():
    expected = 3
    actual = lucas(2)
    assert expected == actual

def test_ten():
    expected = 4
    actual = lucas(3)
    assert expected == actual

def test_eleven():
    expected = 7
    actual = lucas(4)
    assert expected == actual

def test_twelve():
    expected = 11
    actual = lucas(5)
    assert expected == actual

################################# Sum Series Tests #################################

def test_thirteen():
    expected = 2
    actual = sum_series(1, 1, 2)
    assert expected == actual

def test_fourteen():
    expected = 1
    actual = sum_series(2, 1, 2)
    assert expected == actual

def test_fifteen():
    expected = 5
    actual = sum_series(3, 2, 3)
    assert expected == actual

def test_sixteen():
    expected = 10
    actual = sum_series(4, 3, 4)
    assert expected == actual

def test_seventeen():
    expected = 22
    actual = sum_series(5, 4, 5)
    assert expected == actual

def test_eighteen():
    expected = 43
    actual = sum_series(6, 5, 6)
    assert expected == actual