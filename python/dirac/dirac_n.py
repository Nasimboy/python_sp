import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


def d(x, n, a0):
    return n/np.pi*1/(1+n**2*(x - a0)**2)


a0 = 6


def f(x):
    return x**2


def prd(x):
    return d(x, n, a0)*f(x)


for i in range(1, 1000):
    n = i
    id, e = sci.quad(prd, -np.inf, np.inf)
    print("The value of n = ", n)
    print("Integrated value", id)
    print("Actual  value   ", f(a0))
    print("Diff         ", abs(id-f(a0)))

    if(abs(id-f(a0)) < .0029):
        print("n found", n)
        break
    else:
        print("not found", n)
    print("---------------------------------------------------------------------------------")

   # print(id,n)


x = np.linspace(-5+a0, 5+a0, 1000)
y = n/np.sqrt(np.pi)*np.exp(-n**2*(x - a0)**2)
plt.plot(x, y)
plt.plot(x, prd(x))
plt.show()
