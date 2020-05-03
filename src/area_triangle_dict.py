# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Edition: 5th Edition
Year: 2016
Exercise 6.9: Compute the area of a triangle

"""

def triangle_area(vertex):
    """
    :param vertex: vertices
    :return: triangle area of vertices
    """
    x1, y1 = vertex[1]
    x2, y2 = vertex[2]
    x3, y3 = vertex[3]
    return 0.5 * abs(x1*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)


# Dictionary with specified vertices numbered from 1 to 3
t_dict = {1: (2, 1),
          2: (-1, 2),
          3: (-1, -1)}

print(f"The area of a triangle with vertices {t_dict[1]}, {t_dict[2]} and "
      f"{t_dict[3]} is {triangle_area(t_dict)}")
