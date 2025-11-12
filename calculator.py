"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return print("Error")


def hypotenuse(a,b):
    return math.hypot(a,b)




def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a, b):

    return a *b

def div(a,b):
    try:
        return b/a
    except ZeroDivisionError:
        return print("Error")

def log(a,b):
    try:
        return math.log(a,b)
    except ValueError:
        return print("Error")

def exp(a,b):
    return a**b