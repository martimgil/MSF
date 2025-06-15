import numpy as np
import matplotlib.pyplot as plt

# Constantes do sistema
k = 1.0       # N/m
k_ = 0.5      # N/m
m = 1.0       # kg
xAeq = 1.0    # m
xBeq = 2.0    # m

# Frequência angular base (usada depois no Fourier)
T = 100       # período total (s)
dt = 0.01     # passo de tempo
N = int(T/dt) # número de passos
t = np.linspace(0, T, N)
w = 2 * np.pi / T

def simular(xA0, xB0, vA0, vB0):
    xA = np.zeros(N)
    xB = np.zeros(N)
    vA = np.zeros(N)
    vB = np.zeros(N)
    xA[0], xB[0], vA[0], vB[0] = xA0, xB0, vA0, vB0

    for i in range(N-1):
        aA = (-k*(xA[i]-xAeq) - k_*(xA[i]-xB[i])) / m
        aB = (-k*(xB[i]-xBeq) - k_*(xB[i]-xA[i])) / m

        vA[i+1] = vA[i] + aA*dt
        vB[i+1] = vB[i] + aB*dt
        xA[i+1] = xA[i] + vA[i+1]*dt
        xB[i+1] = xB[i] + vB[i+1]*dt

    return xA, xB

# Função para calcular coeficientes de Fourier
def calcular_fourier(x, t, n_max):
    a_n, b_n = [], []
    for n in range(1, n_max+1):
        wn = n * w
        cos_nwt = np.cos(wn * t)
        sin_nwt = np.sin(wn * t)
        a_n.append((2/T) * np.trapezoid(x * cos_nwt, t))
        b_n.append((2/T) * np.trapezoid(x * sin_nwt, t))
    return np.array(a_n), np.array(b_n)

casos = [
    (xAeq + 0.3, xBeq + 0.3, 0, 0),
    (xAeq + 0.3, xBeq - 0.3, 0, 0),
    (xAeq + 0.3, xBeq - 0.1, 0, 0)
]

# Análise de Fourier para cada caso
resultados_fourier = []
for xA0, xB0, vA0, vB0 in casos:
    xA, xB = simular(xA0, xB0, vA0, vB0)
    a_n, b_n = calcular_fourier(xA, t, 30)  # Fourier em xA
    resultados_fourier.append((a_n, b_n))

# Plot dos coeficientes de Fourier
frequencias = np.arange(1, 31) * w
fig, axs = plt.subplots(3, 2, figsize=(12, 10))

for i, (a_n, b_n) in enumerate(resultados_fourier):
    axs[i, 0].stem(frequencias, a_n)
    axs[i, 0].set_title(f'Caso {i+1}: Coeficientes aₙ')
    axs[i, 0].set_xlabel('Frequência (rad/s)')
    axs[i, 0].set_ylabel('aₙ')
    axs[i, 0].grid(True)

    axs[i, 1].stem(frequencias, b_n)
    axs[i, 1].set_title(f'Caso {i+1}: Coeficientes bₙ')
    axs[i, 1].set_xlabel('Frequência (rad/s)')
    axs[i, 1].set_ylabel('bₙ')
    axs[i, 1].grid(True)

plt.tight_layout()
plt.show()