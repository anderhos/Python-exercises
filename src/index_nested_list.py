# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 2.15: Index a nested list
"""

q = [['a', 'b', 'c',], ['d', 'e', 'f'], ['g', 'h']]    # nested list
print(q[0][0])    # prints 'a'
print(q[1])
print(q[2][1])    # prints 'h'
print(q[1][0])

for i in q:
    for j in range(len(i)):
        print(i[j])

print(type(i))
print(type(j))

# i is a list object. i can be one of the three lists in q
# j is an integer number. j is the index of the element in the corresponding
# list i