import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

t0 = 0.0
tf = 5.0
dt = 0.001
t = np.arange(t0, tf, dt)
Nt = np.size(t)

N = 5
d = 0.1
l = 10 * d
m = 0.3
g = 9.8
k = 1e7
x0 = np.arange(0, N, 1) * d

x_arr = np.zeros((N, Nt))
v_arr = np.zeros((N, Nt))
a_arr = np.zeros((N, Nt))

x_arr[:, 0] = x0
x_arr[0, 0] = - 5 * d # posiçao inicial da primeira bola, repetir caso queira levantar mais bolas
x_arr[1, 0] = - 4 * d
v_arr[:, 0] = np.zeros(N)

def acc_toque(dx):
    if dx < d:
        a = k * abs(dx - d)**2 / m
    else:
        a = 0.0
    return a

def acc_i(i, x):
    a = 0
    if i > 0:
        a += acc_toque(x[i] - x[i - 1])
    if i < (N - 1):
        a -= acc_toque(x[i + 1] - x[i])
    a -= g * (x[i] - d * i) / l
    return a

for j in range(np.size(t) - 1):
    for i in range(0, N):
        a_arr[i, j] = acc_i(i, x_arr[:, j])
    v_arr[:, j + 1] = v_arr[:, j] + a_arr[:, j] * dt
    x_arr[:, j + 1] = x_arr[:, j] + v_arr[:, j + 1] * dt

for i in range(0, N):
    plt.plot(t, x_arr[i, :])

plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Posição, x [m]")
plt.show()

# Calculo do momento linear
p_arr = m * v_arr
p_tot = p_arr[0, :] + p_arr[1, :]
# Representação grafica do momento
plt.plot(t, p_arr[0, :], 'b-', t, p_arr[1, :], 'r-', t, p_tot, 'k-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Posição, x [m]")
plt.show()

E_c = p_tot**2 / (2 * m)
E_p = m * g * (x_arr[0, :] - x0[0])**2 / (2 * l)
E_p += m * g * (x_arr[1, :] - x0[1])**2 / (2 * l)
plt.plot(t, E_c, 'b-', t, E_p, 'r-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Energia [J]")
plt.show()


# Sort the wires to ensure they are in the correct order
sorted_indices = np.argsort(x0)  # Sort based on initial positions
x_arr = x_arr[sorted_indices, :]
v_arr = v_arr[sorted_indices, :]
a_arr = a_arr[sorted_indices, :]
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusted figure size to fit the whole animation

lines = [ax.plot([], [], 'o', markersize=25)[0] for _ in range(N)]  # Increased markersize for larger balls
wires = [ax.plot([], [], 'k-')[0] for _ in range(N)]  # Added wires as black lines

ax.set_xlim(-8 * d, 12 * d)
ax.set_ylim(-2 * d, (N + 1) * d)  # Adjusted y-limits to better fit the pendulum
ax.set_xlabel("Posição, x [m]")
ax.set_ylabel("Posição, y [m]")

def init():
    for line in lines:
        line.set_data([], [])
    for wire in wires:
        wire.set_data([], [])
    return lines + wires

def update(frame):
    x_positions = x_arr[:, frame]
    y_positions = np.zeros(N)  # All balls are at the same vertical level (y=0)
    for i, (line, wire) in enumerate(zip(lines, wires)):
        line.set_data([x_positions[i]], [y_positions[i]])
        wire.set_data([(N - i) * d, x_positions[i]], [1, y_positions[i]])  # Wire from above to the ball
    return lines + wires

ani = FuncAnimation(fig, update, frames=Nt, init_func=init, blit=True, interval=0.1)  # Increased speed by reducing interval
plt.show()