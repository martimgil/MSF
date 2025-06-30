import matplotlib.pyplot as plt
import numpy as np

dt = 0.1

t = np.arange(0, 20+dt,dt)
k = 1
m = 1
w = np.sqrt(k/m)
EM = np.zeros(t.size)

v = np.zeros(t.size)
x = np.zeros(t.size)

v1 = np.zeros(t.size)
x1 = np.zeros(t.size)

f = np.zeros(t.size)

x[0] = 4
v[0] = 0

x1[0] = 4
v1[0] = 0

EM[0] = 0.5*m*v1[0]**2 + 0.5*m*w**2*x[0]**2

for i in range(t.size-1):
    f[i] =  -k * x1[i]
    a = f[i]/m
    v1[i+1] = v1[i] + a*dt
    x1[i+1] = x1[i] + v1[i+1]*dt
    EP = 0.5*m*w**2*x1[i+1]**2
    EC = 0.5*m*v1[i+1]**2
    EM[i+1] = EP + EC


plt.plot(t,EM)
plt.xlabel("Tempo")
plt.ylabel("E mecanica")
plt.show()