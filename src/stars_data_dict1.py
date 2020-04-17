        # -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Edition: 5th Edition
Year: 2016
Exercise 6.5: Make a dictionary

"""

"""
Making a dictionary with the names of stars and their luminosity
stars in first column in file and luminosity in fourth column

"""

"""
File not working as it should. Only first name of star and returns
a list within a dictionary it seems
"""

"""
Try new implementation. Remove 2 columns, second last and third last
"""

"""
A list of four tuples, not a table as in density.py
"""
def read_stars(filename):
    infile = open(filename, "r")
    lines = [line for line in infile]
    infile.close()
    return lines

print(read_stars("stars.txt"))

