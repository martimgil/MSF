import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 5.0
dt = 0.001
t = np.arange(t0, tf, dt)
Nt = np.size(t)

N = 2
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
x_arr[0, 0] = - 5 * d
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



