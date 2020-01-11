# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise 2.19: Explore round-off errors from a large number of inverse
operations  

"""
"""
Detailed description of what the program does

1: Import the squre root function from the math module
2: Initializing the outer for loop. 
3: Storing a value for r
4: Entering first inner for-loop for each value of n
5: Taking the squarroot and storing a new value of r
6: Entering second inner for-loop for each value of n
7: Squaring and storing a new value of r that should be
an approximately the same as line 3.
8: Printing for each value of n the value of r that is
returned after taking the square root n times and then
squaring the same number of times.
"""


from math import sqrt
for n in range(1, 60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
        print("for n = %d, sqrt r is %f" % (n, r))
    for i in range(n):
        r = r**2
        print("for n = %d, **2 is %f" % (n, r))
    print("%d times sqrt and **2: %.128f" % (n, r))

# When n is large the number of digits that math uses is overloaded.
# Which causes round-off errors