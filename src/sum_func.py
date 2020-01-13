# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 3.7: Evaluate a sum and write a test function   

"""

def sum_1k(M):
    """
    defining summing formula
    """
    s = 0
    for k in range(1, M + 1):
        s += 1/k
    return s

