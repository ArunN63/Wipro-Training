import pytest

# 1️⃣ Basic Test Function
def test_sum():
    assert 3 + 5 == 8


# 2️⃣ Assertion Failure (intentionally fails)
def test_upper_fail():
    assert "hello".upper() == "hello"


# 3️⃣ Fixture Usage
@pytest.fixture
def number_list():
    return [1, 2, 3]

def test_list_length(number_list):
    assert len(number_list) == 3


# 4️⃣ Parameterized Test
def square(x):
    return x * x

@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(input, expected):
    assert square(input) == expected


# 5️⃣ Exception Handling
def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)