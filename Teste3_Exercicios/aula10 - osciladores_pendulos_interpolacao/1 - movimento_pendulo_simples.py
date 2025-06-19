import numpy as np
import matplotlib.pyplot as plt

#Dados
L = 1.0  # comprimento do pêndulo (m)
g = 9.8  # aceleração da gravidade (m/s²)
theta = 0  # ângulo inicial (rad)
t0 = 0  # tempo inicial (s)
dt = 0.01  # passo de tempo (s)
tf = 10  # tempo final (s)
n = int(tf / dt)  # número de passos de tempo

def euler_cromer(theta0, omega0=0):
    theta = np.zeros(n)
    omega = np.zeros(n)
    t = np.linspace(t0, tf, n)
    
    theta[0] = theta0
    omega[0] = omega0
    
    for i in range(1, n):
        omega[i] = omega[i-1] - (g/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i] * dt
    
    return t, theta

def solucao_analitica(theta0, t):
    A = theta0
    phi = 0  # pois a velocidade inicial é zero
    return A * np.cos(np.sqrt(g/L) * t + phi)

angulos_iniciais = [0.1, 0.3, 0.5]  # rad

for theta0 in angulos_iniciais:
    t, theta_num = euler_cromer(theta0)
    theta_ana = solucao_analitica(theta0, t)

    plt.figure()
    plt.plot(t, theta_num, label='Numérica (Euler-Cromer)')
    plt.plot(t, theta_ana, label='Analítica (linear)', linestyle='--')
    plt.title(f'Comparação para θ₀ = {theta0} rad')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Ângulo θ (rad)')
    plt.legend()
    plt.grid(True)

plt.show()

