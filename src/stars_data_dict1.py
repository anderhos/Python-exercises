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
# Load the file into a list of lines
with open('stars.txt', 'r') as infile:
    text = infile.read()
# Stripping off characters
text = text.strip('data = ')
data = eval(text)
print(data)
print(type(data))

"""
Remember: In the file we have a list of four tuples, not a table as in
e.g density.py
"""





# Also have a look on the other branch
# have a closer look on stack overflow links
# also a look on standard library tutorial
# link https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries
