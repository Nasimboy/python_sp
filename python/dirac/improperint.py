import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt

# Evaluate the following integral


# qn (i)
i = lambda x : np.log(x)
I = sci.quad(i, 0, 1)
print("i. ",I)

x = np.linspace(0,10,1000)
y = np.log(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("np.log(x)")
plt.legend()
plt.show()

# qn (ii)
ii = lambda x : 1/(np.sqrt(4-x))
I = sci.quad(ii, 0, 4)
print("ii. ",I)

x = np.linspace(0,10,1000)
y = 1/(np.sqrt(4-x))
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("1/(np.sqrt(4-x))")
plt.legend()
plt.show()


# qn(iii)
iii = lambda x : 1/x**3
I = sci.quad(iii,0,np.inf)
print("iii. ",I)

x = np.linspace(0,10,1000)
y = 1/x**3
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("1/x**3")
plt.legend()
plt.show()


# qn(iv)
iv = lambda x : (np.cos(x))**2/x**2
I = sci.quad(iv,2,np.inf)
print("iv. ",I)

x = np.linspace(0,10,1000)
y = (np.cos(x))**2/x**2
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("(np.cos(x))**2/x**2")
plt.legend()
plt.show()


# qn(v)
v = lambda x : np.sin(x)**2/(x*(np.sqrt(x)+1))
I = sci.quad(v,1,np.inf)
print("v. ",I)

x = np.linspace(0,10,1000)
y = np.sin(x)**2/(x*(np.sqrt(x)+1))
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("np.sin(x)**2/(x*(np.sqrt(x)+1))")
plt.legend()
plt.show()


# qn(vi)
vi = lambda x : np.exp(-x)*x**(4-1)
I = sci.quad(vi,0,np.inf)
print("vi. ",I)

x = np.linspace(0,10,1000)
y = np.exp(-x)*x**(4-1)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("np.exp(-x)*x**(n-1)")
plt.legend()
plt.show()

# qn(vii)
vii = lambda x : np.exp(x)
I = sci.quad(vii,-np.inf,0)
print("vii. ",I)

x = np.linspace(0,10,1000)
y = np.exp(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("np.exp(x))")
plt.legend()
plt.show()

# qn(viii)
viii = lambda x : np.log(x)/x**2
I = sci.quad(viii,1,np.inf)
print("viii. ",I)

x = np.linspace(0,10,1000)
y = np.log(x)/x**2
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("np.log(x)/x**2")
plt.legend()
plt.show()

# qn(ix)
ix = lambda x : 1/np.sqrt(x)
I = sci.quad(ix,0,1)
print("ix. ",I)

x = np.linspace(0,10,1000)
y = 1/np.sqrt(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("1/np.sqrt(x)")
plt.legend()
plt.show()
















