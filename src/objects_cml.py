# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 4.7: Read input from the command line

"""
import sys

input_value = sys.argv[1]
result = eval(input_value)
print(result, type(result))

"""
When inputing "This is a string" Python interprets This is a string as code.
And there is no variable assigned to this name. We need to add double quotes. 
e.g'"This is a string"'
"""