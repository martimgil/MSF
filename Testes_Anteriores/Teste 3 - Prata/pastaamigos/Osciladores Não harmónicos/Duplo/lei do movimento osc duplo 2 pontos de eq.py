# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:33:06 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
xeq = 1.5
Em = 0.75 #energia total podes mudar aqui
v0 = 0
k = 1
x0 = np.sqrt(np.sqrt(2*Em/k)+(xeq**2))

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscHarmSimp_1D(x0,v0,k,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=-2*k*((x[i]**2)-(xeq**2))*x[i]
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
    return x,v,a

def amp_per_comp(x, t, n):
    ind_max=[i for i in range(1,n-1) if x[i-1]<=x[i]>=x[i+1]]
    ind_min=[i for i in range(1,n-1) if x[i-1]>=x[i]<=x[i+1]]
    x_max=[x[i] for i in ind_max]
    x_min=[x[i] for i in ind_min]
    t_max=[t[i] for i in ind_max]
    x_max1=np.average(x_max)
    x_min1=np.average(x_min)

    T_lst=[t_max[i+1]-t_max[i] for i in range(len(t_max)-1)]
    T=np.average(T_lst)

    lmbd_lst=[x_max[i+1]-x_max[i] for i in range(len(x_max)-1)]
    lmbd=np.average(lmbd_lst)

    return x_max1, x_min1, T, lmbd

values = oscHarmSimp_1D(x0,v0,k,n,dt)
x = values[0]

values1 = amp_per_comp(x,t,n)
x_max = values1[0]
x_min = values1[1]
T = values1[2]
f = 1/T

print("Movimento entre {} m e {} m".format(x_min,x_max))
print("Frequência:", f, "Hz")

plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.plot(t,x)
plt.grid()
plt.show()