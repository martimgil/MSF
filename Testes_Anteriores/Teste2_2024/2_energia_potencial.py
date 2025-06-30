import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 2  # J/m^4
m = 0.5  # kg

# Forca
def force(x):
    return -4 * k * x**3 + k * x

# Energia potencial
def potential(x):
    return k * (x - 0.5)**2 * (x + 0.5)**2

# Energia cinetica
def kinetic(v):
    return 0.5 * m * v**2

# Gráfico do potencial (alínea a)
x_vals = np.linspace(-1.5, 1.5, 1000)
Ep_vals = potential(x_vals)

plt.figure(figsize=(8, 4))
plt.plot(x_vals, Ep_vals, label="Energia Potencial")
plt.axhline(0.25, color='r', linestyle='--', label="E = 0.25 J")
plt.xlabel("Posição x (m)")
plt.ylabel("Energia Potencial (J)")
plt.title("Diagrama de Energia Potencial do Oscilador Quártico")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Integração por método de Euler-Cromer (alínea b)
dt = 0.001  # passo de tempo
t_max = 20  # segundos
n = int(t_max / dt)

t = np.linspace(0, t_max, n)
x = np.zeros(n)
v = np.zeros(n)

# Condições iniciais
x[0] = 1.0
v[0] = 0.0

# Vetores para energia
Ep = np.zeros(n)
Ec = np.zeros(n)
Etot = np.zeros(n)

for i in range(n-1):
    a = force(x[i]) / m
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i+1] * dt  # Euler-Cromer
    
    Ep[i] = potential(x[i])
    Ec[i] = kinetic(v[i])
    Etot[i] = Ep[i] + Ec[i]

Ep[-1] = potential(x[-1])
Ec[-1] = kinetic(v[-1])
Etot[-1] = Ep[-1] + Ec[-1]

# Gráfico da posição vs tempo (alínea b)
plt.figure(figsize=(8, 4))
plt.plot(t, x)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.title("Movimento no Oscilador Quártico")
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico das energias (alínea c)
plt.figure(figsize=(12, 6))
plt.plot(t, Ep, label="Energia Potencial")
plt.plot(t, Ec, label="Energia Cinética")
plt.plot(t, Etot, label="Energia Total", linestyle='--')
plt.xlabel("Tempo (s)")
plt.ylabel("Energia (J)")
plt.title("Energia vs Tempo no Oscilador Quártico")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Parte (d): Velocidade em x = 0.5 m
# Procurar instante mais próximo de x = 0.5
idx = np.argmin(np.abs(x - 0.5))
print(f"Velocidade em x = 0.5 m: {v[idx]:.4f} m/s")
