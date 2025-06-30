# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:14:57 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
xeq = 2
k = 1
x0 = 3
v0 = 0

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscHarmSimp_1D(x0,v0,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    Em = np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        if x[i]>0:
            a[i]=-(x[i]-xeq)
            v[i+1]=v[i]+a[i]*dt
            x[i+1]=x[i]+v[i+1]*dt
            Em[i] = 0.5*m*(v[i]**2) + 0.5*k*((abs(x[i])-xeq)**2)
        else:
            a[i]=-x[i]-xeq
            v[i+1]=v[i]+a[i]*dt
            x[i+1]=x[i]+v[i+1]*dt
            Em[i] = 0.5*m*(v[i]**2) + 0.5*k*((abs(x[i])-xeq)**2)
    Em[n] = 0.5*m*(v[n]**2) + 0.5*k*((abs(x[n])-xeq)**2)
    return x,v,a,Em

values = oscHarmSimp_1D(x0,v0,n,dt)
Em = values[3]

plt.xlabel("t (s)")
plt.ylabel("Em (J)")
plt.plot(t,Em)
plt.grid()
plt.show()

print( "Energia mecânica: 0.5 J")