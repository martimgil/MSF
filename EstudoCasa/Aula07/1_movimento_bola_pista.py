import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 4.0
dt = 0.001
vx0 = 0.0
x0 = 0.0
y0 = 0.1
g = 9.80

def y_func(x: float) -> float:
    return 0.1- 0.05 * x if x<2.0 else 0.0

def dydx_func(x: float) -> float:
    return -0.05 if x<2.0 else 0.0

t = np.arange(t0, tf, dt)

ax = np.zeros(np.size(t))
vx = np.zeros(np.size(t))
vx[0] = vx0

x = np.zeros(np.size(t))
y=np.zeros(np.size(t))
x[0] = x0
y[0] = y0

for i in range(np.size(t)-1):   
    #euler-cromer
    ax[i] = -g * dydx_func(x[i])
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y_func(x[i+1])

fig, ax1_main = plt.subplots ()
color = 'tab:blue'
ax1_main.set_xlabel('time (s)')
ax1_main.set_ylabel('x', color=color)
ax1_main.plot(t[x<2.5], x[x<2.5], color=color)
ax1_main.tick_params (axis='y', labelcolor=color)

ax2_main = ax1_main.twinx()

color = 'tab:red'
ax2_main.set_ylabel('y', color=color)
ax2_main.plot(t[x<2.5], y[x<2.5], color=color)

ax2_main.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()


