import numpy as np
import matplotlib.pyplot as plt
#Calcular as frequências angulares dos modos normais de um sistema de osciladores acoplados
#dados iniciais
m = 1.0 #kg
k=1.0  #N/m
k_prime=0.5 #N/m

K_matrix = np.array([
    [-(k + k_prime), k_prime, 0],
    [k_prime, -2*k_prime, k_prime],
    [0, k_prime, -(k + k_prime)]
]) / m


# Cálculo dos vlores proprios e vetores proprios
eigenvalues, eigenvectors = np.linalg.eig(K_matrix)

#As frequencias angulares são as raizes quadradas dos valores proprios
omega = np.sqrt(-eigenvalues)

sorted_indices = np.argsort(omega)
omega_sorted = omega[sorted_indices]
modes_sorted = eigenvectors[:, sorted_indices]

print("Frequências angulares dos modos normais (rad/s):")

for i, freq in enumerate(omega_sorted, 1):
    print(f"Modo {i}: {freq:.4f}")

#Gráficos do momvimento em cada modo normal usando Euler-Cromer

dt = 0.01  # Intervalo de tempo
t_max = 20.0  # Tempo total de simulação
t = np.arange(0, t_max, dt)
n_steps = len(t)

#Condiçoes iniciais para cada modo com os vetores proprios
initial_conditions = modes_sorted.T

plt.figure(figsize=(15, 10))

for mode in range(3):
    u = np.zeros((3, n_steps))
    v = np.zeros((3, n_steps))

    u[:, 0] = initial_conditions[mode]  # Condição inicial para o modo
    v[:, 0] = 0

    for i in range(n_steps -1):
        a_A = (-(k + k_prime)*u[0, i] + k_prime*u[1, i]) / m
        a_B = (k_prime*u[0, i] - 2*k_prime*u[1, i] + k_prime*u[2, i]) / m
        a_C = (k_prime*u[1, i] - (k + k_prime)*u[2, i]) / m


        # Atualiza velocidades
        v[0, i+1] = v[0, i] + a_A * dt
        v[1, i+1] = v[1, i] + a_B * dt
        v[2, i+1] = v[2, i] + a_C * dt
        
        # Atualiza posições
        u[0, i+1] = u[0, i] + v[0, i+1] * dt
        u[1, i+1] = u[1, i] + v[1, i+1] * dt
        u[2, i+1] = u[2, i] + v[2, i+1] * dt
    
    # Plot
    plt.subplot(3, 1, mode+1)
    plt.plot(t, u[0, :], label='Massa A')
    plt.plot(t, u[1, :], label='Massa B')
    plt.plot(t, u[2, :], label='Massa C')
    plt.title(f'Modo Normal {mode+1} - ω = {omega_sorted[mode]:.3f} rad/s')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()