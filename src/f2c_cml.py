# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 4.2: Read a number from the command line

""" 
import sys

F = float(sys.argv[1])
C = 5/9 * F - 160/9    # Convert to celsius
print(C)
