import numpy as np
import function_lagrange as lag
import matplotlib.pyplot as plt

def calculate_period(L, theta0=0.1, dt=0.001, tf=10.0):
    """Calcula o período do pêndulo para um dado comprimento L"""
    t = np.arange(0, tf, dt)
    theta = np.zeros_like(t)
    theta[0] = theta0
    v = 0.0
    
    for i in range(1, len(t)):
        v = v - (9.8/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + v * dt
    
    # Deteção de máximos
    max_times = []
    for i in range(1, len(theta)-1):
        if theta[i] > theta[i-1] and theta[i] > theta[i+1]:
            t_max, _ = lag.maxminv(t[i-1], t[i], t[i+1], 
                                 theta[i-1], theta[i], theta[i+1])
            max_times.append(t_max)
            if len(max_times) == 2:  
                break
    
    return max_times[1] - max_times[0] if len(max_times) >= 2 else None

# Valores de L para testar (de 0.2m a 2m)
L_values = np.linspace(0.2, 2.0, 15)
periods = []

for L in L_values:
    T = calculate_period(L)
    if T is not None:
        periods.append(T)
    else:
        periods.append(np.nan)

# Transformação logarítmica
log_L = np.log10(L_values)
log_T = np.log10(periods)

# Implementação manual do ajuste linear (mínimos quadrados)
def linear(x, y):
    """Implementação manual de mínimos quadrados para y = a*x + b"""
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x*y)
    sum_x2 = np.sum(x**2)
    
    a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    b = (sum_y - a*sum_x) / n
    
    y_pred = a*x + b
    residuals = y - y_pred
    std_err = np.sqrt(np.sum(residuals**2)/(n-2))
    a_err = std_err * np.sqrt(n/(n*sum_x2 - sum_x**2))
    
    return a, b, a_err

# Ajuste linear
a, b, a_err = linear(log_L, log_T)

# Gerar pontos para a reta de ajuste
log_L_fit = np.array([min(log_L), max(log_L)])
log_T_fit = a*log_L_fit + b

# Gráfico log-log
plt.figure(figsize=(10, 6))
plt.scatter(log_L, log_T, label='Dados simulados', color='blue')
plt.plot(log_L_fit, log_T_fit, 'r--', 
         label=f'Ajuste linear: log T = {a:.3f}±{a_err:.3f} log L + {b:.3f}')
plt.xlabel('log(L) [log(m)]')
plt.ylabel('log(T) [log(s)]')
plt.title('Relação entre o Período e o Comprimento do Pêndulo')
plt.grid(True, which="both", ls="-")
plt.legend()
plt.show()

# Resultados
print("\nResultados do ajuste linear (implementação manual):")
print(f"Declive (a) = {a:.4f} ± {a_err:.4f}")
print(f"Ordenada na origem (b) = {b:.4f}")
