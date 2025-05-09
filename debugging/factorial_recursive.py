#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
        n (int): The number to calculate the factorial of. Should be a non-negative integer.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the first command-line argument, convert to int, and calculate factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
