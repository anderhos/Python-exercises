# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Edition: 5th Edition
Year: 2016
Exercise 6.7: Make a nested dictionary from a file

"""


infile = open("human_evolution.txt", "r")

# column number limits from file
hu_start = 0
w_start = 21
he_start = 37
m_start = 50
b_start = 61
end = 89

# empty dictionary
human_dict = {}
for line in infile:
    # Since every human spcies starts with H in file
    if line[0] == 'H':
        # Strip of leading and trailing spaces
        # making sub-dictionaries
        human = line[hu_start:w_start].strip()
        when = line[w_start:he_start].strip()
        height = line[he_start:m_start].strip()
        mass = line[m_start:b_start].strip()
        brain = line[b_start:end].strip()
    # print("debug: humans= '%s', weight= '%s', height='%s' , mass='%s' , brain='%s'" %
          #(humans, when, height, mass, brain))
        human_dict[human] = {'when': when,
                             'height': height,
                             'mass': mass,
                             'brain': brain}


infile.close()
# output
# : number of characters for each column
for human in human_dict:
    print(f"{human:20} {human_dict[human]['when']:15} {human_dict[human]['height']:11} {human_dict[human]['mass']:10} "
          f"{human_dict[human]['brain']}")
