# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 5.29: Judge a plot 

"""

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 2, 20)
y1 = np.cos(18*np.pi*x1)
plt.plot(x1, y1, 'r-')

x2 = np.linspace(0, 2, 1000)
y2 = np.cos(18*np.pi*x2)
plt.plot(x2, y2, 'b-')

plt.xlabel('x')
plt.ylabel('y')
plt.savefig('tmp4.pdf')
plt.show()

"""
the first function, the red one, will not have enogh points so the result is 
wrong. The second graph, the blue one, will show the correct plot of how
the function looks like.
"""