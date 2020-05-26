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

# Source HPL p 444
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
                result_coeff[i] += self.coeff
        return Polynomial(result_coeff)

class Parabola(Polynomial):
    """
    Inherit coefficients from Polynomial. Set extra coefficients to zero
    """
    def __init__(self, c0, c1, c2):
        super().__init__(coefficients=[c0, c1, c2])

    def __call__(self, x):
        """Evaluate parabola"""
        return self.coeff[0] + self.coeff[1] * x + self.coeff[2] * x**2

class Line(Parabola):
    def __init__(self, c0, c1, c2=0):
        super().__init__(c0, c1, c2)

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s



