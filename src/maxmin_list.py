# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 3.28: Find the max and min elements in a list 
"""
a = [11, 7, 4, 1, 3, 9]

max_list = a[0]
for i in range(1, len(a)):
    if a[i] > max_list:
        max_list = a[i]
print(max_list)

min_list = a[0]
for i in range(1, len(a)):
    if a[i] < min_list:
        min_list = a[i]
print(min_list)