# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 5.39: Animate the evolution of Taylor polynomials

"""

from scipy.special import factorial
import numpy as np

#np.linspace
def fk(x):
    return x**k / factorial(k, exact)
M = 0
N = 10
xmin =0
xmax = 3
ymin = 0
ymax = 30
n = 100
exact = np.exp(x)

animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact)

# Sjekk lecture notes for framgangsmåte.
