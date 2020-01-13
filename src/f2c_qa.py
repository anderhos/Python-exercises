# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 4.1: Make an interactive program 
"""

F = input("F = ?")    # Input in fahrenheit
F = float(F)
C = 5/9 * F - 160/9    # Convert to celsius
print(C)