# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016
Exercise 9.4: Create an alternative class hierarchy for polynomials

"""
"""
Source: https://www.uio.no/studier/emner/matnat/ifi/IN1900/h19/ressurser/
live_programmering/polynomial_hier.py
 """

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """ Evaluate a polynomial"""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        """
        Return self + other as polynomial object
        # Two cases:
        ##
        self: X X X X X X X
        # other: X X X
        ##
        or:
        ##
        self: X X X X X
        # other: X X X X X X X X
        # Start with the longest list and add in the other
        """
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]    # copy
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]    # copy
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)


    def __sub__(self, other):
        """Return self - other as Polynomial object.
               As for the add function above, we have two cases
               that must be treated separately: one where
               self.coeff is longer than other.coeff,
               one where other.coeff is longest. The difference
               from the __add__ method is that for subtraction
               the order matters, so the implementation
               must be slightly different
               """
        # start with the simplest case where self.coeff is longest
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]    # copy
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
            # Here, the polynomial we subtract is the
            # longest, which requires some extra care:
            result_coeff = [0]*len(other.coeff)
            for i in range(len(self.coeff)):
                result_coeff[i] = self.coeff[i]

            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]

            return Polynomial(result_coeff)

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
            # Fix layout
            s = s.replace('+ -', '- ')
            s = s.replace('x^0', '1')
            s = s.replace(' 1*', ' ')
            s = s.replace('x^1 ', 'x ')
            # s = s.replace('x^1', 'x') # will replace x^100 by x^00
            if s[0:3] == ' + ':  # remove initial +
                s = s[3:]
            if s[0:3] == ' - ':  # fix spaces for initial -
                s = '-' + s[3:]
            return s

"""
The exercise text asks for a different type of constructor
for classes Parabola an Line, which takes the coeffecients as
separate arguments. The classes must therefore implement their
own constructor, while the rest can be inherited from the
Polynomial base class.
"""

class Parabola(Polynomial):
    def __init__(self, c0, c1, c2):
        super().__init__(coefficients=[c0, c1, c2])


class Line(Polynomial):
    def __init__(self, c0, c1):
        super().__init__(coefficients=[c0, c1])

"""
Example usage: Parabola and Line support pretty print
and addition because of inheritance from the
Polynomial base class.
"""

p0 = Parabola(1, 2, 3)
print(p0)

l0 = Line(5, 4)
print(l0)

p1 = l0 + p0
print(p1)

"""
Comment AH: Look over soulution one more time to understand better what is
going on.
"""
