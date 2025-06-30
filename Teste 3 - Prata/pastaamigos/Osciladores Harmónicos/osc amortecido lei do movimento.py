# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:47:17 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
b = 0.16
x0 = 2 #posição inicial 
v0 = 3 #velocidade inicial

ti = 0
tf = 50
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscSimpFA_1D(x0,v0,k,m,b,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=-k/m*x[i]+(-b*v[i])/m
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
    return x,v,a

values = oscSimpFA_1D(x0,v0,k,m,b,n,dt)
x = values[0]

A = 3.74
phi = 1.01 #frequência angular
x_analitico = A*np.exp(-b/(2*m)*t)*np.cos(t-1) 

plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.plot(t,x,label="Euler-Cromer")
plt.plot(t,x_analitico,label="Analítico")
plt.legend()
plt.grid()
plt.show()