# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 5.1: Fill lists with function values

"""

import numpy as np

def h(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-0.5*x**2)
n = 41
dx = 8.0/(n-1)
xlist = [i*dx for i in range(n)]
hlist = [h(x) for x in xlist]

print(xlist)
print(hlist)