# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Edition: 5th Edition
Year: 2016
Exercise 5.1: Fill lists with function values

"""

import numpy as np


def h(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-0.5*x**2)


n = 41
interval = len(range(-4, 4))    # The length of the interval of x
dx = interval/(n-1)    # Length of step
x0 = -4    # Starting value for x
xlist = [x0 + i*dx for i in range(n)]
ylist = [h(x) for x in xlist]
list_pairs = [[x, y] for x, y in zip(xlist, ylist)]

print(list_pairs)