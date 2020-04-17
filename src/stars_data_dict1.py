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


def read_stars(filename):

    infile = open(filename, "r")
    # skipping first line
    infile.readline()
    luminosities = {}
    for line in infile:
        words = line.split()
        # luminosity is the last word in line
        luminosity = words[-1]
        # type luminosity is a string
        # Need to remove characters ), so we can convert to float
        # removing the three last words to get star name
        if len(words[:-3]) == 4:
            star = words[0] + ' ' + words[1] + ' ' + words[2] + ' ' + words[3]
        elif len(words[:-3]) == 3:
            star = words[0] + ' ' + words[1] + ' ' + words[2]
        elif len(words[:-3]) == 2:
            star = words[0] + ' ' + words[1]
        else:
            star = words[0]
        # type star is a string but has extra character ( in the beginning
        # of every name

        luminosities[star] = luminosity
    infile.close()
    return luminosities


output = read_stars("stars.txt")
print(output)
"""
keys and values are correct but with extra characters around as mentioned
"""