# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 9.1: Demonstrate the magic of inheritance

"""

import numpy as np

class Line:

    """
    A class for straight lines
    """

    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return self.c0 + self.c1 * x

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

class Parabola0(Line):
    pass


l = Line(1, 3)
p = Parabola0(1, 3)

#print(dir(p))
#print(dir(l))
#print(l.__dict__)
#print(p.__dict__)

