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

"""
Mye som må gjøres om. Forsøk å løse det med tall først
uten plotting.
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


# testing function and summation
for x in range(0, 3):
    exact = np.exp(x)  # The exact value we want to estimate
    old_value = 0  # Initial value of summation before adding any terms
    for k in range(0,10):
        new_value = old_value + fk(x, k)
        # Storing the new value now old for next iteration
        old_value = new_value
        print("Value of x: %d Number of terms: %d Sum = %f Exact value = %f"
              % (x, k+1, old_value, exact))