# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:44:09 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 2
A = 0.1
v0 = 0
phi = 0
w = np.sqrt(k/m)
b = 2

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

x = A*np.exp(-b/(2*m)*t)*np.cos(w*t+phi)
v = A*((-b/(2*m))*np.exp(-b/(2*m)*t) + np.exp(-b/(2*m)*t)*(-w*np.sin(w*t+phi)))
Ec = 0.5*m*(v**2)
Ep = 0.5*k*(x**2)
Em = Ec + Ep

Em0 = Em[0]

for i in range(n):
    if (1-dt)<t[i]<(1+dt):
        Em1 = Em[i]

vEm = Em1-Em0
print("Energia mecânica inicial:", round(Em0,5), "J")
print("Energia mecânica final:", round(Em1,5), "J")
print("Variação da energia mecânica:", vEm, "J")