# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 18:25:43 2023

@author: raque
"""

import numpy as np
import matplotlib.pyplot as plt

m = 0.5
k = 2
alpha = -0.1
beta = 0.02
# Initial conditions
x0 = 1.5
v0 = 0.5
# Dampened oscillator
b = 0
# Forces oscillator
F_0 = 0
omega_f = 0
# Parameters
dt = 0.001
t0 = 0
tf = 20

oscillator = lambda x: -k * x -3*(alpha*x**2) + 4*beta*x**3 # Change me
accel = lambda t, x, v:  oscillator(x)/m - (b/m)*v + (F_0/m)*np.cos(omega_f * t)

# Número de passos/iterações
#
# + 0.1 para garantir que não há arredondamentos
# para baixo
n = int((tf-t0) / dt + 0.1)

t = np.zeros(n + 1) # Tempo
x = np.zeros(n + 1) # Posição
v = np.zeros(n + 1) # Velocidade

Em = np.zeros(n + 1) #Energia Mecânica
Ep = np.zeros(n + 1) #Energia Potencial


# Valores inicias
v[0] = v0
t[0] = t0
x[0] = x0


def rk4(t,x,vx,acelera,dt):
  ax1=acelera(t,x,vx)
  c1v=ax1*dt
  c1x=vx*dt
  ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
  c2v=ax2*dt
  c2x=(vx+c1v/2.)*dt # predicto: vx(t+dt) * dt
  ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
  c3v=ax3*dt
  c3x=(vx+c2v/2.)*dt
  ax4=acelera(t+dt,x+c3x,vx+c3v)
  c4v=ax4*dt
  c4x=(vx+c3v)*dt
  xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
  vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
  return xp,vxp

for i in range(n):
  mx, vx = rk4(t[i], x[i], v[i], accel, dt)
  v[i + 1] = vx
  x[i + 1] = mx
  t[i + 1] = t[i] + dt
  Ep[i + 1] = 0.5*k*x[i]**2 + alpha*x[i]**3 - beta*x[i]**4
  Em[i + 1] = Ep[i] + 0.5*mx*v[i]**2 
  #mudar aqui na em a energia potencial para a do enunciado
  
  
#mudar isto para os valores do regime estacionário
x_temp = x[t >0]
t_temp = t[t > 0]
v_temp = v[t > 0] 

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

i_stationary = int(np.ceil(0 / dt))
A, T = measure_amplitude(t[i_stationary:], x[i_stationary:], dt)
#Prints da amplitude e período
print("Amplitude:", np.round(A, 3), "m")
print("Período:",  np.round(T, 3), "s")


#----------Gráfico Posição tempo----------#
plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Oscilador Quártico Met Runge-Kutta 4ºordem")
plt.xlim(0,20)
plt.ylim(-3,3)
plt.grid()
plt.show()

#----------Gráfico de Fase----------#
# plt.figure()
# plt.plot(x_temp, v_temp)
# plt.ylabel('v (m/s)')
# plt.xlabel('x (m)')
# plt.title('Gráfico de Fase')
# plt.grid()
# plt.show()

#----------Gráfico da Energia Mecânica---------regime estacionário
# Em[-1] = Em[-2]
# plt.plot(t, Em)
# plt.xlabel("Tempo (s)")
# plt.ylabel("Energia mecânica (J)")
# plt.title('Gráfico da Energia mecânica')
# plt.xlim(0,100)
# plt.ylim(0,22.5)
# plt.grid()
# plt.show()

#----------Gráfico da Energia Potencial---------regime estacionário
# Ep[-1] = Ep[-2]
# plt.plot(x, Ep)
# plt.xlabel("x (m)")
# plt.ylabel("Energia potencial (J)")
# plt.title('Gráfico da Energia Potencial')
# plt.xlim(-3,3)
# plt.ylim(0,10)
# plt.grid()
# plt.show()


#----------Gráfico da Energia Potencial aquela cena do space---------regime estacionário
# x_space = np.linspace(-3, 3)

# Ep = 1/2 * k * x_space**2 + alpha*x_space**3 - beta*x_space**4

# plt.plot(x_space, Ep)
# plt.xlabel("x (m)")
# plt.ylabel("Ep (J)")
# plt.title("Sistema Mola-Corpo")
# plt.grid()
# plt.show()

#----------Alguns prints----------#
# =============================================================================
# print("Posição máxima: ", max(x))
# print("Posição mínima: ", min(x))
# print("Velocidade máxima: ", max(v))
# print("Velocidade mínima: ", min(v))
# =============================================================================


#----------Coeficientes de Fourier----------#

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


afo = np.zeros(14)
bfo = np.zeros(14)
ind = np.argwhere(np.diff(np.sign(np.diff(x_temp))) == -2)

t0 = int(ind[-2])
t1 = int(ind[-1])
for i in range(14):

    af, bf = abfourier(t_temp, x_temp, t0, t1, i)
    afo[i] = af
    bfo[i] = bf
    #print('afo = ',i,af,bf,np.sqrt(af**2+bf**2))


#----------Gráfico de an----------#
# ii = np.linspace(0, 20, 14)   #(início, fim, nº de barras) os zeros e o range tem de ser igual ao ultimo argumento
# plt.figure()
# plt.ylabel('| a_n |')   
# plt.xlabel('n')
# plt.bar(ii, np.abs(afo))
# plt.title('Coeficientes de Fourier: an')
# plt.grid()
# plt.show()

#----------Gráfico de bn----------#
# ii = np.linspace(0, 20, 14)
# plt.figure()
# plt.ylabel('| b_n |')
# plt.xlabel('n')
# plt.bar(ii, np.abs(bfo))
# plt.title('Coeficientes de Fourier: bn')
# plt.grid()
# plt.show()


#----------Gráfico de "√(𝑎𝑛^2 + 𝑏𝑛^2)----------#
ii = np.linspace(0, 20, 14)
plt.figure()
plt.ylabel('| "√(an^2 + bn^2) |')
plt.xlabel('n')
plt.bar(ii, np.abs(np.sqrt( afo**2+bfo**2)))
plt.title('Coeficientes de Fourier: √(an^2 + bn^2)')
plt.grid()
plt.show()
