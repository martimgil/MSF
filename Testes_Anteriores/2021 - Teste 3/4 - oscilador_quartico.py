import numpy as np
import matplotlib.pyplot as plt

# Constantes do problema
m = 1.5  # kg
k = 1.2  # N/m
alpha = -0.01  # N/m^2

# a) Diagrama de energia potencial
def Ep(x):
    return 0.5 * k * x**2 + alpha * x**3

x_vals = np.linspace(-10, 10, 1000) 
Ep_vals = Ep(x_vals)

plt.figure()
plt.plot(x_vals, Ep_vals, label="Energia Potencial $E_p(x)$")
plt.axhline(2, color='red', linestyle='--', label="Energia Total = 2 J")  
plt.title("Energia Potencial vs Posição")
plt.xlabel("Posição (m)")
plt.ylabel("Energia Potencial (J)")
plt.legend()
plt.grid(True)
plt.show()

# b) Lei do movimento com Euler 
x0 = 3.5
v0 = 2.0

def F(x):
    return -k * x - 3 * alpha * x**2

def euler_integration(x0, v0, dt=0.001, t_total=30):  
    n_steps = int(t_total / dt)
    t = np.zeros(n_steps)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    t[0] = 0
    x[0] = x0
    v[0] = v0
    
    for i in range(1, n_steps):
        t[i] = t[i-1] + dt
        x[i] = x[i-1] + v[i-1] * dt
        v[i] = v[i-1] + F(x[i-1])/m * dt
    
    return t, x, v

t, x, v = euler_integration(x0, v0, dt=0.001, t_total=30)

# Gráfico da posição x(t)
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Posição x(t)', color='blue')
plt.title("Lei do Movimento (Euler)")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.grid(True)
plt.legend()
plt.show()

Em = 0.5 * m * v**2 + Ep(x)
plt.figure()
plt.plot(t, Em, label='Energia Mecânica', color='green')
plt.axhline(Em[0], color='red', linestyle='--', label='Energia Inicial')
plt.title("Conservação de Energia")
plt.xlabel("Tempo (s)")
plt.ylabel("Energia (J)")
plt.legend()
plt.grid(True)
plt.show()

# Limites do movimento 
Em_total = Em[0]
print(f"Energia mecânica total: {Em_total:.4f} J")

def encontrar_limites(Ep_vals, x_vals, Em_total):
    limites = []
    for i in range(1, len(Ep_vals)):
        if (Ep_vals[i-1] - Em_total) * (Ep_vals[i] - Em_total) < 0:
            x1, x2 = x_vals[i-1], x_vals[i]
            y1, y2 = Ep_vals[i-1], Ep_vals[i]
            x_cruz = x1 + (Em_total - y1) * (x2 - x1) / (y2 - y1)
            limites.append(x_cruz)
    return sorted(limites) if limites else None

limites = encontrar_limites(Ep_vals, x_vals, Em_total)
if limites:
    x_min, x_max = limites[0], limites[-1]
    print(f"Limites do movimento: x ∈ [{x_min:.4f}, {x_max:.4f}]")
else:
    print("Não foram encontrados pontos de retorno.")

# Período e frequência 
def detectar_cruzamentos_zero(t, x):
    cruzamentos = []
    for i in range(1, len(x)):
        if x[i-1] * x[i] < 0:  # Mudança de sinal
            t_cruz = t[i-1] - x[i-1] * (t[i] - t[i-1]) / (x[i] - x[i-1])
            cruzamentos.append(t_cruz)
    return cruzamentos

cruzamentos = detectar_cruzamentos_zero(t, x)
if len(cruzamentos) >= 2:
    T = cruzamentos[1] - cruzamentos[0]
    f = 1 / T
    print(f"Período estimado: T = {T:.4f} s")
    print(f"Frequência estimada: f = {f:.4f} Hz")
else:
    print("Não foram detectados cruzamentos suficientes.")

# c) Análise de Fourier 
def abfourier(tp, xp, it0, it1, nf):
    dt = tp[1] - tp[0]
    per = tp[it1] - tp[it0]
    ome = 2 * np.pi / per

    s1 = xp[it0] * np.cos(nf * ome * tp[it0])
    s2 = xp[it1] * np.cos(nf * ome * tp[it1])
    st = xp[it0+1:it1] * np.cos(nf * ome * tp[it0+1:it1])
    soma = np.sum(st)

    q1 = xp[it0] * np.sin(nf * ome * tp[it0])
    q2 = xp[it1] * np.sin(nf * ome * tp[it1])
    qt = xp[it0+1:it1] * np.sin(nf * ome * tp[it0+1:it1])
    somq = np.sum(qt)

    intega = ((s1 + s2) / 2 + soma) * dt
    af = 2 / per * intega
    integq = ((q1 + q2) / 2 + somq) * dt
    bf = 2 / per * integq
    return af, bf

if len(cruzamentos) >= 2:
    it0 = np.argmin(np.abs(t - cruzamentos[0]))
    it1 = np.argmin(np.abs(t - cruzamentos[1]))
    
    print("\nAnálise de Fourier:")
    for n in range(1, 6):
        a_n, b_n = abfourier(t, x, it0, it1, n)
        magnitude = np.sqrt(a_n**2 + b_n**2)
        print(f"n = {n}: |a_n + ib_n| = {magnitude:.4f}")
else:
    print("Não há dados suficientes para Fourier.")