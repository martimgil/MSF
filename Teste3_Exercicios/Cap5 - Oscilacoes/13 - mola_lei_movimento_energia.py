import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
k = 1.0  # N/m
m = 1.0  # kg
x0 = 4.0  # m
v0 = 0.0  # m/s
t_max = 10.0  
dt = 0.01  

t = np.arange(0, t_max, dt)
x = np.zeros_like(t)
v = np.zeros_like(t)
x[0] = x0
v[0] = v0

# Método de Euler
for i in range(1, len(t)):
    a = -k / m * x[i-1]  # Aceleração: a = -k x / m
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i-1] * dt

# Gráfico da posição x(t)
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='x(t) (m)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Movimento do Oscilador Harmônico Simples')
plt.grid()
plt.legend()
plt.show()

# Amplitude (máximo valor absoluto de x)
amplitude = np.max(np.abs(x))
print(f"Amplitude: {amplitude:.2f} m")

# Cálculo do Período (encontrar os picos de x(t))
peaks = []
for i in range(1, len(x)-1):
    if x[i] > x[i-1] and x[i] > x[i+1]:  
        peaks.append(i)

if len(peaks) >= 2:
    periodo = t[peaks[1]] - t[peaks[0]]
    print(f"Período: {periodo:.2f} s (teórico: {2*np.pi:.2f} s)")
else:
    print("Não foram encontrados picos suficientes para calcular o período.")

# Energia Mecânica
K = 0.5 * m * v**2  # Energia cinética
U = 0.5 * k * x**2  # Energia potencial
E = K + U  # Energia mecânica

# Gráfico da Energia Mecânica
plt.figure(figsize=(10, 5))
plt.plot(t, E, label='Energia Mecânica (J)', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('Energia Mecânica do Sistema')
plt.grid()
plt.legend()
plt.show()

# Verificar se a energia é constante (variação pequena devido a erros numéricos)
delta_E = np.max(E) - np.min(E)
print(f"Variação da Energia Mecânica: {delta_E:.2e} J")