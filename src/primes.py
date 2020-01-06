# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 2.3   Work with a list
"""

primes = [2, 3, 5, 7, 11, 13]
for i in primes:
    print(i)

p = 17
primes.append(p)
print(primes)