# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 3.7: Evaluate a sum and write a test function - Test function  

"""
import sum_func as sf

def test_sum_1k():
    # Testing that the formula works correctly
    assert sf.sum_1k(3) == 11/6
