# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 3.20: Write functions
"""

def hw1():
    return("Hello, world!")

def hw2():
    print("Hello, world!")

def hw3(word1, word2):
    return word1 + word2

print(hw1())    
hw2()
print(hw3("Hello, ", "World!"))
print(hw3("Python ", "function"))