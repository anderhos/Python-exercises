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
stars in first column in file and luminosity in third column

"""

"""
File not working as i should. Only first name of star and returns
a list within a dictionary it seems
"""


def read_stars(filename):
    infile = open(filename, "r")
    luminosities = {}
    for line in infile:
        words = line.split()
        luminosity = words[-1]
        # Need fix, include all the words in the star.
        # Check density.py
        star = words[0]
        luminosities[star] = luminosity
    infile.close()
    return luminosities


luminosities_dict = read_stars("stars.txt")
print(luminosities_dict)
