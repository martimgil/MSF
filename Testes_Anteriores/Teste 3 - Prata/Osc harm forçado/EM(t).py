import matplotlib.pyplot as plt
import numpy as np

#Movimento oscilatório harmónico forçado

dt = 0.001 
t = np.arange(0, 1200+dt,dt)
g = 9.8
m = 1

x = np.zeros(t.size)
v = np.zeros(t.size)
EM = np.zeros(t.size)
Vforca = 1
F0 = 7.5
b = 0.05
k = 1
w = np.sqrt(k/m)

v[0] = -4
x[0] = -2


EM[0] = 0.5*m*v[0]**2 + 0.5*m*w**2*x[0]**2

for i in range(t.size-1):
    a = (-k*x[i]-b*v[i]+F0*np.cos(Vforca*t[i]))/m

    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    EP = 0.5*m*w**2*x[i+1]**2
    EC = 0.5*m*v[i+1]**2
    EM[i+1] = EP + EC

    
plt.plot(t,EM)
plt.ylabel("En Mecanica")
plt.xlabel("t(s)")
print(EM[-1])
plt.show()