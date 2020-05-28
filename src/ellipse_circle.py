# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 9.5: Make circle a subclass of an ellipse

"""
import numpy as np


# semi_major = a
# semi_minor = b

class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return np.pi * self.a * self.b

    def circumference(self):
        """
        Formula
        see: https://en.wikipedia.org/wiki/Ellipse#Circumference
        """
        return np.pi * (3 * (self.a + self.b) -
                        np.sqrt(10 * self.a * self.b) +
                        3 * (self.a ** 2 + self.b ** 2))


class Circle(Ellipse):
    def __init__(self, a):
        b = a
        self.radius = b
        super().__init__(a, b)


my_ellipse = Ellipse(4, 3)
print(my_ellipse.area())
my_circle = Circle(4)
print(my_circle.area())
