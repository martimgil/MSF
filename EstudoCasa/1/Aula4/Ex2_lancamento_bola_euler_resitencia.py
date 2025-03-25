import numpy as np
import matplotlib.pyplot as plt

g = 9.80
vT = 100*1000/3600
t0 = 0
tf = 5
v0 = 10
dt = 0.0001
y0 = 0

t = np.arange(t0,tf,dt)
y = np.empty(np.size(t))
v = np.empty(np.size(t))
a = np.empty(np.size(t))

#a) Determinar a lei do movimento sem resistencia do ar

t= np.arange(t0, tf, dt)
v = np.empty(np.size(t))
x = np.empty(np.size(t))

v[0] = v0
x[0] = y0

for i in range(np.size(t)-1):
    v[i+1]=v[i] + g*dt
    x[i+1] = x[i] + v[i]*dt

#b) Determinar a altura máxima e o instante em que ocorre


izero = np.size(y) - np.size(y[y<0]) #posicao em que volta a origem 
tzero = t[izero]
print("Tempo de retorno à orígem, tzero = ", tzero, "s")

# c) 


D = g / vT ** 2

t = np.arange(t0, tf, dt) 
y = np.empty(np.size(t)) 
v = np.empty(np.size(t)) 
a = np.empty(np.size(t)) 

y[0] = y0
v[0] = v0

for i in range(np.size(t) - 1):
    a[i] = - g - D * v[i] * np.abs(v[i])
    v[i+1] = v[i] + a[i] * dt
    y[i+1] = y[i] + v[i] * dt




izero = np.size(y) - np.size(y[y<0]) #posicao em que volta a origem 
tzero = t[izero]
print("Tempo de retorno à orígem, tzero = ", tzero, "s")
