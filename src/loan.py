# -*- coding: utf-8 -*-

__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

"""
From

Book: A Primer on Scientific Programming with Python
Author: Hans Petter Langtangen
Editition: 5th Edition
Year: 2016

Exercise A.4: Compute the development of a loan 

"""
import numpy as np
import matplotlib.pyplot as plt
import decimal


def g(N, L, p):
    """
    A function that returns the current loan and the downpayment for each
    month

    :param N: Number of months downpayment
    :param L: Initial amount of loan
    :param p: Interest rate in percent
    :return:
        y: what to pay each month
        x: the current value of the loan
    """
    y = np.zeros(N+1)
    x = np.zeros(N+1)
    x[0] = L
    for n in range(1, N+1):
        y[n] = float(p)/(12*100) * x[n-1] + float(L)/N
        x[n] = x[n-1] + float(p)/(12*100) * x[n-1] - y[n]
    return x, y

if __name__ == "__main__":
    N = 120
    x, y = g(N, 10**6, 5)
    print("Month    Payment    Loan after month")
    for i in range(N+1):
        precision = 4
        print(f"{i}       {y[i]}       {x[i]}")
    plt.figure()
    plt.plot(np.arange(0, N+1), x, 'r')
    plt.xlabel('N')
    plt.ylabel('Loan')
    plt.show()
    plt.figure()
    plt.plot(np.arange(0, N+1), y, 'r')
    plt.xlabel('N')
    plt.ylabel('Downpayment')
    plt.show()