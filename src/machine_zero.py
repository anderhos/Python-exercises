# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 2.20: Explore what zero can be on a computer  

"""

"""
1: Storing 1.0 as a value for eps
2: Initializing the while loop iterating as long as
the condition is not true.
3: Inside the while loop. Print a number of dots followed by the eps
4: Dividing eps by two and storing the new eps value
5: After termination of the while loop printing the
final value of eps.
"""
eps = 1.0
while 1.0 != 1.0 + eps:
    print("...............", eps)
    eps = eps/2.0
print("final eps:", eps)

# Python interprets 10**(-16) as zero