import numpy as np
import matplotlib.pyplot as plt
import math

dt = 0.001

t = np.arange(0, 100+dt,dt)

#Constantes
k = 1
m = 1
alpha = 0.05
w = math.sqrt(k/m)

v = np.zeros(t.size)
x = np.zeros(t.size)
f = np.zeros(t.size)
a = np.zeros(t.size)
Em = np.zeros(t.size)

x[0] = 2.2  #posicao inicial
v[0] = 0    #velocidade inicial

for i in range(t.size-1):
    f[i] =  -k*x[i] - 3*alpha*(x[i]**2)
    a[i] = f[i]/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt
    Em[i] = 0.5*m*(v[i]**2) + 0.5*k*(x[i]**2) + alpha*(x[i]**3)
    
Em[t.size-1] = 0.5*m*(v[t.size-1]**2) + 0.5*k*(x[t.size-1]**2) + alpha*(x[t.size-1]**3)

    
#Lei do movimento
plt.plot(t,x)
plt.xlabel("tempo")
plt.ylabel("x(m)")
plt.legend(["x(t)"])
plt.grid()
plt.show()


#Energia Mecânica
plt.xlabel("t (s)")
plt.ylabel("Em (J)")
plt.legend(["Em(t)"])
plt.plot(t,Em)
plt.grid()
plt.show()