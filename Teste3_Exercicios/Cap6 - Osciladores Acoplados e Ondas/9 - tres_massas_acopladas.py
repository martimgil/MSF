import numpy as np
import matplotlib.pyplot as plt

# a) Cálculo das frequências angulares dos 3 modos normais de oscilação
# Dados fornecidos
k = 1  # constante da mola em N/m
k_prime = 0.5  # constante da mola em N/m
m = 1  # massa em kg

# Matriz de coeficientes do sistema
M = m * np.eye(3)  # Matriz de massa (identidade, pois as massas são iguais)
K = np.array([[ k + 2*k_prime, -k_prime, 0],
              [-k_prime, 2*k_prime + k, -k_prime],
              [0, -k_prime, k + 2*k_prime]])

# Resolvendo o problema de autovalores e autovetores
# Para encontrar as frequências normais do sistema
eigvals, eigvecs = np.linalg.eig(np.linalg.inv(M).dot(K))

# Frequências angulares (ω) correspondem à raiz quadrada dos autovalores
frequencias_angulares = np.sqrt(np.abs(eigvals))

# Frequências angulares em Hz (dividindo por 2*pi)
frequencias_hz = frequencias_angulares / (2 * np.pi)

# Exibindo os resultados
print("Frequências angulares (rad/s):", frequencias_angulares)
print("Frequências em Hz:", frequencias_hz)

# b) Simulação do movimento das massas usando o método de Euler-Cromer

# Parâmetros de simulação
t_max = 20  # tempo máximo de simulação em segundos
dt = 0.01  # passo de tempo
t = np.arange(0, t_max, dt)  # vetor de tempo

# Função para o método de Euler-Cromer
def euler_cromer_corrected(mode_frequencies, initial_conditions):
    num_modes = len(mode_frequencies)
    positions = np.zeros((3, len(t)))  # posições das 3 massas
    velocities = np.zeros_like(positions)  # velocidades das 3 massas

    # Inicializando as condições iniciais
    positions[:, 0] = initial_conditions

    # Calculando o movimento ao longo do tempo
    for i in range(1, len(t)):
        for j in range(3):
            # Aceleração proporcional ao modo normal
            acceleration = -mode_frequencies[j]**2 * positions[j, i-1]
            velocities[j, i] = velocities[j, i-1] + acceleration * dt
            positions[j, i] = positions[j, i-1] + velocities[j, i] * dt

    return positions

initial_conditions_1 = np.array([1, 0, 0])  # deslocamento inicial na massa A (modo 1)
initial_conditions_2 = np.array([0, 1, 0])  # deslocamento inicial na massa B (modo 2)
initial_conditions_3 = np.array([0, 0, 1])  # deslocamento inicial na massa C (modo 3)

positions_1 = euler_cromer_corrected([frequencias_angulares[0]] * 3, initial_conditions_1)
positions_2 = euler_cromer_corrected([frequencias_angulares[1]] * 3, initial_conditions_2)
positions_3 = euler_cromer_corrected([frequencias_angulares[2]] * 3, initial_conditions_3)

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, positions_1[0], label='Modo 1')
plt.title('Movimento das Massas (Modo 1)')
plt.xlabel('Tempo [s]')
plt.ylabel('Deslocamento [m]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, positions_2[1], label='Modo 2')
plt.title('Movimento das Massas (Modo 2)')
plt.xlabel('Tempo [s]')
plt.ylabel('Deslocamento [m]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, positions_3[2], label='Modo 3')
plt.title('Movimento das Massas (Modo 3)')
plt.xlabel('Tempo [s]')
plt.ylabel('Deslocamento [m]')
plt.grid(True)

plt.tight_layout()
plt.show()
