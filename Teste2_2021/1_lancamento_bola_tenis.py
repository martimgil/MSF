import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.8  # m/s²
v0 = 140 * 1000 / 3600  # velocidade inicial em m/s
v_terminal = 100 * 1000 / 3600  # velocidade terminal em m/s
theta = np.radians(7)
m = 0.057  # massa da bola (kg)
y0 = 0
x0 = 0
dt = 0.001

# Coeficiente de resistência do ar baseado na velocidade terminal
# F_res = (1/2) * rho * Cd * A * v^2  ->  v_terminal = sqrt((2mg)/(rho*Cd*A))  => rearranjar para encontrar k
# Usamos a forma F_res = k * v^2, então k = mg / v_terminal^2
k = m * g / (v_terminal ** 2)

# Tempo máximo
t_max = 10
t = np.arange(0, t_max, dt)
x = np.zeros(len(t))
y = np.zeros(len(t))
vx = np.zeros(len(t))
vy = np.zeros(len(t))
v = np.zeros(len(t))
F_res = np.zeros(len(t))

# Condições iniciais
x[0] = x0
y[0] = y0
vx[0] = v0 * np.cos(theta)
vy[0] = v0 * np.sin(theta)
v[0] = np.sqrt(vx[0]**2 + vy[0]**2)
F_res[0] = k * v[0]**2

# Simulação
for i in range(1, len(t)):
    v[i-1] = np.sqrt(vx[i-1]**2 + vy[i-1]**2)
    F_res[i-1] = k * v[i-1]**2

    # Componentes da força de resistência
    Fdx = -F_res[i-1] * (vx[i-1] / v[i-1])
    Fdy = -F_res[i-1] * (vy[i-1] / v[i-1])

    # Acelerações
    ax = Fdx / m
    ay = Fdy / m - g

    # Atualização
    vx[i] = vx[i-1] + ax * dt
    vy[i] = vy[i-1] + ay * dt

    x[i] = x[i-1] + vx[i-1] * dt
    y[i] = y[i-1] + vy[i-1] * dt

    if y[i] < 0:
        x = x[:i+1]
        y = y[:i+1]
        vx = vx[:i+1]
        vy = vy[:i+1]
        v = v[:i]
        F_res = F_res[:i]
        t = t[:i+1]
        break

# Recalcular velocidade total para último ponto
v = np.sqrt(vx**2 + vy**2)
F_res = k * v**2

# Cálculo do trabalho pela regra trapezoidal
W_res = -np.trapz(F_res * v, dx=dt)

# Plot da trajetória
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Trajetória da bola de tênis com resistência do ar')
plt.xlabel('Distância (m)')
plt.ylabel('Altura (m)')
plt.grid()
plt.show()

# Resultados
print(f'Alcance aproximado: {x[-1]:.2f} metros')
print(f'Trabalho realizado pela resistência do ar: {W_res:.2f} J')
