# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise A.1: Determine the limit of a sequence 

"""

from numpy import *
from math import ceil

# ex (a)

#a0 = 4
N = 100
index_set = range(0, N+2)
print(index_set)
a = zeros(len(index_set))
print(len(index_set))
print(len(a))

#a[0] = a0
for n in index_set[0:N+2:2]:
    a[n] = (7 + 1 / (n + 1)) / 3 - 1/(n + 1)**2

print(a)

"""
Comment:
The computed value for a[n] when n is large is 2.337 it is an approximation
of the excact limit 8/3 when n goes to infinity

"""

# ex (b)

