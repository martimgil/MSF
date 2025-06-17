import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos
g = 9.81  # aceleração da gravidade (m/s²)
L = 1.0   # comprimento do fio (m)
T0 = 2*np.pi*np.sqrt(L/g)  # Período para pequenos ângulos

# Método de Euler melhorado (para maior precisão no cálculo do período)
def solve_pendulum_euler(theta0_deg, t_max=10, dt=0.001):
    theta0 = np.radians(theta0_deg)
    omega0 = 0.0  # velocidade angular inicial
    
    t = np.arange(0, t_max, dt)
    theta = np.zeros_like(t)
    omega = np.zeros_like(t)
    
    theta[0] = theta0
    omega[0] = omega0
    
    for i in range(1, len(t)):
        alpha = -(g/L) * np.sin(theta[i-1])
        omega[i] = omega[i-1] + alpha * dt
        theta[i] = theta[i-1] + omega[i] * dt  # Euler-Cromer (melhor para energia)
    
    return t, theta

# Função para calcular o período
def calculate_period(t, theta):
    # Encontra os cruzamentos por zero (mudanças de sinal)
    zero_crossings = np.where(np.diff(np.sign(theta)))[0]
    
    # Calcula os tempos entre cruzamentos
    if len(zero_crossings) < 2:
        return None
    
    # Pega os tempos de cruzamento (interpola para maior precisão)
    crossing_times = []
    for i in zero_crossings:
        t1, t2 = t[i], t[i+1]
        theta1, theta2 = theta[i], theta[i+1]
        # Interpolação linear para encontrar o tempo exato do cruzamento
        tc = t1 - theta1*(t2-t1)/(theta2-theta1)
        crossing_times.append(tc)
    
    # Calcula os períodos (intervalo entre dois cruzamentos do mesmo tipo)
    periods = []
    for i in range(0, len(crossing_times)-2, 2):
        periods.append(crossing_times[i+2] - crossing_times[i])
    
    return np.mean(periods) if periods else None

# Ângulos iniciais para simulação
angles_deg = [5, 10, 20, 30]
colors = ['b', 'g', 'r', 'c']

# Resultados
periods = []
T_ratios = []

# Plot configuração
plt.figure(figsize=(12, 8))
plt.suptitle('Análise do Período do Pêndulo Simples', y=1.02)

# Gráfico 1: Movimento angular
plt.subplot(2, 1, 1)
plt.title('Movimento Angular')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (graus)')
plt.grid(True)

# Gráfico 2: Período em função do ângulo
plt.subplot(2, 1, 2)
plt.title('Variação do Período com a Amplitude')
plt.xlabel('Ângulo Inicial (graus)')
plt.ylabel('Período (s) / T₀')
plt.axhline(1, color='k', linestyle='--', label='Pequenos ângulos (T₀)')
plt.grid(True)

# Resolver para cada ângulo inicial
for angle, color in zip(angles_deg, colors):
    t, theta = solve_pendulum_euler(angle, t_max=10, dt=0.001)
    period = calculate_period(t, theta)
    
    if period is not None:
        periods.append(period)
        T_ratio = period/T0
        T_ratios.append(T_ratio)
        print(f"Ângulo inicial: {angle}° | Período: {period:.4f} s | T/T₀: {T_ratio:.4f}")
        
        # Plot movimento
        plt.subplot(2, 1, 1)
        plt.plot(t, np.degrees(theta), color, label=f'θ₀ = {angle}°')
        
        # Plot período
        plt.subplot(2, 1, 2)
        plt.plot(angle, T_ratio, 'o', color=color, markersize=8)

# Linha teórica para comparação (aproximação mais precisa)
theta_max = np.radians(np.linspace(5, 30, 50))
T_approx = T0 * (1 + (1/16)*theta_max**2)  # Aproximação de segunda ordem
plt.subplot(2, 1, 2)
plt.plot(np.degrees(theta_max), T_approx/T0, 'k-', label='Aproximação teórica')

# Finalizar gráficos
plt.subplot(2, 1, 1)
plt.legend()
plt.subplot(2, 1, 2)
plt.legend()
plt.tight_layout()
plt.show()