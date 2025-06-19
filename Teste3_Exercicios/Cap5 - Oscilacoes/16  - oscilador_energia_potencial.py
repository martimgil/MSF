import numpy as np
import matplotlib.pyplot as plt

k = 1.0
alpha = -0.01
m = 1.0

def Ep (x):
    return 0.5 * k * x**2 + alpha * x**4

def F(x):
    return -k*x-3*alpha*x**2

def euler_integration(x0, v0, dt=0.001, t_total=30):
    n_steps = int(t_total / dt)
    t = np.zeros(n_steps)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    # Condições iniciais
    t[0] = 0
    x[0] = x0
    v[0] = v0
    
    # Integração
    for i in range(1, n_steps):
        t[i] = t[i-1] + dt
        x[i] = x[i-1] + v[i-1] * dt
        v[i] = v[i-1] + F(x[i-1])/m * dt
    
    return t, x, v

def analyze_motion(t, x, v, case_label):
    """Análise do movimento e plot dos gráficos"""
    # Energia mecânica inicial
    E_initial = Ep(x[0]) + 0.5 * m * v[0]**2
    print(f"\n{case_label}) Energia mecânica inicial: {E_initial:.4f} J")
    
    # Pontos de retorno
    sign_changes = np.where(np.diff(np.sign(v)))[0]
    turning_points = x[sign_changes]
    if len(turning_points) > 0:
        x_min, x_max = min(turning_points), max(turning_points)
        print(f"Limites do movimento: {x_min:.4f} m a {x_max:.4f} m")
    else:
        print("Não foram encontrados pontos de retorno")
    
    # Frequência
    zero_crossings = np.where(np.diff(np.sign(x)))[0]
    if len(zero_crossings) > 1:
        periods = np.diff(t[zero_crossings])
        freq = 1 / np.mean(periods)
        print(f"Frequência aproximada: {freq:.4f} Hz")
    else:
        print("Não foram detectados ciclos completos")


# --------------------------------------------------
# Alínea a) Diagrama de energia e análise para E < 1 J
# --------------------------------------------------

print("\nAlínea a) ")

x_vals = np.linspace(-15, 15, 1000)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, Ep(x_vals), label='Energia Potencial $E_p(x)$')
plt.axhline(y=1, color='r', linestyle='--', label='E = 1 J')
plt.xlabel('Posição x (m)')
plt.ylabel('Energia (J)')
plt.title('Diagrama de Energia Potencial')
plt.grid(True)
plt.legend()
plt.show()

print("Quando a energia total for menor que 1 J, o movimento será limitado")
print("entre dois pontos de retorno onde a energia cinética se anula (E = Ep).")

# --------------------------------------------------
# Alínea b) x0 = 1.3 m, v0 = 0 m/s
# --------------------------------------------------

print("\n Alínea b) ")
t_b, x_b, v_b = euler_integration(x0=1.3, v0=0, t_total=20)
analyze_motion(t_b, x_b, v_b, "b")

# --------------------------------------------------
# Alínea c) x0 = 2.9 m, v0 = 0 m/s
# --------------------------------------------------

print("\n Alínea c) ")
t_c, x_c, v_c = euler_integration(x0=2.9, v0=0, t_total=30)
analyze_motion(t_c, x_c, v_c, "c")

# --------------------------------------------------
# Gráfico comparativo das duas situações
# --------------------------------------------------

plt.figure(figsize=(12, 6))
plt.plot(t_b, x_b, label='b) x0 = 1.3 m')
plt.plot(t_c[:len(t_b)], x_c[:len(t_b)], label='c) x0 = 2.9 m')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Comparação dos Movimentos')
plt.grid(True)
plt.legend()
plt.show()