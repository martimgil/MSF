# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:11:53 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt


def oscilador_quartico(dt, tf):
    n = int(tf/dt+0.1)
    print('n', n)
    tempo = np.empty(n+1)
    x = np.empty(n+1)
    vx = np.empty(n+1)
    a = np.empty(n+1)
    Em = np.empty(n+1)

    t0 = 0 #Mudar
    x0 = 3 #Mudar
    vx0 = 0.0 #Mudar

    tempo[0] = t0
    vx[0] = vx0
    x[0] = x0

    k = 1 #Mudar
    m = 1 #Mudar
    b = 0.05 #Mudar
    F0 = 7.5 #Mudar
    Wf = 1 #Mudar
    alpha = 1 #Mudar
    #ampl = 0
    #countMax = 0
    #tMax = []
    #periodo = []
    for i in range(n):
        tempo[i+1] = tempo[i]+dt
        a[i] = -(k/m)*x[i]*(1+2*alpha*x[i]**2) - \
            (b/m)*vx[i]+(F0/m)*np.cos(Wf*tempo[i])
        vx[i+1] = vx[i]+a[i]*dt
        x[i+1] = x[i]+vx[i+1]*dt

    return a, vx, x, tempo


dt = 0.0001
tf = 760 # Este tempo adiciona ao tempo inicial tf = tf + t0
a_1, vx_1, x_1, t_1 = oscilador_quartico(dt, tf)
dt = 0.01
a_2, vx_2, x_2, t_2 = oscilador_quartico(dt, tf)


plt.title('Oscilador Quádrico Forçado Met Euler-Cromer')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid()
plt.plot(t_1, x_1)
plt.plot(t_2, x_2)
plt.show()

x_temp = x_1[t_1 > 660]
t_temp = t_1[t_1 > 660]
maximos_x = x_temp[:-2][np.diff(np.sign(np.diff(x_temp))) == -2]
maximos_t = t_temp[:-2][np.diff(np.sign(np.diff(x_temp))) == -2]
print("Amplitude:", np.round(np.mean(maximos_x), 3), "m")
print("Período:",  np.round(np.mean(np.diff(maximos_t)), 3), "s")


