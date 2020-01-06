# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From 

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Ex 3.23: Wrap a formula in a function
"""

from math import *
"""
M_s = 47    # mass of small egg measured in grams
M_l = 67    # mass of large egg measured in grams
p = 1.038   # density measured in g cm^(-3)
c = 3.7 * K**(-1)   # joules per g^(-1) multiplied by..
K = 5.4 * 10**(-3) * K**(-1)    # watt per cm^(-1) times ..
Tw = 100    # Degrees
Ty = 70    # Degrees
T0 = 4    # Degrees
"""


def egg(M, T0=20, Ty=70):
    p = 1.038    # density measured in g cm^(-3)
    K = 5.4 * 10 ** (-3) #* K ** (-1)  # watt per cm^(-1) times ..
    c = 3.7 #* K ** (-1)  # joules per g^(-1) multiplied by..
    Tw = 100  # Degrees

    t = (M**(2/3) * c * p**(1/3))/(K * pi**2 * (4 * pi / 3)**(2/3)) * \
        log(0.76 * (T0 - Tw)/(Ty - Tw))
    return t

if __name__ == "__main__":
    print("The perfect cooking time for a soft boiled small egg with "
          "temperature %g celsius is %g seconds." %(4, egg(47, 4, 63)))
    print(egg(47, 4, 70))    # Hard, small from fridge
    print(egg(67, 4, 63))    # Soft, large from fridge
    print(egg(67, 4, 70))    # Hard, large from fridge
    print(egg(67, 25, 70))    # Hard, large from warm room
    print(egg(47, 25, 63))    # Soft, small from warm room
