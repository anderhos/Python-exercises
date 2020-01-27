# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 5.13: Plot the trajectory of a ball 

"""

import matplotlib.pyplot as plt
from numpy import *
import sys

g = 9.81
n = 51

def f(x):
    return x * tan(theta) - 1/(2 * v0**2) * (g * x**2)/cos(theta)**2 + y0


y0 = sys.argv[1]
y0 = float(y0)
theta = sys.argv[2]
theta = float(theta)
v0 = sys.argv[3]
v0 = float(v0)

x = linspace(0, 10, n)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""

for y0 in sys.argv[1]:
    for theta in sys.argv[2]:
        for v0 in sys.argv[3:]:
            y0 = float(y0)
            theta = float(theta)
            v0 = float(v0)
            x = linspace(0, 10, n)
            y = f(x)
            plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""