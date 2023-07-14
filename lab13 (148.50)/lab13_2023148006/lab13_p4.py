"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab13_p4.py
"""


def fib(n):
    """Recursively computes the n-th Fibonacci number."""
    if n == 0:  # first fib number is always 0
        return 0
    elif n == 1:  # seconds fib number is always 1
        return 1
    else:
        return fib(n - 2) + fib(
            n - 1
        )  # nth fib number is sum of two previous fib numbers
