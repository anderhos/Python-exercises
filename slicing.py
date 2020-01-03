# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

import numpy as np

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 2nd Edition
Year: 2011

Ex 5.6 Demonstrate array slicing
"""

y = [i/10 for i in range(31)]    # Create array
w = np.array(y)

print("first: " , w[:])
print("second: ", w[:-2])
print("third: ", w[::5])    # output with step 5 - > 0. 0.5 1. ...
print("forth: ", w[2:-2:6])    # output start 2, stop -2, step 6 -> 0.2 0.8
# 1.4 2.0 2.6

print("w: ", w)   # the entire array
print(type(w))