import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


def d(x, n, a0):
    return np.sin(n*(x-a0))/(np.pi*(x-a0))


n = 40
a0 = 6
e = 1


def f(x):
    return x**2


def prd(x):
    return d(x, n, a0)*f(x)


print(sci.quad(prd, a0-e, a0+e))
print(f(a0))

x = np.linspace(a0-e, a0+e, 1000)
plt.plot(x, d(x, n, a0))
plt.plot(x, prd(x))
plt.show()
