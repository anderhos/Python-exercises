# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 2.1  Make a Fahrenheit-Celsius conversion table
"""

print("--------------------------")

F = 0
dF = 10    # Increment F
while F <= 100:
    C = 5 / 9 * F - 160 / 9  # Conversion formula
    print(C, F)
    F += dF

print("------------------------")
