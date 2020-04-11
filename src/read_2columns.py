# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Edition: 5th Edition
Year: 2016
Exercise 5.14: Plot data in a two-column file

"""

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

# open file to process
infile = open('xy.dat', 'r')

for line in infile:
    data = line.split()
    x.append(float(data[0]))
    y.append(float(data[1]))

# converting y to array before computations
y2 = np.array(y)

# make plot of data
plt.plot(x, y2)
plt.show()

mean_y2 = np.mean(y2)
max_y2 = np.max(y2)
min_y2 = np.min(y2)

print(f"Mean of y2 is {mean_y2}")
print(f"Max of y2 is {max_y2}")
print(f"Min of y2 is {min_y2}")