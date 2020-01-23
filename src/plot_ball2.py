# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 5.10: Plot a formula for several parameters 

"""


import matplotlib.pyplot as plt
import numpy as np
import sys

g = 9.81
n = 51
for v0 in sys.argv[1:]:
    v0 = float(v0)
    t = np.linspace(0, 2*v0/g, n)
    y = v0 * t - 0.5 * g * t**2
    plt.plot(t, y)

plt.xlabel('s')
plt.ylabel('m')
plt.show()