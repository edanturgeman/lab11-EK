"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


#https://github.com/edanturgeman/lab11-EK
#Partner 1: Edan Turgeman
#Partner 2: Kevin Taing
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


