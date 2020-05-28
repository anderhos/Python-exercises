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
# t: time for one complete orbit
# w: angular velocity
import numpy as np


class Ellipse:
    def __init__(self, semi_major, semi_minor):
        self.semi_major = semi_major
        self.semi_minor = semi_minor

    def area(self):
        return np.pi * self.semi_major * self.semi_minor

    def circumference(self):
        """
        Not implemented
        see: https://en.wikipedia.org/wiki/Ellipse#Circumference
        """
        pass


class Circle(Ellipse):
    def __init__(self, semi_major):
        semi_minor = semi_major
        self.radius = semi_minor
        super().__init__(semi_major, semi_minor)


my_ellipse = Ellipse(4, 3)
print(my_ellipse.area())
my_circle = Circle(4)
print(my_circle.area())
