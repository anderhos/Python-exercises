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
import glob, os

# Clean up old frames
for name in glob.glob('tmp_*.png'):
    os.remove(name)

def fk(x, k):
    """
    Defining the function for the terms
    """
    return x**k / factorial(k)

# limits
M = 0
N = 10
# steps
n = 11
x = 1
k_min = M

k_values = np.linspace(M, N, n)

# first plot

old_value = 0
exact = np.exp(x)
for k in k_values:
    new_value = old_value + fk(x, k)
    # Storing the new value now old for next iteration
    old_value = new_value
    #print("Value of x: %d Number of terms: %d Sum = %f Exact value = %f"
     #     % (x, k+1, old_value, exact))

# Plot the approximation
