import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


"""
Faça uma simulação do movimento da bola usando o método de Euler-Cromer com as 
seguintes condições inicias:
𝑥0 =0
𝑣𝑥,0 =0
simule o movimento até 𝑥 =2.5 m 
"""

t0 = 0.0
tf = 4.0
dt = 0.001
vx0 = 0.0
x0 = 0.0
y0 = 0.1
g = 9.80


#Trajetoria y(x)
def y_func(x: float) -> float:
    return 0.025*(x-2)**2 if x<2.0 else 0.0

#Derivada y(x)
def dydx_func(x: float) -> float:
    return 0.05*(x-2) if x<2.0 else 0.0

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


"""Quanto tempo demora para a bola demorá a atingir x=2.5m="""


x2 = x
y2 = y
vx2 = vx
i25 = np.size(x[x <= 2.5])
v25 = vx[i25]
t25 = t[i25]
print("Quando x = 2.5 m, a velocidade é v = {0:.5f} m/s2".format(v25))
print("Quando x = 2.5 m, o tempo decorrido é t = {0:.5f} s".format(t25))


"""Gráfico da velocidade"""

plt.plot(y2, vx2, 'r-')   
plt.xlabel('y (m)')
plt.ylabel('vx (m/s)')
plt.show()

""" Podemos comparar os resultados com os obtidos atraves da conservação da energia. 
Calcule a energia potencial inicial e a energia cinetica final. Qual é a velocidade final? Concorda com o resultado obtido na simulação?
"""

v=np.sqrt(2*g*0.1)
print("A velocidade final é {0:.5f} m/s2".format(v))

"""Animação do movimento da bola para cada forma de pista. Qual delas é que a bola atinge x=2m primeiro"""

fig = plt.figure()
ax = plt.axes(xlim = (-0.1, 2.6), ylim = (-0.05,0.15))
bola = ax.plot([], [], 'ro')[0]

def update(frame):
    bola.set_xdata([x2[frame]])
    bola.set_ydata([y2[frame]])

    return bola

nframes = 100
total_frames = np.size(t)
iframe = np.arange(0, total_frames, total_frames//nframes)
ani = FuncAnimation(fig=fig, func=update, frames=iframe, interval=10)
plt.show()