# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:34:31 2023

@author: diogu
"""

import numpy as np

m = 1
k = 100
A = 0.1
v0 = 0
phi = 0
w = np.sqrt(k/m)

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

x = A*np.cos(w*t+phi)
Ec = 0.5*m*((-w*A*np.sin(w*t+phi))**2)
Ep = 0.5*k*((A*np.cos(w*t+phi))**2)

for i in range(n):
    if (Ep[i]-0.00001)<Ec[i]<(Ep[i]+0.00001):
        print("Ec = Ep =", Ec[i], "J")
        break

for i in range(n):
    if (Ep[i]-0.01)<Ec[i]<(Ep[i]+0.01):
        print("Instante:", t[i], "s")
        print("Posição:", x[i], "m")
        break