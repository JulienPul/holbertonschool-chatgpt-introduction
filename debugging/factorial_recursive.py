#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: {} <non-negative integer>".format(sys.argv[0]))
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Error: factorial is not defined for negative numbers")
        sys.exit(1)
except ValueError:
    print("Error: please provide a valid integer")
    sys.exit(1)

# Warning: recursion limit!
if num > 998:
    print("Warning: number too large for recursion, use an iterative version")
    sys.exit(1)

print(factorial(num))
