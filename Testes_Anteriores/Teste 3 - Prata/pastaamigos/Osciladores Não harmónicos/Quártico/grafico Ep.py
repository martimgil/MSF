import numpy as np
from matplotlib import pyplot as plt

m = 0.5
xeq = 0
k = 2
alpha = -0.1
beta = 0.02
x = np.arange(-4, 4, 0.1)
Ep = 0.5*k*(x**2)+alpha*(x**3)-beta*(x**4)

plt.plot(x,Ep)
plt.grid()
plt.show()