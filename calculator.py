"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return print("Error")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a, b):
    if (a >= 0 or b > 1):
        raise ValueError
    else:
        return math.log(a,b)

def exp(a, b):
    return a**b

def hypotenuse(a,b):
    return math.hypot(a,b)




def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a, b):

    return a *b

def log(a,b):
    try:
        return math.log(a,b)
    except ValueError:
        return print("Error")

def exp(a,b):
    return a**b