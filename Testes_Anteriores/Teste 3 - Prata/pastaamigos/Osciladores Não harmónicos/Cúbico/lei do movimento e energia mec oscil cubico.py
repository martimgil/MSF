# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:41:08 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
alpha = -0.01
k = 1
x0 = 1.3 #mudar posição inicial
v0 = 0

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscHarmSimp_1D(x0,v0,k,m,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    Em = np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=(-k*x[i] - 3*alpha*(x[i]**2))/m 
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
        
        Em[i] = 0.5*m*(v[i]**2) + 0.5*k*(x[i]**2) + alpha*(x[i]**3)
    Em[n] = 0.5*m*(v[n]**2) + 0.5*k*(x[n]**2) + alpha*(x[n]**3)
    return x,v,a,Em

def amp_per_comp(x, t, n):
    ind_max=[i for i in range(1,n-1) if x[i-1]<=x[i]>=x[i+1]]
    ind_min=[i for i in range(1,n-1) if x[i-1]>=x[i]<=x[i+1]]
    x_max=[x[i] for i in ind_max]
    x_min=[x[i] for i in ind_min]
    t_max=[t[i] for i in ind_max]
    x_max_avg =np.average(x_max)
    x_min_avg = np.average(x_min)

    T_lst=[t_max[i+1]-t_max[i] for i in range(len(t_max)-1)]
    T=np.average(T_lst)

    lmbd_lst=[x_max[i+1]-x_max[i] for i in range(len(x_max)-1)]
    lmbd=np.average(lmbd_lst)

    return x_max_avg, x_min_avg, T, lmbd

values = oscHarmSimp_1D(x0,v0,k,m,n,dt)
x = values[0]
Em = values[3]

values1 = amp_per_comp(x,t,n)
x_max = values1[0]
x_min = values1[1]
T = values1[2]
f = 1/T

print("Limites movimento: {} m a {} m".format(x_min,x_max))
print("Frequência:", f, "Hz")

#lei do movimento
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.plot(t,x)
plt.grid()
plt.show()

#energia mecânica
# =============================================================================
# plt.xlabel("t (s)")
# plt.ylabel("Em (J)")
# plt.plot(t,Em)
# plt.grid()
# plt.show()
# =============================================================================

