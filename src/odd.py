# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 2.4  Generate odd numbers
"""

n = 10    # The number of elements to check
odd = []    # list of odd numbers
k = 0
while k <= n:
    if k//2 < k/2:
        odd.append(k)
    k += 1
print(odd)
