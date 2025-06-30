#Martim Gil 124833
#Exercicio 2

import numpy as np
import matplotlib.pyplot as plt

k = 2.0
k_prime = 0.5
m = 1.0
xA_eq=0
xB_eq = 0

def derivatives(y):
    xA, vA, xB, vB = y

    F_A = -k*(xA - xA_eq) - k_prime*((xA-xA_eq)-(xB-xB_eq))
    F_B = -k_prime*(xB - xB_eq) - k*((xB - xB_eq)-(xA - xA_eq))

    aA = F_A / m
    aB = F_B / m

    return np.array([vA, aA, vB, aB])

def euler_integrate(y0,t,dt):
    n = len(t)
    y = np.zeros((n,4))
    y[0] = y0

    for i in range(1,n):
        y[i] = y[i-1] + dt * derivatives(y[i-1])
    return y

dt = 0.01
t_max = 30.0
t = np.arange(0, t_max, dt)

# Casos iniciais
cases = [
    {'name': 'Caso i)', 'xA0': xA_eq, 'xB0': xB_eq, 'vA0': 0.2, 'vB0': -0.3},
    {'name': 'Caso ii)', 'xA0': xA_eq , 'xB0': xB_eq, 'vA0': 0.2, 'vB0': -0.2},
    {'name': 'Caso iii)', 'xA0': xA_eq, 'xB0': xB_eq, 'vA0': 0.3, 'vB0': 0.3}
]

plt.figure(figsize=(15, 10))

for i, case in enumerate(cases):
    y0 = np.array([case['xA0'], case['vA0'], case['xB0'], case['vB0']])

    solution = euler_integrate(y0, t, dt)
    xA = solution[:, 0]
    xB = solution[:, 2]

    plt.subplot(3, 1, i + 1)
    plt.plot(t, xA, label='xA', color='blue')
    plt.plot(t, xB, label='xB', color='orange')
    plt.title(case['name'])
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

#b) Analise das caractericas do movimento dos osciladores acoplados:

print("Análise das características do movimento dos osciladores acoplados:")
print("Caso i): Neste caso, os osciladores apresentam um movimento oscilatório com frequências muito semelhantes, no entanto possuem amplitudes distintias, tendo o corpo B adquirido maior amplitude que o corpo A. Isso ocorre devido à diferença nas velocidades iniciais, onde o corpo B inicia com uma velocidade negativa maior que a do corpo A, resultando em um movimento oscilatório mais amplo para o corpo B. Além disso, estes movimenta-se em sentidos opostos. Ou seja adquitem um modo anti-simetrico, ou seja em oposição de fase.")
print("Caso ii): Semelhante ao caso i), ou seja, os osciladores apresentam um movimento oscilatório com frequências muito semelhantes, no entanto possuem amplitudes distintias, tendo o corpo B adquirido maior amplitude que o corpo A. Isso ocorre devido à diferença nas velocidades iniciais, apesar de ambas serem iguais em modulo, a velocidade do corpo B é negativa, resultando em um movimento oscilatório mais amplo para o corpo B. Além disso, estes movimenta-se em sentidos opostos. Ou seja adquitem um modo anti-simetrico, portanto em oposição de fase.")
print("Caso iii): Neste caso, os osciladores apresentam um movimento oscilatório com frequências muito semelhantes, no entanto possuem amplitudes semelhantes, tendo ambos os corpos adquirido amplitudes semelhantes. Isso ocorre devido à igualdade das velocidades iniciais, onde ambos os corpos iniciam com a mesma velocidade positiva, resultando em um movimento oscilatório mais amplo para ambos os corpos. Além disso, estes movimenta-se em sentidos iguais. Ou seja adquitem um modo simetrico, portanto em fase.")