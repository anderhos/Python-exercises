# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 2.7: Generate equally spaced coordinates 
"""

n = 10    # intervals
a = 2    # Choosing an arbitrary value of a and b
b = 7
h = (b-a)/n    # interval length

comp_list = [a + i*h for i in range(n+1)]
print(comp_list)