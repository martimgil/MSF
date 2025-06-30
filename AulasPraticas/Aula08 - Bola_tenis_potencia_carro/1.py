import numpy as np
import matplotlib.pyplot as plt

# Condições iniciais
r0 = np.array([0, 2, 3])  # posição inicial (m)
v0 = np.array([160, 20, -20]) * 1000 / 3600  # velocidade inicial (m/s)

# Parâmetros de tempo
t0 = 0
tf = 0.4
dt = 0.001

# Constantes físicas
m = 0.057  # kg
g = 9.80   # m/s^2
vt = 120 * 1000 / 3600  # velocidade terminal em m/s

# Coeficiente de resistência do ar (modelo quadrático)
D = g / (vt ** 2)

# Vetores para armazenar o movimento
n = int((tf - t0) / dt + 0.1)
t = np.zeros(n + 1)

vx = np.zeros(n + 1)
vy = np.zeros(n + 1)
vz = np.zeros(n + 1)

rx = np.zeros(n + 1)
ry = np.zeros(n + 1)
rz = np.zeros(n + 1)

# Condições iniciais
rx[0], ry[0], rz[0] = r0
vx[0], vy[0], vz[0] = v0

# Método de Euler
for i in range(n):
    v = np.sqrt(vx[i]**2 + vy[i]**2 + vz[i]**2)

    ax = -D * v * vx[i]
    ay = -D * v * vy[i]
    az = -g - D * v * vz[i]

    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    vz[i+1] = vz[i] + az * dt

    rx[i+1] = rx[i] + vx[i] * dt
    ry[i+1] = ry[i] + vy[i] * dt
    rz[i+1] = rz[i] + vz[i] * dt

    t[i+1] = t[i] + dt

    if rz[i+1] <= 0:
        rz[i+1] = 0
        n = i + 1
        break

# Gráfico 3D da trajetória
plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.plot3D(rx[:n+1], ry[:n+1], rz[:n+1], 'g', label='Trajetória')

# Rede
rede_x = [11.9, 11.9, 11.9, 11.9]
rede_y = [0, 0, 8.2, 8.2]
rede_z = [0, 0.9, 0.9, 0]
ax.plot3D(rede_x, rede_y, rede_z, 'r')

# Campo
campo1_x = [0, 23.8, 23.8, 0, 0]
campo1_y = [0, 0, 8.2, 8.2, 0]
campo1_z = [0, 0, 0, 0, 0]
ax.plot3D(campo1_x, campo1_y, campo1_z, 'b')

# Linha central
linha_x = [0, 23.8]
linha_y = [4.1, 4.1]
linha_z = [0, 0]
ax.plot3D(linha_x, linha_y, linha_z, 'k')

ax.scatter(rx[0], ry[0], rz[0], c='g', s=100, label='Início')
ax.scatter(rx[n], ry[n], rz[n], c='r', s=100, label='Fim')

ax.set_xlim3d(0, 25)
ax.set_ylim3d(0, 10)
ax.set_zlim3d(0, 5)
ax.set_box_aspect((14, 10, 3))
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
ax.legend()
plt.show()

print(f"A bola atinge o solo no ponto (x, y, z) = ({rx[n]:.2f}, {ry[n]:.2f}, {rz[n]:.2f})")

#### EXERCIO 2 ####

# Cálculo das energias
Ep = m * g * rz[:n+1]
v_total = np.sqrt(vx[:n+1]**2 + vy[:n+1]**2 + vz[:n+1]**2)
Ec = 0.5 * m * v_total**2
Em = Ec + Ep

# Gráficos das energias
plt.plot(t[:n+1], Ep, label="Energia Potencial")
plt.plot(t[:n+1], Ec, label="Energia Cinética")
plt.plot(t[:n+1], Em, label="Energia Mecânica")
plt.legend(loc="center right")
plt.title("Energias da Bola")
plt.xlabel("Tempo (s)")
plt.ylabel("Energia (J)")
plt.show()

print(f"Variação da energia mecânica (Em final - inicial): {Em[-1] - Em[0]:.4f} J")

# Função de integração (trapezoidal)
def integral(f, a, b, dt):
    i_a = max(0, int(a / dt))
    i_b = min(len(f) - 2, int(b / dt))
    integral_sum = 0.0
    for i in range(i_a, i_b):
        integral_sum += (f[i] + f[i+1]) / 2.0 * dt
    return integral_sum

# Cálculo da força de resistência
F_ar = np.zeros((n+1, 3))
for i in range(n+1):
    v = np.sqrt(vx[i]**2 + vy[i]**2 + vz[i]**2)
    F_ar[i, 0] = -m * D * v * vx[i]
    F_ar[i, 1] = -m * D * v * vy[i]
    F_ar[i, 2] = -m * D * v * vz[i]

# Produto escalar F . v
F_dot_v = np.sum(F_ar * np.column_stack((vx[:n+1], vy[:n+1], vz[:n+1])), axis=1)

# Integrais
t1 = 0.2
t2 = 0.4
W_air0 = integral(F_dot_v, t0, t0, dt)
W_air1 = integral(F_dot_v, t0, t1, dt)
W_air2 = integral(F_dot_v, t0, t2, dt)

print(f"Trabalho da resistência do ar em t0 = {W_air0:.4f} J")
print(f"Trabalho da resistência do ar de t0 a t1 = {W_air1:.4f} J")
print(f"Trabalho da resistência do ar de t0 a t2 = {W_air2:.4f} J")

# Comparação com conservação de energia
i_t1 = int(t1 / dt)
W_res_t0_t1_cons = Em[i_t1] - Em[0]
print(f"Trabalho pela conservação de energia (t0 a t1): {W_res_t0_t1_cons:.4f} J")