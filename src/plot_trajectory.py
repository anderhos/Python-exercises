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
import numpy as np
import sys
from math import cos, tan, sqrt

g = 9.81
n = 101

y0 = sys.argv[1]
y0 = float(y0)
theta = sys.argv[2]
theta = float(theta)
v0 = sys.argv[3]
v0 = float(v0)

"""
To plot the graph we need to solve the quadratic function 
y = f(x) = a*x**2 + b*x + c for f(x) > 0.
We must find the max root. Because the min root is negative in our case.
"""

a = -1.0/(2*v0**2)*g/(cos(theta)**2)
b = tan(theta)
c = y0

roots = np.roots([a, b, c])
x_max = max(roots)
x = np.linspace(0, x_max, n)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('plot_trajectory.pdf')
plt.show()
