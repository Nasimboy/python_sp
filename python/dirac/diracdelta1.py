import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


def f1(x, n, a0):
    return n/np.sqrt(np.pi)*np.exp(-n**2*(x - a0)**2)


n = 10
a0 = 6


def g(x):
    return x


def p1(x):
    return f1(x, n, a0)*g(x)


print(sci.quad(p1, -np.inf, np.inf))

x = np.linspace(-5+a0, 5+a0, 1000)
y = n/np.sqrt(np.pi)*np.exp(-n**2*(x - a0)**2)
plt.plot(x, y)
plt.legend(["1st"])
plt.plot(x, p1(x))
plt.legend(["2nd"])
plt.show()

#########################################################


def d(x, n, a0):
    return n/np.sqrt(np.pi)*np.exp(-n**2*(x - a0)**2)


n = 110
a0 = 6
e = 5


def f(x):
    return x


def prd(x):
    return d(x, n, a0)*f(x)


print(sci.quad(prd, a0-e, a0+e))
print(f(a0))

#x = np.linspace(a0-e, a0+e, 1000)
#plt.plot(x, f(x))
#plt.plot(x, prd(x))
# plt.show()
