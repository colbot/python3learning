#
import numpy as np
import matplotlib.pyplot as plt

def sigmod(x):
    return 1.0/(1.0+np.exp(-x))


def sigmod_prime(z):
    return sigmod(z)*(1.0-sigmod(z))


x = np.array([i/10 for i in range(-40, 40)])
y=sigmod(x)
z=sigmod_prime(x)

plt.plot(x, y)
plt.plot(x, z)
plt.show()
