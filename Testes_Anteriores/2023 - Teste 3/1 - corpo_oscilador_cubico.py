import numpy as np
import matplotlib.pyplot as plt

# Dados
m = 1.0  # massa (kg)
k = 1.0  # constante elástica (N/m)
a = 0.05 # coeficiente de não linearidade (N/m²)
x0 = -2  # posição inicial
v0 = 3   # velocidade inicial

# Energia potencial
def Ep(x):
    return 0.5 * k * x**2 + a * x**3

# Força
def F(x):
    return -k * x - 3 * a * x**2

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

# PARTE 1 – Diagrama de energia potencial
x_vals = np.linspace(-8, 4, 1000)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, Ep(x_vals), label='Energia Potencial', color='blue')
plt.axhline(y=7, color='red', linestyle='--', label='E = 7 J')
plt.axhline(y=8, color='green', linestyle='--', label='E = 8 J')
plt.xlabel('Posição x (m)')
plt.ylabel('Energia (J)')
plt.title('Diagrama de Energia Potencial do Oscilador Cúbico')
plt.grid(True)
plt.legend()
plt.show()

# PARTE 2 – Simulação e energia total
t, x, v = euler_integration(x0, v0, dt=0.01, t_total=30)

Ep_vals = np.array([Ep(xi) for xi in x])
Ec_vals = 0.5 * m * v**2
E_total = Ep_vals + Ec_vals

plt.figure(figsize=(10, 6))
plt.plot(t, E_total, label='Energia Total', color='green')
plt.axhline(y=8, color='red', linestyle='--', label='E = 8 J')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('Evolução da Energia Total do Sistema')
plt.grid(True)
plt.legend()
plt.show()


### b) Calcular a lei do movimvento 

x0 = 2.2
v0 = 0.0

t, x, v = euler_integration(x0, v0, dt=0.01, t_total=30)
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Posição x(t)', color='blue')
plt.plot(t, v, label='Velocidade v(t)', color='orange')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m) / Velocidade (m/s)')
plt.title('Movimento do Oscilador Cúbico')
plt.grid(True)
plt.legend()
plt.show()

Em = Ep(x) + 0.5 * m * v**2
plt.figure(figsize=(10, 6))
plt.plot(t, Em, label='Energia Mecânica', color='purple')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('Energia Mecânica do Oscilador Cúbico')
plt.grid(True)
plt.legend()
plt.show()

### c) Faça a analise de Fourier da solucao encontrada



def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf




# Define an interval of approximately one period
it0 = 1000  # t ≈ 10s
it1 = min(3000, len(t)-1)  # t ≈ 30s (2 periods approx.), ensure within bounds
N = 30      # number of harmonics

harmonics = np.arange(1, N+1)
amplitudes = []

for n in harmonics:
    a_n, b_n = abfourier(t, x, it0, it1, n)
    amp = np.sqrt(a_n**2 + b_n**2)
    amplitudes.append(amp)

plt.figure(figsize=(10, 6))
plt.stem(harmonics, amplitudes, use_line_collection=True)
plt.xlabel('n (harmonic)')
plt.ylabel('Amplitude')
plt.title('Fourier Spectrum of Position x(t)')
plt.grid(True)
plt.show()