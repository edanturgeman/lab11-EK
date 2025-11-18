#https://github.com/edanturgeman/lab11-EK
#Partner 1: Edan Turgeman
#Partner 2: Kevin Taing
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""



# First example
import math

import math

def square_root(a):
    if type(a) is not int:
        raise ValueError
    elif a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def subtract(a,b):
    return a - b

def logarithm(a,b):
    if type(a) is not int or type(b) is not int:
        raise ValueError
    elif a >= 1 or b >= 1:
        return math.log(a,b)
    else:
        raise ValueError


def exp(a, b):
    return a**b

def hypotenuse(a,b):
    return math.hypot(a,b)


