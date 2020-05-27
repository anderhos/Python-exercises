# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 9.2: Make polynomial subclasses of parabolas

"""
from sin_plus_quadratic import Parabola
# from dir_subclass import Line


class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        super().__init__(c0, c1, c2)    # Let parabola store c0, c1, c2
        self.c3 = c3

    def __call__(self, x):
        print("Call to Cubic")
        return super().__call__(x) + self.c3 * x**3


class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        super().__init__(c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        print("Call Poly4")
        return super().__call__(x) + self.c4 * x**4


f = Cubic(1, 2, 3, 4)
f1 = f(x=2.5)
print("f1 = ", f1)
# print("f_table = ", f.table(0, 5, 11))

g = Poly4(1, 2, 3, 4, 5)
g2 = g(x=2.5)
print("g2 = ", g2)
# print("g_table = ", g.table(0, 5, 11))
