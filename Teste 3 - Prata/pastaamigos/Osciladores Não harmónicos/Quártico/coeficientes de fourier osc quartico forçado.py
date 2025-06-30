# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:22:27 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt


def oscilador_quartico(dt, tf):
    n = int(tf/dt+0.1)
    tempo = np.empty(n+1)
    x = np.empty(n+1)
    vx = np.empty(n+1)
    a = np.empty(n+1)
    Em = np.empty(n+1)

    t0 = 0
    x0 = 3.0
    vx0 = 0.0

    tempo[0] = t0
    vx[0] = vx0
    x[0] = x0

    k = 1
    m = 1
    b = 0.05
    F0 = 7.5
    Wf = 1
    alpha = 0.002
    ampl = 0
    countMax = 0
    tMax = []
    periodo = []
    for i in range(n):
        tempo[i+1] = tempo[i]+dt
        a[i] = -(k/m)*x[i]*(1+2*alpha*x[i]**2) - \
            (b/m)*vx[i]+(F0/m)*np.cos(Wf*tempo[i])
        vx[i+1] = vx[i]+a[i]*dt
        x[i+1] = x[i]+vx[i+1]*dt

    return a, vx, x, tempo


dt = 0.0001
tf = 200
a_1, vx_1, x_1, t_1 = oscilador_quartico(dt, tf)
dt = 0.01
a_2, vx_2, x_2, t_2 = oscilador_quartico(dt, tf)


def abfourier(tp, xp, it0, it1, nf):
    dt = tp[1]-tp[0]
    per = tp[it1]-tp[it0]
    ome = 2*np.pi/per

    s1 = xp[it0]*np.cos(nf*ome*tp[it0])
    s2 = xp[it1]*np.cos(nf*ome*tp[it1])
    st = xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma = np.sum(st)

    q1 = xp[it0]*np.sin(nf*ome*tp[it0])
    q2 = xp[it1]*np.sin(nf*ome*tp[it1])
    qt = xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq = np.sum(qt)

    intega = ((s1+s2)/2+soma)*dt
    af = 2/per*intega
    integq = ((q1+q2)/2+somq)*dt
    bf = 2/per*integq
    return af, bf


x_temp = x_1[t_1 > 100]
t_temp = t_1[t_1 > 100]
# ind=np.transpose([0 for i in range(1000)

afo = np.zeros(15)
bfo = np.zeros(15)
ind = np.argwhere(np.diff(np.sign(np.diff(x_temp))) == -2)

t0 = int(ind[-2])
t1 = int(ind[-1])
for i in range(15):

    af, bf = abfourier(t_temp, x_temp, t0, t1, i)
    afo[i] = af
    bfo[i] = bf
    #print('afo = ',i,af,bf,np.sqrt(af**2+bf**2))


#comentar e descomentar para an e bn
ii = np.linspace(0, 14, 15)
plt.figure()
plt.ylabel('| a_n |')
plt.xlabel('n')
plt.bar(ii, np.abs(afo))
plt.grid()
plt.show()


ii = np.linspace(0, 14, 15)
plt.figure()
plt.ylabel('| b_n |')
plt.xlabel('n')
plt.bar(ii, np.abs(bfo))
plt.grid()
plt.show()
