import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# Exercício 1: Oscilador Acoplado - Solução Numérica
# ==================================================

# Parâmetros do sistema
k = 1.0  # Constante elástica das molas externas [N/m]
k_prime = 0.5  # Constante elástica da mola de acoplamento [N/m]
m = 1.0  # Massa dos corpos [kg]
x_A_eq = 1.0  # Posição de equilíbrio do corpo A [m]
x_B_eq = 2.0  # Posição de equilíbrio do corpo B [m]

# Configuração temporal
t_max = 30.0  # Tempo máximo de simulação [s]
dt = 0.01  # Passo de tempo [s]
steps = int(t_max / dt)
t = np.linspace(0, t_max, steps)

# Função para resolver numericamente os osciladores acoplados
def solve_coupled_oscillators(xA0, xB0, vA0, vB0):
    xA = np.zeros(steps)
    xB = np.zeros(steps)
    vA = np.zeros(steps)
    vB = np.zeros(steps)
    
    # Condições iniciais
    xA[0] = xA0
    xB[0] = xB0
    vA[0] = vA0
    vB[0] = vB0
    
    # Integração numérica (método de Euler)
    for i in range(1, steps):
        # Forças atuantes
        F_A = -k*(xA[i-1] - x_A_eq) - k_prime*(xA[i-1] - xB[i-1])
        F_B = -k*(xB[i-1] - x_B_eq) + k_prime*(xA[i-1] - xB[i-1])
        
        # Acelerações
        aA = F_A / m
        aB = F_B / m
        
        # Atualização de velocidades e posições
        vA[i] = vA[i-1] + aA * dt
        vB[i] = vB[i-1] + aB * dt
        xA[i] = xA[i-1] + vA[i-1] * dt
        xB[i] = xB[i-1] + vB[i-1] * dt
    
    return xA, xB

# ==================================================
# Exercício 2: Solução Teórica e Análise de Fourier
# ==================================================

# Frequências angulares dos modos normais
omega1 = np.sqrt(k/m)  # Modo simétrico
omega2 = np.sqrt((k + 2*k_prime)/m)  # Modo antissimétrico

# Solução teórica
def theoretical_solution(t, A1, A2, phi1, phi2):
    xA = x_A_eq + A1*np.cos(omega1*t + phi1) + A2*np.cos(omega2*t + phi2)
    xB = x_B_eq + A1*np.cos(omega1*t + phi1) - A2*np.cos(omega2*t + phi2)
    return xA, xB

# Função para cálculo dos coeficientes de Fourier
def abfourier(tp, xp, it0, it1, nf):
    dt = tp[1] - tp[0]
    per = tp[it1] - tp[it0]
    ome = 2*np.pi/per

    s1 = xp[it0]*np.cos(nf*ome*tp[it0])
    s2 = xp[it1]*np.cos(nf*ome*tp[it1])
    st = xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma = np.sum(st)
    
    q1 = xp[it0]*np.sin(nf*ome*tp[it0])
    q2 = xp[it1]*np.sin(nf*ome*tp[it1])
    qt = xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq = np.sum(qt)
    
    intega = ((s1+s2)/2 + soma)*dt
    af = 2/per*intega
    integq = ((q1+q2)/2 + somq)*dt
    bf = 2/per*integq
    return af, bf

# Configuração para análise de Fourier
T = 100.0  # Período para análise de Fourier [s]
dt_fourier = 0.1  # Passo de tempo para Fourier [s]
t_fourier = np.arange(0, T, dt_fourier)
it0 = 0
it1 = len(t_fourier) - 1
n_max = 30  # Número máximo de coeficientes de Fourier

# Função para calcular e plotar coeficientes de Fourier
def plot_fourier_coefficients(t, x, title):
    a_n = np.zeros(n_max)
    b_n = np.zeros(n_max)
    omega_n = np.zeros(n_max)
    
    for n in range(1, n_max+1):
        a_n[n-1], b_n[n-1] = abfourier(t, x, it0, it1, n)
        omega_n[n-1] = n * (2*np.pi/T)
    
    plt.figure(figsize=(12, 6))
    plt.stem(omega_n, a_n, 'b', markerfmt='bo', label='$a_n$')
    plt.stem(omega_n, b_n, 'r', markerfmt='ro', label='$b_n$')
    plt.title(title)
    plt.xlabel('$\omega_n$ [rad/s]')
    plt.ylabel('Coeficientes de Fourier')
    plt.legend()
    plt.grid()
    plt.show()

# ==================================================
# Caso i) Deslocamentos iniciais iguais
# ==================================================

# Condições iniciais
xA0_i = x_A_eq + 0.3
xB0_i = x_B_eq + 0.3
vA0_i = 0
vB0_i = 0

# Solução teórica (apenas modo simétrico)
A1_i = 0.3
A2_i = 0.0
xA_theo_i, xB_theo_i = theoretical_solution(t, A1_i, A2_i, 0, 0)

# Solução numérica
xA_num_i, xB_num_i = solve_coupled_oscillators(xA0_i, xB0_i, vA0_i, vB0_i)

# Plot comparativo
plt.figure(figsize=(12, 6))
plt.plot(t, xA_num_i, 'b-', label='Numérico A')
plt.plot(t, xB_num_i, 'r-', label='Numérico B')
plt.plot(t, xA_theo_i, 'b--', label='Teórico A')
plt.plot(t, xB_theo_i, 'r--', label='Teórico B')
plt.title('Caso i) Deslocamentos iguais (+0.3 m em ambos)')
plt.xlabel('Tempo [s]')
plt.ylabel('Posição [m]')
plt.legend()
plt.grid()
plt.show()

