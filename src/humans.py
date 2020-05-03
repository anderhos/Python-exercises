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
# Skip first three lines
for line in range(3):
    infile.readline()

hu_start = 0
w_start = 21
he_start = 37
m_start = 50
b_start = 62
end = 88
extra = 89

list_human = []
for line in infile:
    humans = line[hu_start:w_start].strip()
    when = line[w_start:he_start].strip()
    height = line[he_start:m_start].strip()
    mass = line[m_start:b_start].strip()
    brain = line[b_start:end].strip()
    #print("debug: humans= '%s', weight= '%s', height='%s' , mass='%s' , brain='%s'" %
          #(humans, when, height, mass, brain))
    list_human.append((humans, when, height, mass, brain))
    del(list_human[7:])

infile.close()

human_dict = {}

for human in list_human:
    human_dict[human[0]] = {'when': human[1],
                            'height': human[2],
                            'mass': human[3],
                            'brain': human[4]}

print(human_dict)

# printe kolonne 22 osv

for i in list_human:
    print(i[0], i[1], i[2], i[3], i[4])


#print(list_human[0][0], list_human[0][1], list_human[0][2], list_human[0][3])