# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 9.3: Implement a class for a function as a subclass

"""

from dir_subclass import Line
import numpy as np


class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)  # let Line store c0 and c1
        self.c2 = c2

    def __call__(self, x):
        return Line.__call__(self, x) + self.c2 * x**2


class MyFunc(Parabola):
    def __init__(self, c0, c1, c2, w, a):
        super().__init__(c0, c1, c2)
        self.w = w
        self.a = a

    def __call__(self, x):
        return self.a*np.sin(self.w*x) + super().__call__(x)

f = MyFunc(3, 2, 1, 2, 5)
f1 = f(x=2.5)
print(f1)
print(f.table(0, 5, 11))