# Análise de Fourier
plot_fourier_coefficients(t_fourier, xA_num_i[:len(t_fourier)], 
                         'Caso i) Coef. Fourier para xA (deslocamentos iguais)')
plot_fourier_coefficients(t_fourier, xB_num_i[:len(t_fourier)], 
                         'Caso i) Coef. Fourier para xB (deslocamentos iguais)')

# ==================================================
# Caso ii) Deslocamentos iniciais opostos
# ==================================================

# Condições iniciais
xA0_ii = x_A_eq + 0.3
xB0_ii = x_B_eq - 0.3
vA0_ii = 0
vB0_ii = 0

# Solução teórica (apenas modo antissimétrico)
A1_ii = 0.0
A2_ii = 0.3
xA_theo_ii, xB_theo_ii = theoretical_solution(t, A1_ii, A2_ii, 0, 0)

# Solução numérica
xA_num_ii, xB_num_ii = solve_coupled_oscillators(xA0_ii, xB0_ii, vA0_ii, vB0_ii)

# Plot comparativo
plt.figure(figsize=(12, 6))
plt.plot(t, xA_num_ii, 'b-', label='Numérico A')
plt.plot(t, xB_num_ii, 'r-', label='Numérico B')
plt.plot(t, xA_theo_ii, 'b--', label='Teórico A')
plt.plot(t, xB_theo_ii, 'r--', label='Teórico B')
plt.title('Caso ii) Deslocamentos opostos (+0.3 m e -0.3 m)')
plt.xlabel('Tempo [s]')
plt.ylabel('Posição [m]')
plt.legend()
plt.grid()
plt.show()

# Análise de Fourier
plot_fourier_coefficients(t_fourier, xA_num_ii[:len(t_fourier)], 
                         'Caso ii) Coef. Fourier para xA (deslocamentos opostos)')
plot_fourier_coefficients(t_fourier, xB_num_ii[:len(t_fourier)], 
                         'Caso ii) Coef. Fourier para xB (deslocamentos opostos)')

# ==================================================
# Caso iii) Deslocamentos iniciais diferentes
# ==================================================

# Condições iniciais
xA0_iii = x_A_eq + 0.3
xB0_iii = x_B_eq - 0.1
vA0_iii = 0
vB0_iii = 0

# Solução teórica (ambos os modos)
A1_iii = 0.1  # (0.3 + (-0.1))/2
A2_iii = 0.2  # (0.3 - (-0.1))/2
xA_theo_iii, xB_theo_iii = theoretical_solution(t, A1_iii, A2_iii, 0, 0)

# Solução numérica
xA_num_iii, xB_num_iii = solve_coupled_oscillators(xA0_iii, xB0_iii, vA0_iii, vB0_iii)

# Plot comparativo
plt.figure(figsize=(12, 6))
plt.plot(t, xA_num_iii, 'b-', label='Numérico A')
plt.plot(t, xB_num_iii, 'r-', label='Numérico B')
plt.plot(t, xA_theo_iii, 'b--', label='Teórico A')
plt.plot(t, xB_theo_iii, 'r--', label='Teórico B')
plt.title('Caso iii) Deslocamentos diferentes (+0.3 m e -0.1 m)')
plt.xlabel('Tempo [s]')
plt.ylabel('Posição [m]')
plt.legend()
plt.grid()
plt.show()

# Análise de Fourier
plot_fourier_coefficients(t_fourier, xA_num_iii[:len(t_fourier)], 
                         'Caso iii) Coef. Fourier para xA (deslocamentos diferentes)')
plot_fourier_coefficients(t_fourier, xB_num_iii[:len(t_fourier)], 
                         'Caso iii) Coef. Fourier para xB (deslocamentos diferentes)')

# ==================================================
# Pergunta 1: Comportamento quando k' = 0
# ==================================================

# Simulação com k' = 0
k_prime_zero = 0.0

def solve_uncoupled_oscillators(xA0, xB0, vA0, vB0):
    xA = np.zeros(steps)
    xB = np.zeros(steps)
    vA = np.zeros(steps)
    vB = np.zeros(steps)
    
    xA[0] = xA0
    xB[0] = xB0
    vA[0] = vA0
    vB[0] = vB0
    
    for i in range(1, steps):
        F_A = -k*(xA[i-1] - x_A_eq)
        F_B = -k*(xB[i-1] - x_B_eq)
        
        aA = F_A / m
        aB = F_B / m
        
        vA[i] = vA[i-1] + aA * dt
        vB[i] = vB[i-1] + aB * dt
        xA[i] = xA[i-1] + vA[i-1] * dt
        xB[i] = xB[i-1] + vB[i-1] * dt
    
    return xA, xB

# Usando condições do caso iii para demonstração
xA_uncoupled, xB_uncoupled = solve_uncoupled_oscillators(xA0_iii, xB0_iii, vA0_iii, vB0_iii)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(t, xA_uncoupled, 'b-', label='Corpo A')
plt.plot(t, xB_uncoupled, 'r-', label='Corpo B')
plt.title('Movimento com k\' = 0 (osciladores não acoplados)')
plt.xlabel('Tempo [s]')
plt.ylabel('Posição [m]')
plt.legend()
plt.grid()
plt.show()