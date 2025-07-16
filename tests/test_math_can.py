import pytest
from math_can.jobs.math_can import MathCan

@pytest.fixture
def math_can():
    return MathCan()

def test_add(math_can):
    assert math_can.operations['add'](2, 3) == 5

def test_subtract(math_can):
    assert math_can.operations['subtract'](5, 2) == 3

def test_multiply(math_can):
    assert math_can.operations['multiply'](3, 4) == 12

def test_divide(math_can):
    assert math_can.operations['divide'](10, 2) == 5

def test_percentage(math_can):
    assert math_can.operations['percentage'](25, 100) == 25

def test_power(math_can):
    assert math_can.operations['power'](2, 3) == 8

def test_modulus(math_can):
    assert math_can.operations['modulus'](10, 3) == 1

def test_floor_divide(math_can):
    assert math_can.operations['floor_divide'](10, 3) == 3

def test_absolute(math_can):
    assert math_can.operations['absolute'](-5) == 5
