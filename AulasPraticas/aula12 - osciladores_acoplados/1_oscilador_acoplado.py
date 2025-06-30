import numpy as np
import matplotlib.pyplot as plt

k = 1.0
k_prime = 0.5
m = 1.0
x_A_eq = 1.0
x_B_eq = 2.0

t_max = 30.0
dt = 0.01
steps = int(t_max / dt)
t = np.linspace(0, t_max, steps)

def solved_coupled_oscillators(xA0, xB0, vA0, vB0):
    xA = np.zeros(steps)
    xB = np.zeros(steps)
    vA = np.zeros(steps)
    vB = np.zeros(steps)

    xA[0] = xA0
    xB[0] = xB0
    vA[0] = vA0
    vB[0] = vB0

    for i in range(1, steps):
        F_A = -k * (xA[i-1] - x_A_eq) - k_prime * (xA[i-1] - xB[i-1])
        F_B = -k * (xB[i-1] - x_B_eq)

        aA = F_A / m
        aB = F_B / m

        vA[i] = vA[i-1] + aA * dt
        vB[i] = vB[i-1] + aB * dt
        xA[i] = xA[i-1] + vA[i-1] * dt
        xB[i] = xB[i-1] + vB[i-1] * dt

    return xA, xB

### CASO I ###

xA0_i = x_A_eq + 0.3
xB0_i = x_B_eq + 0.3
vA0_i = 0.0
vB0_i = 0.0

xA_i, xB_i = solved_coupled_oscillators(xA0_i, xB0_i, vA0_i, vB0_i)

plt.figure(figsize=(12, 6))
plt.plot(t, xA_i, label='Oscilador A', color='blue')
plt.plot(t, xB_i, label='Oscilador B', color='orange')
plt.title("Caso I")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend()
plt.grid()
plt.show()

### CASO II ###

xA0_ii = x_A_eq + 0.3
xB0_ii = x_B_eq + 0.3
vA0_ii = 0
vB0_ii = 0

xA_ii, xB_ii = solved_coupled_oscillators(xA0_ii, xB0_ii, vA0_ii, vB0_ii)

plt.figure(figsize=(12, 6))
plt.plot(t, xA_ii, label='Oscilador A', color='blue')
plt.plot(t, xB_ii, label='Oscilador B', color='orange')
plt.title("Caso II")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend()
plt.grid()
plt.show()

### CASO III ###

xA0_iii = x_A_eq + 0.3
xB0_iii = x_B_eq + 0.3
vA0_iii = 0
vB0_iii = 0.5

xA_iii, xB_iii = solved_coupled_oscillators(xA0_iii, xB0_iii, vA0_iii, vB0_iii)

plt.figure(figsize=(12, 6))
plt.plot(t, xA_iii, label='Oscilador A', color='blue')
plt.plot(t, xB_iii, label='Oscilador B', color='orange')
plt.title("Caso III")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend()
plt.grid()
plt.show()

"""
b) 

Caso i): Os dois corpos oscilam em fase, com a mesma frequência. O acoplamento não é visível porque ambos foram deslocados igualmente.

Caso ii): Os corpos oscilam em oposição de fase (quando um vai para a direita, o outro vai para a esquerda). Mostra o modo antissimétrico do sistema acoplado.

Caso iii): O movimento é uma combinação dos dois modos anteriores, resultando em batimentos - a energia é transferida periodicamente de um oscilador para o outro.

"""