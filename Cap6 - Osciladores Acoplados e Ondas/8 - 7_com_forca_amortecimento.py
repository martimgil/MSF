import numpy as np
import matplotlib.pyplot as plt

# Parâmetros constantes do sistema
k = 1.0
k_prime = 0.5
m = 1.0
b = 0.05
F0 = 0.005
x_Aeq = 1.0
x_Beq = 1.2

# ==============================================
# PARTE A) - SIMULAÇÃO PARA ω_f = 1 rad/s
# ==============================================

def simulate(omega_f, t_max=150, dt=0.1):
    """Função que realiza a simulação para um dado omega_f"""
    n_steps = int(t_max/dt)
    time = np.linspace(0, t_max, n_steps)
    

    # Condições iniciais (parte a)
    x_A = np.zeros(n_steps)
    x_B = np.zeros(n_steps)
    v_A = np.zeros(n_steps)
    v_B = np.zeros(n_steps)
    
    x_A[0] = x_Aeq + 0.05
    x_B[0] = x_Beq + 0.05
    v_A[0] = 0.0
    v_B[0] = 0.0

    # Funções de aceleração
    def acc_A(x_A, x_B, v_A, t):
        return (-k*(x_A-x_Aeq) - k_prime*((x_A-x_Aeq)-(x_B-x_Beq)) - b*v_A + F0*np.cos(omega_f*t))/m
    
    def acc_B(x_A, x_B, v_B, t):
        return (-k*(x_B-x_Beq) - k_prime*((x_B-x_Beq)-(x_A-x_Aeq)) - b*v_B)/m

    # Integração com Euler
    for i in range(1, n_steps):
        t = time[i-1]
        a_A = acc_A(x_A[i-1], x_B[i-1], v_A[i-1], t)
        a_B = acc_B(x_A[i-1], x_B[i-1], v_B[i-1], t)
        
        v_A[i] = v_A[i-1] + a_A*dt
        v_B[i] = v_B[i-1] + a_B*dt
        
        x_A[i] = x_A[i-1] + v_A[i-1]*dt
        x_B[i] = x_B[i-1] + v_B[i-1]*dt
    
    return time, x_A, x_B

# Simulação para parte a)
omega_f_a = 1.0  # rad/s
time_a, x_A_a, x_B_a = simulate(omega_f_a)

# Gráfico para parte a)
plt.figure(figsize=(12, 6))
plt.plot(time_a, x_A_a, label='Corpo A')
plt.plot(time_a, x_B_a, label='Corpo B')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title(f'Parte a) Movimento dos corpos para ω_f = {omega_f_a} rad/s')
plt.legend()
plt.grid(True)
plt.show()

# ==============================================
# PARTE B) - ANÁLISE DE AMPLITUDE VS FREQUÊNCIA
# ==============================================

# Variamos omega_f de 0 a 2.5 rad/s
omega_f_values = np.linspace(0, 2.5, 50)
amplitudes_A = []
amplitudes_B = []

for omega_f in omega_f_values:
    # Simulamos por tempo suficiente para atingir regime estável
    time, x_A, x_B = simulate(omega_f, t_max=300)
    
    # Ignoramos os primeiros 100s (transiente)
    steady_state = time > 100
    x_A_steady = x_A[steady_state]
    x_B_steady = x_B[steady_state]
    
    # Calculamos a amplitude no regime estacionário
    amp_A = (np.max(x_A_steady) - np.min(x_A_steady))/2
    amp_B = (np.max(x_B_steady) - np.min(x_B_steady))/2
    
    amplitudes_A.append(amp_A)
    amplitudes_B.append(amp_B)

# Gráfico para parte b)
plt.figure(figsize=(12, 6))
plt.plot(omega_f_values, amplitudes_A, 'o-', label='Corpo A')
plt.plot(omega_f_values, amplitudes_B, 'o-', label='Corpo B')
plt.xlabel('Frequência de forçamento ω_f (rad/s)')
plt.ylabel('Amplitude de oscilação (m)')
plt.title('Parte b) Resposta em amplitude vs frequência de forçamento')
plt.legend()
plt.grid(True)
plt.show()

# ==============================================
# ANÁLISE DOS RESULTADOS - OBSERVAÇÕES
# ==============================================
print("Observações para a parte b):")
print("1. Podemos observar picos de ressonância em determinadas frequências")
print("2. O corpo A (que recebe o forçamento) tem amplitudes maiores que o B")
print("3. O sistema apresenta duas frequências de ressonância distintas")
print("4. Para ω_f próximo de zero, a amplitude é aproximadamente F0/(k + k_prime)")
print("5. Quando ω_f aumenta muito, as amplitudes tendem a zero")