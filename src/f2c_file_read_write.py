# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 4.4: Read and write several numbers from and to ﬁle

"""
from pprint import *

fahrenheit = []
with open('Fdeg.dat', 'r') as infile:
    for line in range(3):    # Skipping the first three lines
        infile.readline()
    for line in infile:    # Splitting the string
        words = line.split()
        fahrenheit.append(words[2])
    f_degrees = [float(w) for w in fahrenheit]
    # Converting to a list of float values of the fahrenheit degrees
    c_degrees = [5/9 * f - 160/9 for f in f_degrees]
    # Converting to a list with celsius degrees

outfile = open('outfile.txt', 'w')
for f, c in zip(f_degrees, c_degrees):
    outfile.write(f'{f:6.2f} {c:6.2f}\n')

outfile.close()