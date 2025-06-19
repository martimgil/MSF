import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
m = 1.0       # massa (kg)
k = 1.0       # constante elástica (N/m)
b = 0.05      # coeficiente de amortecimento (kg/s)
alpha = 1.0   # parâmetro não-linear (N/m^2)
F0 = 7.5      # amplitude da força externa (N)
wf = 1.0      # frequência da força externa (rad/s)

# Função que define as equações diferenciais
def derivadas(y, t):
    x, v = y
    dxdt = v
    dvdt = (-k*x*(1 + 2*alpha*x**2) - b*v + F0*np.cos(wf*t)) / m
    return np.array([dxdt, dvdt])

# Implementação do método de Runge-Kutta de 4ª ordem
def runge_kutta4(func, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    h = t[1] - t[0]
    
    for i in range(n-1):
        k1 = func(y[i], t[i])
        k2 = func(y[i] + 0.5*h*k1, t[i] + 0.5*h)
        k3 = func(y[i] + 0.5*h*k2, t[i] + 0.5*h)
        k4 = func(y[i] + h*k3, t[i] + h)
        y[i+1] = y[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    return y

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

# Configuração da simulação
t_max = 100.0  # tempo máximo de simulação (s)
dt = 0.01      # passo de tempo (s)
t = np.arange(0, t_max, dt)

# a) Resolução com x0 = 3 m, v0 = 0 m/s
y0_a = np.array([3.0, 0.0])
sol_a = runge_kutta4(derivadas, y0_a, t)
x_a, v_a = sol_a[:, 0], sol_a[:, 1]

# Gráfico da alínea a)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x_a)
plt.title('a) Lei do movimento - x0=3m, v0=0m/s')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x_a, v_a)
plt.title('Espaço de fase')
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.grid()
plt.tight_layout()
plt.show()

# b) Análise do regime estacionário (últimos 20% da simulação)
n_steady = int(0.8 * len(t))
x_steady = x_a[n_steady:]
v_steady = v_a[n_steady:]
t_steady = t[n_steady:]

# Encontrar amplitude (máximo e mínimo no regime estacionário)
amplitude_max = np.max(x_steady)
amplitude_min = np.min(x_steady)
print(f"b) Limites do movimento no regime estacionário: [{amplitude_min:.3f}, {amplitude_max:.3f}] m")

# Calcular período (encontrar picos)
zeros = np.where(np.diff(sign(np.diff(x_steady))) < 0)[0] + 1
periodos = np.diff(t_steady[zeros])
periodo_medio = np.mean(periodos)
print(f"Período médio no regime estacionário: {periodo_medio:.3f} s")

# Encontrar um período completo para análise de Fourier
it0 = 0
it1 = len(x_steady) - 1
for i in range(1, len(x_steady)):
    if abs(x_steady[i] - x_steady[0]) < 0.1 and v_steady[i] * v_steady[0] > 0:
        it1 = i
        break

# Calcular coeficientes de Fourier para as primeiras 5 harmônicas
print("\nCoeficientes de Fourier para o regime estacionário (caso a):")
for nf in range(5):
    af, bf = abfourier(t_steady, x_steady, 0, it1, nf)
    print(f"n={nf}: a_{nf} = {af:.4f}, b_{nf} = {bf:.4f}")

# Gráfico do regime estacionário
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t_steady, x_steady)
plt.title('b) Regime estacionário - movimento')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x_steady, v_steady)
plt.title('Espaço de fase no regime estacionário')
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.grid()
plt.tight_layout()
plt.show()

# c) Resolução com x0 = -3 m, v0 = -3 m/s
y0_c = np.array([-3.0, -3.0])
sol_c = runge_kutta4(derivadas, y0_c, t)
x_c, v_c = sol_c[:, 0], sol_c[:, 1]

# Gráfico da alínea c)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x_c)
plt.title('c) Lei do movimento - x0=-3m, v0=-3m/s')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x_c, v_c)
plt.title('Espaço de fase')
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.grid()
plt.tight_layout()
plt.show()

# d) Análise do regime estacionário para o caso c)
x_steady_c = x_c[n_steady:]
v_steady_c = v_c[n_steady:]
t_steady_c = t[n_steady:]

# Limites de movimento
amplitude_max_c = np.max(x_steady_c)
amplitude_min_c = np.min(x_steady_c)
print(f"\nd) Limites do movimento no regime estacionário (caso c): [{amplitude_min_c:.3f}, {amplitude_max_c:.3f}] m")

# Encontrar um período completo para análise de Fourier
it0_c = 0
it1_c = len(x_steady_c) - 1
for i in range(1, len(x_steady_c)):
    if abs(x_steady_c[i] - x_steady_c[0]) < 0.1 and v_steady_c[i] * v_steady_c[0] > 0:
        it1_c = i
        break

# Calcular coeficientes de Fourier para as primeiras 5 harmônicas
print("\nCoeficientes de Fourier para o regime estacionário (caso c):")
for nf in range(5):
    af, bf = abfourier(t_steady_c, x_steady_c, 0, it1_c, nf)
    print(f"n={nf}: a_{nf} = {af:.4f}, b_{nf} = {bf:.4f}")

# Reconstruir sinal com os coeficientes de Fourier
def reconstroi_sinal(t, af, bf, nf_max, periodo):
    ome = 2*np.pi/periodo
    sinal = np.zeros_like(t)
    for nf in range(nf_max + 1):
        sinal += af[nf] * np.cos(nf*ome*t) + bf[nf] * np.sin(nf*ome*t)
    return sinal

# Calcular todos os coeficientes para nf_max = 4
nf_max = 4
af_c = np.zeros(nf_max + 1)
bf_c = np.zeros(nf_max + 1)
for nf in range(nf_max + 1):
    af_c[nf], bf_c[nf] = abfourier(t_steady_c, x_steady_c, 0, it1_c, nf)

# Reconstruir sinal
periodo_c = t_steady_c[it1_c] - t_steady_c[0]
x_reconst = reconstroi_sinal(t_steady_c[:it1_c], af_c, bf_c, nf_max, periodo_c)

# Gráfico comparativo
plt.figure(figsize=(12, 4))
plt.plot(t_steady_c[:it1_c], x_steady_c[:it1_c], label='Sinal original')
plt.plot(t_steady_c[:it1_c], x_reconst, '--', label=f'Sinal reconstruído (até n={nf_max})')
plt.title('d) Comparação entre sinal original e reconstruído (caso c)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.grid()
plt.show()

# e) Cálculo da energia mecânica
def energia_mecanica(x, v):
    Ep = 0.5 * k * x**2 * (1 + alpha * x**2)
    Ec = 0.5 * m * v**2
    return Ep + Ec

# Energia para caso a)
E_a = energia_mecanica(x_a, v_a)

# Energia para regime estacionário do caso a)
E_steady = energia_mecanica(x_steady, v_steady)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(t, E_a)
plt.title('e) Energia mecânica - caso a)')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t_steady, E_steady)
plt.title('Energia no regime estacionário')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.grid()
plt.tight_layout()
plt.show()

# f) Análise dos resultados
print("\nf) Caracterização das soluções:")
print("- O sistema apresenta um regime transiente inicial que depende das condições iniciais")
print("- Após o transiente, o sistema converge para um regime estacionário periódico")
print("- A energia mecânica não é constante devido ao amortecimento e à força externa")
print("- O comportamento não-linear é evidente na forma do espaço de fase e nos coeficientes de Fourier")
print("- Os coeficientes de Fourier mostram a presença de múltiplas harmônicas devido à não-linearidade")