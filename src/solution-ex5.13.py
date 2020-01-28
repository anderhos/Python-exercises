# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
-----------
SOLUTUION
-----------

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

#the code needs exactly 3 command-line args
y0, theta, v0 = [float(arg) for arg in sys.argv[1:]]

g = 9.81

"""
We should plot for y=f(x)>0, so
we must solve a quadratic equation
a*x**2 +b*x + c = 0
to find the right range of x values.
"""

a = -1.0/(2*v0**2)*g/(cos(theta)**2)
b = tan(theta)
c = y0
x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)

x_max = max(x1,x2)
x = np.linspace(0,x2,101)

#simple formula since a,b,c were defined above:
y = a*x**2 + b*x + c

plt.plot(x,y)
plt.savefig('solution-ex5.13.pdf')
plt.show()
