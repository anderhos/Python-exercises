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
import matplotlib.pyplot as plt

# ex (a)

#a0 = 4
N = 100
index_set = range(0, N+1)
a = zeros(len(index_set))

#a[0] = a0
for n in index_set[0:N+1]:
    a[n] = (7 + 1 / (n + 1)) / (3 - 1/(n + 1)**2)


"""
Comment:
The computed value for a[n] when n is large is 2.337 it is an approximation
of the excact limit 8/3 when n goes to infinity

"""


# ex (b)

# Defining function

def Dn(N):
    result = zeros(N+1)
    for n in range(N+1):
        result[n] = sin(2**(-n)) / 2**(-n)
    return result

# Computing for large N

a = Dn(100)    # 101 elements


# ex (c)

def D(f, x, N):
    res = zeros(N+1)
    for n in range(N+1):
        h = 2**(-n)
        res[n] = (f(x+h) - f(x)) / h
    return res

if __name__ == "__main__":
    f = sin
    N = 80
    for x in [0, pi]:
        d = D(f, x, N)
        plt.figure()
        plt.plot(arange(0,N+1), d, 'o')
        plt.xlabel('N')
        plt.ylabel('D')
        plt.show()
    # ex (d)

# Expect the limit to be cos(pi) = -1
"""

ed (e): To many digits gives us a round of error. The numerator becomes zero
for large values of N
"""