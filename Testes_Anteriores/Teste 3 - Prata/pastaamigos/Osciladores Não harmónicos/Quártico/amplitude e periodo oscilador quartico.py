# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:19:33 2023

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

    t0 = 0.
    x0 = -3.0
    vx0 = 0.0

    tempo[0] = t0
    vx[0] = vx0
    x[0] = x0

    k = 1
    m = 1
    b = 0.05
    F0 = 7.5
    Wf = 1.4
    alpha = 0.001
# =============================================================================
#     ampl = 0
#     countMax = 0
#     tMax = []
#     periodo = []
# =============================================================================
    for i in range(n):
        força = -(k)*x[i]*(1+2*alpha*x[i]**2) - (b)*vx[i]+(F0)*np.cos(Wf*tempo[i])
        # Wf = 1.4
        # if tempo[i] > 400:
        #     Wf = 1.37
        tempo[i+1] = tempo[i]+dt
        a[i] = força/m
        vx[i+1] = vx[i]+a[i]*dt
        x[i+1] = x[i]+vx[i+1]*dt
        

    return a, vx, x, tempo


dt = 0.001
tf = 800
a_1, vx_1, x_1, t_1 = oscilador_quartico(dt, tf)
# dt = 0.01
# a_2, vx_2, x_2, t_2 = oscilador_quartico(dt, tf)


plt.plot(t_1, x_1, label="dt = 0.0001")
# plt.plot(t_2, x_2, label="dt = 0.01")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend()
plt.grid(True)
plt.show()


# =============================================================================
# plt.plot(t_1[:-2][np.diff(np.sign(np.diff(x_1))) == -2],
#          x_1[:-2][np.diff(np.sign(np.diff(x_1))) == -2], ".")
# plt.xlabel("Tempo (s)")
# plt.ylabel("Máximos x (m)")
# =============================================================================
#Calculo da amplitude e período
def measure_amplitude(t, x, dt):
    ft = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(len(x), dt) # Get frequency axis from the time axis
    mags = abs(ft) # We don't care about the phase information here

    inflection = np.diff(np.sign(np.diff(mags)))
    peaks = (inflection < 0).nonzero()[0] + 1
    peak = peaks[mags[peaks].argmax()]
    signal_freq = freqs[peak]
    T = 1/signal_freq
    
    window = int(np.ceil(T / dt))
    max = x[-window:].max()
    min = x[-window:].min()
    A = (max - min)/2

    return A, T

i_stationary = int(np.ceil(750 / dt)) #Mudar conforme o regime
A, T = measure_amplitude(t_1[i_stationary:], x_1[i_stationary:], dt)
#Prints da amplitude e período
print("Amplitude:", np.round(A, 3), "m")
print("Período:",  np.round(T, 3), "s")
