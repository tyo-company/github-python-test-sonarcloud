# string_and_math.py

def concatenate_strings(str1, str2):
    return str1 + str2

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
