"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab13_p5.py
"""

fib_cache = {}


def fib_memo(n):
    """Recursively computes the n-th Fibonacci number using memoization."""

    global fib_cache

    if n == 0:  # first fib number is always 0
        return 0
    elif n == 1:  # seconds fib number is always 1
        return 1
    elif n in fib_cache:  # retrun cached value if exists in cache
        return fib_cache[n]
    else:
        fib = fib_memo(n - 2) + fib_memo(n - 1)
        fib_cache[n] = fib  # cache if value us new
        return fib  # nth fib number is sum of two previous fib numbers
