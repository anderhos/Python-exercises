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
# Load the file. Execute the text as code
with open('stars.txt', 'r') as infile:
    exec(infile.read())
# Now data is a list of tuples

#creating empty dictionary
stars_dict = {}
# assigning star to key and lumiosity to value
for i in data:
    stars_dict[i[0]] = i[-1]

print(stars_dict)
print(stars_dict['Alpha Centauri A'])
