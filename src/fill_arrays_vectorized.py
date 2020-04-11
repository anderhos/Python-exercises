# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Edition: 5th Edition
Year: 2016
Exercise 5.3: Fill arrays; vectorized version

"""


import numpy as np


def h(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-0.5*x**2)


n = 41
start = -4
stop = 4
dx = 1/(n-1)

x = np.linspace(start, stop, n)

# fill array y with function values
y = h(x)


print(y)
