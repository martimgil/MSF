import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t0 = 0
tf = 10
dt = 0.001  
v0 = 2 * np.pi  
x0 = 1.0 

G = 4 * np.pi**2  

t = np.arange(t0, tf, dt)
N = len(t)

x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)

x[0] = x0
y[0] = 0
vx[0] = 0
vy[0] = v0

for i in range(N-1):
    r = np.sqrt(x[i]**2 + y[i]**2)
    ax = -G * x[i] / r**3
    ay = -G * y[i] / r**3
    
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt


fig, ax = plt.subplots() 
plt.plot(x,y)
terra = ax.plot(x[0], y[0], 'o')[0]
sol = ax.plot(0,0, 'oy')[0]

ax.set(xlim=[-1.6, 1.4], ylim=[-1.6, 1.4])

def update(frame):
    terra.set_xdata([x[frame]])
    terra.set_ydata([y[frame]])
    return terra

ani = FuncAnimation(fig=fig, func=update, frames=N, interval=1)
plt.show()