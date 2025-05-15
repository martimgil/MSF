import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos
r = 0.11  # raio da bola (m)
m = 0.45  # massa da bola (kg)
rho_ar = 1.225  # densidade do ar (kg/m^3)
A = np.pi * r**2  # área de secção transversal (m^2)
g = 9.8  # aceleração gravitacional (m/s^2)
v_terminal = 27.78  # velocidade terminal (m/s)

# Constante de resistência do ar (a partir da velocidade terminal)
k = m * g / v_terminal**2

# Parâmetros iniciais
v0 = 27.78  # velocidade inicial (m/s)
theta_deg = 16  # ângulo com a horizontal
phi_deg = 0     # sem efeito lateral inicialmente
theta = np.radians(theta_deg)
phi = np.radians(phi_deg)

# Componentes da velocidade inicial (em 3D)
v0x = v0 * np.cos(theta) * np.cos(phi)
v0y = v0 * np.sin(theta)
v0z = v0 * np.cos(theta) * np.sin(phi)

# Vetores iniciais
r_vec = np.array([0.0, 0.0, 0.0])  # posição inicial (x, y, z)
v_vec = np.array([v0x, v0y, v0z])  # velocidade inicial (x, y, z)

# Parâmetros de simulação
dt = 0.001  # passo de tempo
t_max = 3.0
steps = int(t_max / dt)

# Armazenamento para gráficos
traj = np.zeros((steps, 3))

# Sem rotação (sem Magnus para já)
omega = np.array([0.0, 0.0, 0.0])  # vetor de rotação

# Simulação com método de Euler
for i in range(steps):
    v = np.linalg.norm(v_vec)
    
    # Força de resistência do ar: -k * v * v̂
    F_ar = -k * v * v_vec
    
    # Força de Magnus: (1/2) * A * rho * r * (omega x v)
    F_magnus = 0.5 * A * rho_ar * r * np.cross(omega, v_vec)
    
    F_total = np.array([0, -m * g, 0]) + F_ar + F_magnus
    
    a_vec = F_total / m
    v_vec += a_vec * dt
    r_vec += v_vec * dt

    traj[i] = r_vec

    if r_vec[0] > 21:
        traj = traj[:i+1]
        break

x, y, z = traj[:, 0], traj[:, 1], traj[:, 2]

# Plot 3D da trajetória
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, z, y, label="Trajetória da bola", color='orange')
ax.set_xlabel("x (direção baliza) [m]")
ax.set_ylabel("z (lateral) [m]")
ax.set_zlabel("y (altura) [m]")
ax.set_title("Trajetória da bola com resistência do ar")
ax.legend()
ax.set_xlim(0, 25)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 5)

# Baliza
ax.plot([20, 20], [-3.75, 3.75], [0, 0], 'k--')
ax.plot([20, 20], [-3.75, -3.75], [0, 2.4], 'g--')
ax.plot([20, 20], [3.75, 3.75], [0, 2.4], 'g--')

plt.show()
