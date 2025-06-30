import numpy as np
import matplotlib.pyplot as plt


# Dados
m = 2
xeq = 0
k = 0.5
b = 0.2
x0 = 0.2
v0 = 0
dt = 0.0001
t_total = 60


n_steps = int(t_total / dt)
t = np.zeros(n_steps)
x = np.zeros(n_steps)
v = np.zeros(n_steps)

# Condições iniciais
t[0] = 0
x[0] = x0
v[0] = v0

# Integração
for i in range(1, n_steps):
    t[i] = t[i-1] + dt
    x[i] = x[i-1] + v[i-1] * dt
    f = -k*x[i-1] + (-b*v[i-1])
    v[i] = v[i-1] + f * dt / m



plt.plot(t, x, label='Posição x(t)', color='orange')
plt.title('Movimento do Oscilador Harmônico Forçado')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.show()

plt.plot(t, v, label='Velocidade v(t)', color='green')
plt.title('Velocidade do Oscilador Harmônico Forçado')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.legend()
plt.show()

# b) Aplicação de uma força externa 
wf=1.0
n_steps = int(t_total / dt)
t = np.zeros(n_steps)
x = np.zeros(n_steps)
v = np.zeros(n_steps)

# Condições iniciais
t[0] = 0
x[0] = x0
v[0] = v0


# Integração
for i in range(1, n_steps):
    t[i] = t[i-1] + dt
    x[i] = x[i-1] + v[i-1] * dt
    f = -k*x[i-1] + (-b*v[i-1]) + 5* np.cos(wf * t[i-1])  # Força externa aplicada
    v[i] = v[i-1] + f * dt / m



t_estacionario = t[t>30]
x_estacionario = x[t>30]

maximos = []

for i in range(1, len(x_estacionario)-1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])
amplitude = np.mean(maximos)
print(f"Amplitude no regime estacionário: {amplitude:.2f} m")

# c) Redução da frequencia da força externa

wf = 0.5
n_steps = int(t_total / dt)
t = np.zeros(n_steps)
x = np.zeros(n_steps)
v = np.zeros(n_steps)

# Condições iniciais
t[0] = 0
x[0] = x0
v[0] = v0

# Integração
for i in range(1, n_steps):
    t[i] = t[i-1] + dt
    x[i] = x[i-1] + v[i-1] * dt
    f = -k*x[i-1] + (-b*v[i-1]) + 5* np.cos(wf * t[i-1])  # Força externa aplicada
    v[i] = v[i-1] + f * dt / m

t_estacionario = t[t>30]
x_estacionario = x[t>30]

maximos = []

for i in range(1, len(x_estacionario)-1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])
amplitude = np.mean(maximos)
print(f"Amplitude no regime estacionário: {amplitude:.2f} m")
print("As amplitudes são tão diferentes porque a frequencia da força externa agora aproxima-se da frequencia natural ou seja ocorre ressonancia e a amplitude atinge o maximo possivel dentro dos limites impostos por b")