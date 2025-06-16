import numpy as np
import matplotlib.pyplot as plt

k = 1.0     
k_ = 0.5    
m = 1.0     
xAeq = 1.0  
xBeq = 2.0  

dt = 0.01    
T = 40        
N = int(T/dt) 
t = np.linspace(0, T, N)

def simular_movimento(xA0, xB0, vA0=0, vB0=0):
    xA = np.zeros(N)
    xB = np.zeros(N)
    vA = np.zeros(N)
    vB = np.zeros(N)

    xA[0] = xA0
    xB[0] = xB0
    vA[0] = vA0
    vB[0] = vB0c

    for i in range(N - 1):
        FA = -k * (xA[i] - xAeq) + k_ * (xB[i] - xA[i] - (xBeq - xAeq))
        FB = -k * (xB[i] - xBeq) - k_ * (xB[i] - xA[i] - (xBeq - xAeq))

        aA = FA / m
        aB = FB / m

        vA[i + 1] = vA[i] + aA * dt
        vB[i + 1] = vB[i] + aB * dt
        xA[i + 1] = xA[i] + vA[i + 1] * dt
        xB[i + 1] = xB[i] + vB[i + 1] * dt

    return xA, xB

casos = {
    "(i)": (xAeq + 0.3, xBeq + 0.3),
    "(ii)": (xAeq + 0.3, xBeq - 0.3),
    "(iii)": (xAeq + 0.3, xBeq - 0.1)
}

plt.figure(figsize=(14, 10))

for i, (label, (xA0, xB0)) in enumerate(casos.items(), 1):
    xA, xB = simular_movimento(xA0, xB0)
    plt.subplot(3, 1, i)
    plt.plot(t, xA, label='xA(t)', color='blue')
    plt.plot(t, xB, label='xB(t)', color='red')
    plt.title(f"Movimento dos Corpos A e B - Caso {label}")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

print("(i) Modo normal simétrico, em fase.")
print("(ii) Modo normal anti-simétrico, fora de fase.")
print("(iii) Combinação dos modos normais: batimentos entre modos em fase e fora de fase.")