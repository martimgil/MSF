import numpy as np
import matplotlib.pyplot as plt

# Dados
m = 1.0
k = 1.0
b = 0.16
F0 = 2.0
wf = 2.0

x0 = 4.0
v0 = 0.0

t0 = 0.0
tf = 200.0
dt = 0.01
n = int((tf - t0) / dt) + 1
t = np.linspace(t0, tf, n)
x = np.zeros(n)
v = np.zeros(n)

# Condições iniciais
x[0] = x0
v[0] = v0

for i in range(n-1):
    F = -k * x[i] - b * v[i] + F0 * np.cos(wf * t[i])  # Força total
    a = F / m  # Aceleração
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i] * dt


plt.figure(figsize=(10, 5))
plt.plot(t, x, 'b-', linewidth=1)
plt.title('Lei do movimento do oscilador harmônico forçado e amortecido')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid(True)
plt.show()

# b) - Amplitude e periodo no regime estacionario

t_estacionario = t[t>30]
x_estacionario = x[t>30]

maximos = []

for i in range(1, len(x_estacionario)-1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])
amplitude = np.mean(maximos)
print(f"Amplitude no regime estacionário: {amplitude:.2f} m")

#Calculamos o periodo encontrando o tempo entre maximos consecutivos

indices_maximos = []
for i in range(1, len(x_estacionario)-1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        indices_maximos.append(i)

if len(indices_maximos) > 1:
    periodos = np.diff(t_estacionario[indices_maximos])
    periodo = np.mean(periodos)
    print(f"Período no regime estacionário: {periodo:.4f} s")
    print(f"Frequência angular medida: {2*np.pi/periodo:.4f} rad/s (deve ser próxima de wf = {wf} rad/s)")
else:
    print("Não foram encontrados máximos suficientes para calcular o período")

