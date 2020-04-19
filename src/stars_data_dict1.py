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
# have a list of tuples
data = eval(text)
# making a list of lists instead of list of tuples

input_list = []
for i in data:
    input_list.append(list(i))

# delete not needed items
for j in input_list:
    del j[1:3]

# convert to dictionary
stars_dict = dict(input_list)
print(stars_dict)
print(stars_dict['Alpha Centauri A'])
