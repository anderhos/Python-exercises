# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 5.11: Specify the extent of the axes in a plot 

"""

import matplotlib.pyplot as plt
import numpy as np
import sys

g = 9.81
n = 51

def f(t):
    return v0 * t - 0.5 * g * t**2

for v0 in sys.argv[1:]:
    v0 = float(v0)
    t = np.linspace(0, 2 * v0 / g, n)
    y = f(t)
    max_y = np.amax(y)
    min_y = np.amin(y)
    max_t = np.amax(t)
    min_t = np.amin(t)
    print(max_y)
    print(min_y)
    print(max_t)
    print(min_t)
    plt.plot(t, y)

plt.xlabel('s')
plt.ylabel('m')
plt.axis([0, 15, 0, 200])
plt.savefig('plot_ball3.pdf')
plt.show()