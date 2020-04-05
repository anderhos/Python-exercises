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
import matplotlib.pyplot as plt
import numpy as np

M = 0
N = 10
xmin = 0
xmax = 3
n = 20
x = np.linspace(xmin, xmax, n)    # Correct?
ymin = 0
ymax = 30
exact = np.exp(x)

def fk(x, k):
    """
    Defining the function for the terms
    """
    return x**k / factorial(k)




# Sjekk lecture notes for framgangsmåte!
