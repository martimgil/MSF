import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.81  # gravidade [m/s²]
m = 0.057  # massa da bola [kg]
r = 0.034  # raio da bola [m]
A = np.pi * r**2  # área da secção transversal da bola
rho_ar = 1.225  # densidade do ar [kg/m³]
v_terminal = 20  # velocidade terminal [m/s]
k_drag = m * g / v_terminal**2  # coeficiente de resistência do ar

# Condições iniciais
x0, y0 = 0, 3  # posição inicial (x, y) [m]
vx0, vy0 = 30, 0  # velocidade inicial (vx, vy) [m/s]
v0 = np.array([vx0, vy0])  # vetor velocidade inicial

# Simulação
dt = 0.001  # passo de tempo
t_max = 2  # tempo máximo de simulação [s]
steps = int(t_max / dt)

# Inicialização dos arrays
x = np.zeros(steps)
y = np.zeros(steps)
vx = np.zeros(steps)
vy = np.zeros(steps)

x[0], y[0] = x0, y0
vx[0], vy[0] = vx0, vy0

# Simulação sem efeito Magnus
for i in range(steps - 1):
    v = np.array([vx[i], vy[i]])
    v_norm = np.linalg.norm(v)
    if y[i] < 0:
        x = x[:i]
        y = y[:i]
        break
    # Força de resistência do ar
    F_drag = -k_drag * v_norm * v
    ax = F_drag[0] / m
    ay = (F_drag[1] - m * g) / m
    # Atualiza velocidade e posição
    vx[i + 1] = vx[i] + ax * dt
    vy[i + 1] = vy[i] + ay * dt
    x[i + 1] = x[i] + vx[i] * dt
    y[i + 1] = y[i] + vy[i] * dt

# Verifica validade do saque
x_final = x[-1]
valido = (x_final >= 12) and (x_final <= 18.4) and (np.interp(12, x, y) > 1)

# Gráfico do movimento
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Trajetória da bola")
plt.axhline(1, color='red', linestyle='--', label='Altura da rede (1m)')
plt.axvline(12, color='gray', linestyle='--', label='Rede (x=12m)')
plt.axvline(18.4, color='green', linestyle='--', label='Fim da área válida')
plt.axvline(12, color='green', linestyle='--')
plt.xlabel("Distância (x) [m]")
plt.ylabel("Altura (y) [m]")
plt.title("Movimento da bola de tênis (sem efeito Magnus)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

x_final, valido

### b) Simulação com efeito Magnus ### 
# # Vetor de rotação
omega = np.array([0, 0, -60])  # rotação em rad/s no eixo z (spin para baixo)

# Re-inicialização dos arrays
x_m = np.zeros(steps)
y_m = np.zeros(steps)
vx_m = np.zeros(steps)
vy_m = np.zeros(steps)

x_m[0], y_m[0] = x0, y0
vx_m[0], vy_m[0] = vx0, vy0

# Simulação com efeito Magnus
for i in range(steps - 1):
    v = np.array([vx_m[i], vy_m[i], 0])
    v_norm = np.linalg.norm(v)
    if y_m[i] < 0:
        x_m = x_m[:i]
        y_m = y_m[:i]
        break
    # Força de resistência do ar
    F_drag = -k_drag * v_norm * v[:2]
    # Força de Magnus
    F_magnus_3d = 0.5 * A * rho_ar * r * np.cross(omega, v)
    F_magnus = F_magnus_3d[:2]
    # Acelerações
    ax = (F_drag[0] + F_magnus[0]) / m
    ay = (F_drag[1] + F_magnus[1] - m * g) / m
    # Atualiza velocidades e posições
    vx_m[i + 1] = vx_m[i] + ax * dt
    vy_m[i + 1] = vy_m[i] + ay * dt
    x_m[i + 1] = x_m[i] + vx_m[i] * dt
    y_m[i + 1] = y_m[i] + vy_m[i] * dt

# Verifica validade do saque com Magnus
x_final_m = x_m[-1]
valido_m = (x_final_m >= 12) and (x_final_m <= 18.4) and (np.interp(12, x_m, y_m) > 1)

# Gráfico do movimento com efeito Magnus
plt.figure(figsize=(10, 5))
plt.plot(x_m, y_m, label="Trajetória com efeito Magnus", color="blue")
plt.axhline(1, color='red', linestyle='--', label='Altura da rede (1m)')
plt.axvline(12, color='gray', linestyle='--', label='Rede (x=12m)')
plt.axvline(18.4, color='green', linestyle='--', label='Fim da área válida')
plt.axvline(12, color='green', linestyle='--')
plt.xlabel("Distância (x) [m]")
plt.ylabel("Altura (y) [m]")
plt.title("Movimento da bola de tênis (com efeito Magnus)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

x_final_m, valido_m
