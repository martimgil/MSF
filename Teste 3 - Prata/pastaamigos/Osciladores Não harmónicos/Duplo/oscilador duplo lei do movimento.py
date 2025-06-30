# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:16:33 2023

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
    x[0]=x0
    v[0]=v0
    for i in range(n):
        if x[i]>0:
            a[i]=-(x[i]-xeq)
            v[i+1]=v[i]+a[i]*dt
            x[i+1]=x[i]+v[i+1]*dt
        else:
            a[i]=-x[i]-xeq
            v[i+1]=v[i]+a[i]*dt
            x[i+1]=x[i]+v[i+1]*dt
    return x,v,a

def amp_per_comp(x, t, n):
    ind_max=[i for i in range(1,n-1) if x[i-1]<=x[i]>=x[i+1]]
    x_max=[x[i] for i in ind_max]
    t_max=[t[i] for i in ind_max]
    A=np.average(x_max)

    T_lst=[t_max[i+1]-t_max[i] for i in range(len(t_max)-1)]
    T=np.average(T_lst)

    lmbd_lst=[x_max[i+1]-x_max[i] for i in range(len(x_max)-1)]
    lmbd=np.average(lmbd_lst)

    return A, T, lmbd

values = oscHarmSimp_1D(x0,v0,n,dt)
x = values[0]

values1 = amp_per_comp(x,t,n)
T = values1[1]

print("Período:", T, "s")

plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.plot(t,x)
plt.grid()
plt.show()