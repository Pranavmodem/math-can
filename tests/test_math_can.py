from math_can.operators import Operator

def test_add():
    assert Operator.add(2, 3) == 5

def test_subtract():
    assert Operator.subtract(5, 2) == 3

def test_multiply():
    assert Operator.multiply(3, 4) == 12

def test_divide():
    assert Operator.divide(10, 2) == 5
    try:
        Operator.divide(1, 0)
    except ZeroDivisionError:
        pass
