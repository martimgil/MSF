import numpy as np
import matplotlib.pyplot as plt

'''
a) Simule o movimento do pêndulo usando o método de Euler-Cromer
durante 10s. O pêndulo comece com ângulo = 0.1 rad com velocidade nula
'''

# Constantes
g = 9.8      # m/s²
L = 1.0      # m
dt = 0.01    # passo de tempo
T = 10       # tempo total (s)
n = int(T / dt)

# Função para o método de Euler-Cromer
def euler_cromer(theta0, omega0=0):
    theta = np.zeros(n)
    omega = np.zeros(n)
    t = np.linspace(0, T, n)
    
    theta[0] = theta0
    omega[0] = omega0
    
    for i in range(1, n):
        omega[i] = omega[i-1] - (g/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i] * dt
    
    return t, theta

"""
b) solucao analitica 
"""
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