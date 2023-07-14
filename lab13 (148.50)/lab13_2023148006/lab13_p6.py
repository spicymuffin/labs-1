"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab13_p6.py
"""


def fibcalls(n):
    """
    Recursively computes the number of function calls required
    to compute the n-th Fibonacci number.
    """

    if n == 0:
        # one call required to compute first fib number
        return 1
    elif n == 1:
        # one call required to compute second fib number
        return 1
    else:
        # the number of calls required equals to the number
        # of calls required to compute
        # n - 2 th fib number + n - 1 th fib number
        # +1 (this call)
        return fibcalls(n - 2) + fibcalls(n - 1) + 1

