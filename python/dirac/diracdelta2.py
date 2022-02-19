import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


def f1(x, n, a0):
    return n/np.pi*1/(1+n**2*(x - a0)**2)


n = 10
a0 = 8


def g(x):
    return x


def p1(x):
    return f1(x, n, a0)*g(x)


print(sci.quad(p1, -np.inf, np.inf))

x = np.linspace(-5+a0, 5+a0, 1000)
#y = n/np.pi*1/(1+n**2*(x - a0)**2)
plt.plot(x, f1(x, n, a0))
plt.legend(["1st"])
plt.plot(x, p1(x))
plt.legend(["2nd"])
plt.show()
