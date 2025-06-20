import numpy as np
import matplotlib.pyplot as plt

m=1.0
xeq = 0.0
x0  = -3
k=1.0
b = 0.05

#a)Calcule a amplitude do movimento no regime estacionario

t_start = 0
t_end = 600
dt = 0.0001
t = np.arange(t_start, t_end, dt)

x_a = np.zeros_like(t)
v_a = np.zeros_like(t)
x_a[0] = x0
v_a[0] = 0.0

omega = 1.4  # rad/s
F0 = 7.5  # N

for i in range(1, len(t)):
    F_ext = F0 * np.cos(omega * t[i-1])
    a = (-k * x_a[i-1] - b * v_a[i-1] + F_ext) / m
    v_a[i] = v_a[i-1] + a * dt
    x_a[i] = x_a[i-1] + v_a[i-1] * dt


#Analisar apenas o regime estacionário (últimos 20 segundos)

t_estacionario = t[-int(20/dt):]
x_estacionario = x_a[-int(20/dt):]

maximos=  []

for i in range(1, len(x_estacionario) - 1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])

amplitude = np.mean(maximos)
print(f"Amplitude no regime estacionário: {amplitude:.4f} m")

#b)  Calcular a ampltude da oscilação no regime estacionário
beta = 0.001

t_start = 0
t_end = 600
dt = 0.0001
t = np.arange(t_start, t_end, dt)

x_a = np.zeros_like(t)
v_a = np.zeros_like(t)
x_a[0] = x0
v_a[0] = 0.0

omega = 1.4  # rad/s
F0 = 7.5  # N

for i in range(1, len(t)):
    F_ext = F0 * np.cos(omega * t[i-1])
    a = (-k * x_a[i-1]*(1+2*beta * x_a[i-1]**2) - b * v_a[i-1] + F_ext) / m
    v_a[i] = v_a[i-1] + a * dt
    x_a[i] = x_a[i-1] + v_a[i-1] * dt


#Analisar apenas o regime estacionário (últimos 20 segundos)

t_estacionario = t[-int(20/dt):]
x_estacionario = x_a[-int(20/dt):]

maximos=  []

for i in range(1, len(x_estacionario) - 1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])

amplitude = np.mean(maximos)
print(f"Amplitude no regime estacionário: {amplitude:.4f} m")

#c) Alteracao da frequencia da força externa

beta = 0.001

t_start = 400
t_end = 800
dt = 0.01
t = np.arange(t_start, t_end, dt)

x_a = np.zeros_like(t)
v_a = np.zeros_like(t)
x_a[0] = x0
v_a[0] = 0.0

omega = 1.37  # rad/s
F0 = 7.5  # N

for i in range(1, len(t)):
    F_ext = F0 * np.cos(omega * t[i-1])
    a = (-k * x_a[i-1]*(1+2*beta * x_a[i-1]**2) - b * v_a[i-1] + F_ext) / m
    v_a[i] = v_a[i-1] + a * dt
    x_a[i] = x_a[i-1] + v_a[i-1] * dt


#Analisar apenas o regime estacionário (últimos 20 segundos)

t_estacionario = t[-int(20/dt):]
x_estacionario = x_a[-int(20/dt):]

maximos=  []

for i in range(1, len(x_estacionario) - 1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])

amplitude = np.mean(maximos)
print(f"Amplitude no regime estacionário: {amplitude:.4f} m")