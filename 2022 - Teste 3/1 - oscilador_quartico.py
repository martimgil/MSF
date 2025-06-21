import numpy as np
import matplotlib.pyplot as plt

# Constantes do problema
m = 0.5  # kg
k = 2  # N/m
a = -0.1  # N/m^2
alpha = -0.1  # N/m^2
beta = 0.02  # N/m^3

# Potencial em função da posição
def Ep(x):
    return 0.5 * k * x**2 + alpha * x**3 - beta * x**4

# Intervalo de x para plotagem
x_vals = np.linspace(-3, 3, 1000)
Ep_vals = Ep(x_vals)

plt.figure()
plt.plot(x_vals, Ep_vals, label="Energia Potencial $E_p(x)$")
plt.axhline(4, color='red', linestyle='--', label="Energia Total = 4 J")
plt.title("Energia Potencial vs Posição")
plt.xlabel("Posição (m)")
plt.ylabel("Energia Potencial (J)")
plt.legend()
plt.grid(True)
plt.show()

#b) Calcular a lei do movimento
x0 = 1.5
v0 = 0.5

def F(x):
    return -k * x - 3 * alpha * x**2 + 4 * beta * x**3

# Integração de Euler
def euler_integration(x0, v0, dt=0.01, t_total=30):
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

plt.figure(figsize=(10, 6))
t, x, v = euler_integration(x0, v0, dt=0.01, t_total=30)
plt.plot(t, x, label='Posição x(t)', color='blue')
plt.title("Lei do Movimento do Oscilador Quártico")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.grid(True)
plt.legend()
plt.show()

Em = 0.5 * m * v**2 + Ep(x)
plt.plot(t, Em, label='Energia Mecânica', color='green')

plt.title("Energia Mecânica do Oscilador Quártico")
plt.show()

# Limite se efetua o movimento e a frequencia e o periodo do movimento.

Em_total = 0.5 * m * v0**2 + Ep(x0)

def encontrar_limites(Ep_vals, x_vals, Em_total):
    limites = []
    for i in range(1, len(Ep_vals)):
        if (Ep_vals[i-1] - Em_total) * (Ep_vals[i] - Em_total) < 0:
            # Há uma mudança de sinal, cruzou Em_total
            # Interpolação linear para estimar o ponto exato
            x1, x2 = x_vals[i-1], x_vals[i]
            y1, y2 = Ep_vals[i-1], Ep_vals[i]
            x_cruzamento = x1 + (Em_total - y1) * (x2 - x1) / (y2 - y1)
            limites.append(x_cruzamento)
    return limites


limites = encontrar_limites(Ep_vals, x_vals, Em_total)
x_min, x_max = min(limites), max(limites)
print(f"Limites do movimento: x ∈ [{x_min:.4f}, {x_max:.4f}]")

# Estimar o período detectando os picos de x(t) manualmente
def detectar_picos(x, t):
    picos_tempo = []
    for i in range(1, len(x)-1):
        if x[i-1] < x[i] > x[i+1]:
            picos_tempo.append(t[i])
    return picos_tempo

tempos_pico = detectar_picos(x, t)
if len(tempos_pico) >= 2:
    T = tempos_pico[1] - tempos_pico[0]
    f = 1 / T
    print(f"Período estimado: T = {T:.4f} s")
    print(f"Frequência estimada: f = {f:.4f} Hz")
else:
    print("Não foi possível detectar dois picos para estimar o período.")

#d) Analise de Fourier

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

# Identificar os índices correspondentes a um período completo
tempos_pico = detectar_picos(x, t)
if len(tempos_pico) >= 2:
    # tempo do primeiro e segundo pico
    t0 = tempos_pico[0]
    t1 = tempos_pico[1]
    
    # encontrar os índices correspondentes
    it0 = np.argmin(np.abs(t - t0))
    it1 = np.argmin(np.abs(t - t1))

    # Número de harmônicos a calcular
    N_harm = 5
    magnitudes = []

    print("Harmônicos de Fourier:")
    for n in range(1, N_harm + 1):
        a_n, b_n = abfourier(t, x, it0, it1, n)
        magnitude = np.sqrt(a_n**2 + b_n**2)
        magnitudes.append(magnitude)
        print(f"n = {n}: sqrt(a_n² + b_n²) = {magnitude:.4f}")
else:
    print("Não há picos suficientes para realizar a análise de Fourier.")
