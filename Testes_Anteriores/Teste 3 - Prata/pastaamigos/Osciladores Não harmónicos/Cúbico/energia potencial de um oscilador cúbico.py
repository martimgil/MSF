# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:39:08 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

k = 1
alpha = -0.01

x = np.linspace(-6,6,100)

Ep = 0.5*k*(x**2) + alpha*(x**3)

plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.plot(x,Ep)
plt.grid()
plt.show()

