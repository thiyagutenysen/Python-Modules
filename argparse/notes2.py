# this is usual code
import argparse
import sys


def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y


ans = calculate(3, 5, "add")
print(ans)
