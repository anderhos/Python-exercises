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
    def __init__(self, semi_major, semi_minor, t, w):
        self.semi_major = semi_major
        self.semi_minor = semi_minor
        self.t = t
        self.w = w

    def area(self):
        return np.pi * self.semi_major * self.semi_minor

    def circumference(self):
        """
        Not implemented
        see: https://en.wikipedia.org/wiki/Ellipse#Circumference
        """
        pass


class Circle(Ellipse):
    def __init__(self, semi_major, semi_minor, t, w):
        super().__init__(semi_major, semi_minor, t, w)
        semi_major = semi_minor
        self.radius = semi_major
