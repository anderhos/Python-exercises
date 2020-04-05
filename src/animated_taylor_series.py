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

M = 0
N = 10
k = np.linspace(M, N, N+1)
xmin = 0
xmax = 3
n = 20
x = np.linspace(xmin, xmax, n)

max_fk = fk(xmax, N)
k_values = np.linspace(M, N, N+1)

x = np.linspace(xmin, xmax, n)    # Correct?
exact = np.exp(x)

# plotting the exact function, and making static axes
plt.plot(x, exact)
plt.ion()
y = fk(x, k=N)
lines = plt.plot(x, y)
plt.axis([xmin, xmax, -0.2, max_fk])
plt.xlabel('x')
plt.ylabel('fk')
plt.legend(['k=%4.2f' % M])

# Show movie, and make hardcopies simultanously
counter = 0
for k in k_values:
    y = fk(x, k)
    lines[0].set_ydata(y)
    plt.legend(['k=%4.2f' % k])
    plt.draw()
    plt.savefig('tmp_%04d.png' % counter)
    counter += 1
input('Type Return key: ')
# Sjekk lecture notes for framgangsmåte!
