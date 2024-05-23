# test_string_and_math.py

import pytest
from string_and_math import (
    concatenate_strings,
    reverse_string,
    is_palindrome,
    factorial,
    fibonacci
)

def test_concatenate_strings():
    assert concatenate_strings("Hello, ", "world!") == "Hello, world!"
    assert concatenate_strings("", "test") == "test"
    assert concatenate_strings("test", "") == "test"

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""

def test_is_palindrome():
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")
    assert is_palindrome("")

# def test_factorial():
#     assert factorial(0) == 1
#     assert factorial(5) == 120
#     assert factorial(3) == 6
#     with pytest.raises(ValueError):
#         factorial(-1)

# def test_fibonacci():
#     assert fibonacci(0) == 0
#     assert fibonacci(1) == 1
#     assert fibonacci(5) == 5
#     assert fibonacci(10) == 55
#     with pytest.raises(ValueError):
#         fibonacci(-1)
