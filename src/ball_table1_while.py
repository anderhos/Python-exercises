# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 2.8   Make a table of values from a formula
"""
g = 9.81
v0 = 10
n = 10    # number of t intervals
a = 0    # lower bound t
b = 2 * v0/g    # upper bound
h = (b-a)/n    # length of sub-interval

print("  t      y(t)")
t = 0
eps = 1e-6
while t <= b + eps:
    y = v0 * t - 0.5 * g * t**2
    print("%6.2f %6.2f" % (t, y))
    t += h