import numpy as np
import matplotlib.pyplot as plt

k = 1.0          
k_prime = 0.5    
m = 1.0          
xAeq = 1.0  
xBeq = 2.0    

omega1 = np.sqrt(k/m)
omega2 = np.sqrt((k + 2*k_prime)/m)

t = np.linspace(0, 40, 1000)

# Função para solução analítica
def analytical_solution(t, A1, phi1, A2, phi2):
    xA = xAeq + A1 * np.cos(omega1*t + phi1) + A2 * np.cos(omega2*t + phi2)
    xB = xBeq + A1 * np.cos(omega1*t + phi1) - A2 * np.cos(omega2*t + phi2)
    return xA, xB

# Função para solução numérica (integração de Euler)
def numerical_solution(xA0, xB0, vA0, vB0, t):
    dt = t[1] - t[0]
    xA = np.zeros_like(t)
    xB = np.zeros_like(t)
    vA = np.zeros_like(t)
    vB = np.zeros_like(t)
    
    xA[0] = xA0
    xB[0] = xB0
    vA[0] = vA0
    vB[0] = vB0
    
    for i in range(1, len(t)):
        FA = -k*(xA[i-1]-xAeq) + k_prime*(xB[i] - xA[i] - (xBeq - xAeq))
        FB = -k*(xB[i-1]-xBeq) - k_prime*(xB[i] - xA[i] - (xBeq - xAeq))
        
        vA[i] = vA[i-1] + (FA/m)*dt
        vB[i] = vB[i-1] + (FB/m)*dt
        xA[i] = xA[i-1] + vA[i]*dt  
        xB[i] = xB[i-1] + vB[i]*dt
    
    return xA, xB

cases = [
    {'name': 'Caso i) xA0=1.3m, xB0=2.3m', 'xA0': 1.3, 'xB0': 2.3, 'A1': 0.3, 'A2': 0},
    {'name': 'Caso ii) xA0=1.3m, xB0=1.7m', 'xA0': 1.3, 'xB0': 1.7, 'A1': 0, 'A2': 0.3},
    {'name': 'Caso iii) xA0=1.3m, xB0=1.9m', 'xA0': 1.3, 'xB0': 1.9, 'A1': 0.1, 'A2': 0.2}
]

plt.figure(figsize=(15, 10))

for i, case in enumerate(cases):
    xA_analytical, xB_analytical = analytical_solution(t, case['A1'], 0, case['A2'], 0)
    
    xA_numerical, xB_numerical = numerical_solution(case['xA0'], case['xB0'], 0, 0, t)
    
    plt.subplot(3, 1, i+1)
    
    # Plot corpo A
    plt.plot(t, xA_analytical, 'b-', label='A numérico')
    plt.plot(t, xA_numerical, 'b--', label='A analítico')
    
    # Plot corpo B
    plt.plot(t, xB_analytical, 'r-', label='B numérico')
    plt.plot(t, xB_numerical, 'r--', label='B analitico')
    
    plt.title(case['name'])
    plt.ylabel('Posição (m)')
    plt.xlabel('Tempo (s)')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()