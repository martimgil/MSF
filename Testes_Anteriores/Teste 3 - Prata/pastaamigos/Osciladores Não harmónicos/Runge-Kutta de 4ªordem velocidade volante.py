# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:56:43 2023

@author: diogu
"""

import numpy as np
import matplotlib.pyplot as plt


def acelera(t, x, vx):
    ax = g-g/vt**2*np.abs(vx)*vx
    return ax


def rk4(t, x, vx, dt):
    # Modificado
    ax1 = acelera(t, x, vx)
    c1v = ax1*dt
    c1x = vx*dt
    ax2 = acelera(t+dt/2., x+c1x/2., vx+c1v/2.)
    c2v = ax2*dt
    c2x = (vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3 = acelera(t+dt/2., x+c2x/2., vx+c2v/2.)
    c3v = ax3*dt
    c3x = (vx+c2v/2.)*dt
    ax4 = acelera(t+dt, x+c3x, vx+c3v)
    c4v = ax4*dt
    c4x = (vx+c3v)*dt
    xp = x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp = vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp, vxp


dt = 0.5
tf = 2.0
n = int(tf/dt)

g = 9.80
vt = 6.80

t0 = 0
x0 = 0
vx0 = 0

t = np.zeros(n+1)
xrk4 = np.zeros(n+1)
vxrk4 = np.zeros(n+1)  # rk4
vxe = np.zeros(n+1)  # euler

t[0] = t0
vxrk4[0] = vx0
xrk4[0] = x0
tem = t0
xet = x0
vxet = vx0

for i in range(n):
    xet, vxet = rk4(tem, xet, vxet, dt)
    tem = tem+dt
    t[i+1] = tem
    vxrk4[i+1] = vxet
    xrk4[i+1] = xet
    vxe[i+1] = vxe[i]+(g-g/vt**2*np.abs(vxe[i])*vxe[i])*dt  # Euler

te = np.linspace(t0, tf, 100)
ve = vt*np.tanh(g*te/vt)
tet = 2
vet = vt*np.tanh(g*tet/vt)
print('t=', tet, 's')
print('v=', vet, 'm/s')

plt.grid()
plt.plot(t, vxrk4, label="Runge-Kutta")
plt.plot(te, ve, label="Teórico")
plt.plot(t, vxe, label="Euler")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade(m/s)")
plt.legend()
plt.show()
