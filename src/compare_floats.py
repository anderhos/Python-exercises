# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 2.21: Compare two real numbers with a tolerance   

"""
a = 1/947.0*947
b = 1
tol = 1e-15
if abs(a-b) < tol:
    print("Wrong result!")
print("a is %.20f" % a)
print(tol)

# Modifying tol to see when the error represented by abs(a-b) is
# within the level of tolerance