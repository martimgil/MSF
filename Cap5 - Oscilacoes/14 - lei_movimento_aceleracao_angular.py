import numpy as np
import matplotlib.pyplot as plt

# Dados
g = 9.8
L = 0.5
omega = np.sqrt(g / L)

theta0 = 0.1
dtheta0 = 0.5

t_max = 10.0
dt = 0.01
n_steps = int(t_max / dt)

t = np.linspace(0, t_max, n_steps)
theta = np.zeros(n_steps)
dtheta = np.zeros(n_steps)

theta[0] = theta0
dtheta[0] = dtheta0

for i in range(1, n_steps):
    d2theta = -(g/L) * theta[i-1] #Aceleração angular: d²θ/dt² = -g/L * θ
    dtheta[i] = dtheta[i-1] + d2theta * dt #Atualiza velocidade
    theta[i] = theta[i-1] + dtheta[i-1] * dt #Atualiza posição

plt.figure(figsize=(10, 5))
plt.plot(t, theta, label='θ(t) (rad)')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (rad)')
plt.title('Movimento de um Pêndulo Simples')
plt.grid()
plt.legend()
plt.show()

amplitude = np.max(np.abs(theta))

# Encontra o período (tempo entre dois máximos consecutivos)
peaks = np.where(np.diff(np.sign(np.diff(theta))) < 0)[0] + 1
if len(peaks) >= 2:
    period = t[peaks[1]] - t[peaks[0]]
else:
    period = 2 * np.pi / omega  # Valor teórico se não houver picos suficientes

print(f"Amplitude do movimento: {amplitude:.3f} rad")
print(f"Período do movimento: {period:.3f} s")