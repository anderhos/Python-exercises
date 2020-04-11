
import numpy as np


def h(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-0.5*x**2)


n = 41
x0 = -4
stop = 4
dx = 1/(n-1)

x = np.linspace(x0, stop, n)
y = np.zeros(41)

for i in range(n):
    y[i] = h(x[i])

print(y)