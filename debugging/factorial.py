#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: factorial is not defined for negative numbers")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Error: please provide an integer as argument")
else:
    print("Usage: {} <number>".format(sys.argv[0]))
