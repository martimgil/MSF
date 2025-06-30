import numpy as np
import matplotlib.pyplot as plt

dt = 0.0001
tf=1000
n = int(tf/dt+0.1)

t= np.empty(n+1)
x = np.empty(n+1)
vx = np.empty(n+1)
a = np.empty(n+1)
Em = np.empty(n+1)

t0 = 0 
x0 = 2.000
vx0 = 0

t[0] = t0
vx[0] = vx0
x[0] = x0

k = 1 #N/m
m = 1 #kg
b = 0.02 #kg/s
F0 = 7.5 
Wf = 1 
alpha = 0.15 #N/m**2

for i in range(n):
    t[i+1] = t[i]+dt
    a[i] = (-4*alpha*x[i]**3)/m - (b/m)*vx[i] +(F0/m)*np.cos(Wf*t[i])
    vx[i+1] = vx[i]+a[i]*dt
    x[i+1] = x[i]+vx[i+1]*dt


plt.title('Oscilador Quádrico Forçado Método Euler-Cromer')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid()
plt.plot(t, x)
plt.show()