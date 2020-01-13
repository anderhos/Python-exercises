# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 4.3: Read a number from a ﬁle

"""

with open('sample1.txt', 'r') as infile:
    for line in range(1, 4):    # Skipping the first three lines
        infile.readline()
    for line in infile:    # Splitting the string
        words = line.split()
    fahrenheit = words[2]
    print(fahrenheit)
