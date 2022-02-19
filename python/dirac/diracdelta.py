import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


###########################################################

# qn(1)

def d(x, n, a0):
    return n/np.sqrt(np.pi)*np.exp(-n**2*(x - a0)**2)  # 1st Limiting Condition


n = 50
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

########################################################

# qn(2)


def d(x, n, a0):
    return n/np.pi*1/(1+n**2*(x - a0)**2)  # 2nd Limiting Condition


n = 50
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

###########################################################

# qn(3)


def d(x, n, a0):
    return np.sin(n*(x-a0))/(np.pi*(x-a0))  # 3rd Limiting Condition


n = 50
a0 = 6
e = .9


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
