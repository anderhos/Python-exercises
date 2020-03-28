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
M = 0
N = 10
xmin = 0
xmax = 3
n = 20
x = np.linspace(xmin, xmax, n)    # Correct?
ymin = 0
ymax = 30
# How should y relate to fk? Or is it just defining axis?
exact = np.exp(x)

def fk(x):
    """
    Defining the function for the terms
    """
    return x**k / factorial(k)



def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
    """
    The function to be plotted as a movie
    """
    output = 0
    for _ in range(N+1):    # Accumulating the terms
        new_output = fk(x) + output
        output = new_output
        print(output)
    return output

# Need to combine the two functions?

# Sjekk lecture notes for framgangsmåte!
