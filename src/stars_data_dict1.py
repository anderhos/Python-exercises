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
File not working as it should. Get a dictionary, but keys and values are
not as they should be.
"""

"""
Remember: In the file we have a list of four tuples, not a table as in
e.g density.py
"""

"""
Try to read the whole file into one string. Combining the four-tuples


"""


def read_stars(filename):

    infile = open(filename, "r")
    # skipping first line
    infile.readline()
    filestr = infile.read()
    return filestr


output = read_stars("stars.txt")
print(output)
print(type(output))
"""
keys and values are correct but with extra characters around as mentioned
"""