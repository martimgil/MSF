# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:32:40 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
xeq = 1.5
k = 1

x = np.linspace(-3,3,100)

Ep = 0.5*k*(((x**2)-(xeq)**2)**2)

plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.plot(x,Ep)
plt.grid()
plt.show()