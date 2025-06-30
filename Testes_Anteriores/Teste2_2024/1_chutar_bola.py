import numpy as np
import matplotlib.pyplot as plt

# Parâmetros iniciais
t0 = 0.0
tf = 2.0  # Tempo maior para alcançar 20m
dt = 0.001

# Conversão de velocidade inicial
v0_magnitude = 100 * 1000 / 3600  # 100 km/h para m/s
theta = np.radians(16)  # Ângulo de 16° em radianos

# Componentes da velocidade inicial (x horizontal, y vertical, z lateral)
v0 = np.array([
    v0_magnitude * np.cos(theta),  # componente x
    v0_magnitude * np.sin(theta),  # componente y
    0.0                            # componente z inicialmente zero
])

r0 = np.array([0.0, 0.0, 0.0])  # Posição inicial (origem)

# Parâmetros físicos
g = 9.8  # aceleração da gravidade
R = 0.11  # raio da bola em metros
A = np.pi * R**2  # área da seção transversal
m = 0.45  # massa da bola em kg
rho_ar = 1.225  # densidade do ar em kg/m³
D = 0.0127  # coeficiente de resistência do ar em m⁻¹
omega = np.array([0, 0, -10])  # vetor rotação em rad/s

# Arrays para armazenar resultados
t = np.arange(t0, tf, dt)
a = np.zeros([3, np.size(t)])
v = np.zeros([3, np.size(t)])
v[:, 0] = v0

r = np.zeros([3, np.size(t)])
r[:, 0] = r0

# Simulação para parte (a) - sem efeito Magnus
for i in range(np.size(t) - 1):
    v_norm = np.linalg.norm(v[:, i])
    a[0, i] = -D * v[0, i] * v_norm  # aceleração em x
    a[1, i] = -g - D * v[1, i] * v_norm  # aceleração em y
    a[2, i] = -D * v[2, i] * v_norm  # aceleração em z
    v[:, i + 1] = v[:, i] + a[:, i] * dt
    r[:, i + 1] = r[:, i] + v[:, i] * dt
    
    # Parar quando atingir x = 20m
    if r[0, i + 1] >= 20:
        break

# Encontrar o índice quando x ≈ 20m
idx_20m = np.argmax(r[0, :] >= 20)
t_20m = t[idx_20m]
x_20m = r[0, idx_20m]
y_20m = r[1, idx_20m]
z_20m = r[2, idx_20m]

# Verificar se é gol para parte (a)
is_goal_a = (0 < y_20m < 2.4) and (-3.75 < z_20m < 3.75)

print("Parte (a) - Sem efeito Magnus:")
print(f"Tempo para atingir 20m: {t_20m:.3f} s")
print(f"Posição em x=20m: y = {y_20m:.3f} m, z = {z_20m:.3f} m")
print(f"É golo? {'Sim' if is_goal_a else 'Não'}")

# Reset para parte (b) - com efeito Magnus
v[:, 0] = v0
r[:, 0] = r0

# Simulação para parte (b) - com efeito Magnus
for i in range(np.size(t) - 1):
    v_norm = np.linalg.norm(v[:, i])
    
    # Força de Magnus (apenas componentes x e y pois ω está em z)
    F_magnus_x = 0.5 * A * rho_ar * R * (omega[1]*v[2,i] - omega[2]*v[1,i]) / m
    F_magnus_y = 0.5 * A * rho_ar * R * (omega[2]*v[0,i] - omega[0]*v[2,i]) / m
    F_magnus_z = 0.5 * A * rho_ar * R * (omega[0]*v[1,i] - omega[1]*v[0,i]) / m
    
    a[0, i] = -D * v[0, i] * v_norm + F_magnus_x
    a[1, i] = -g - D * v[1, i] * v_norm + F_magnus_y
    a[2, i] = -D * v[2, i] * v_norm + F_magnus_z
    
    v[:, i + 1] = v[:, i] + a[:, i] * dt
    r[:, i + 1] = r[:, i] + v[:, i] * dt
    
    # Parar quando atingir x = 20m
    if r[0, i + 1] >= 20:
        break

# Encontrar o índice quando x ≈ 20m para parte (b)
idx_20m_b = np.argmax(r[0, :] >= 20)
t_20m_b = t[idx_20m_b]
x_20m_b = r[0, idx_20m_b]
y_20m_b = r[1, idx_20m_b]
z_20m_b = r[2, idx_20m_b]

is_goal_b = (0 < y_20m_b < 2.4) and (-3.75 < z_20m_b < 3.75)

print("\nParte (b) - Com efeito Magnus:")
print(f"Tempo para atingir 20m: {t_20m_b:.3f} s")
print(f"Posição em x=20m: y = {y_20m_b:.3f} m, z = {z_20m_b:.3f} m")
print(f"É golo? {'Sim' if is_goal_b else 'Não'}")