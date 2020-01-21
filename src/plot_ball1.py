# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 5.9: Plot a formula

"""

import matplotlib.pyplot as plt
import numpy as np

v0 = 10
g = 9.81
t = np.linspace(0, 2*v0/g, 51)
y = v0 * t - 0.5 * g * t**2

plt.xlabel('s')
plt.ylabel('m')

plt.plot(t, y)
plt.show()