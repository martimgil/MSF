import numpy as np
import matplotlib.pyplot as plt

# Dados
m = 1.0
k = 1.0
alpha = 0.002
b = 0.05
F0 = 7.5
wf = 1.0

x0_a = 3.0
v0_a = 0.0

t0 = 0.0
tf = 100.0
dt = 0.01
n = int((tf - t0) / dt) + 1
t = np.linspace(t0, tf, n)
x_a = np.zeros(n)
v_a = np.zeros(n)

x_a[0] = x0_a
v_a[0] = v0_a

for i in range(n-1):
    F = -k * x_a[i]*(1+2*alpha*x_a[i]**2) - b*v_a[i] + F0*np.cos(wf*t[i])
    a = F / m
    v_a[i+1] = v_a[i] + a * dt
    x_a[i+1] = x_a[i] + v_a[i] * dt

plt.figure(figsize=(12, 6))
plt.plot(t, x_a, label='Posição (x)', color='blue')
plt.title("Lei do movimento do oscilador quártico forçado e amortecido (x0=3m, v0=0m/s)")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.grid(True)
plt.show()

# Resolução com passo de tempo reduzido

dt_test = dt/2
n_test = int((tf - t0) / dt_test) + 1
t_test = np.linspace(t0, tf, n_test)
x_test = np.zeros(n_test)
v_test = np.zeros(n_test)
x_test[0] = x0_a
v_test[0] = v0_a

for i in range(n_test-1):
    F = -k * x_test[i]*(1+2*alpha*x_test[i]**2) - b*v_test[i] + F0*np.cos(wf*t_test[i])
    a = F / m
    v_test[i+1] = v_test[i] + a * dt_test
    x_test[i+1] = x_test[i] + v_test[i] * dt_test

x_a_interp = np.interp(t, t_test, x_test)
dif = np.max(np.abs(x_test - x_a_interp))
print(f"Máxima diferença entre os resultados com passo de tempo reduzido: {dif:.6f} m")
print(f"O resultado é confiavel se a diferença for pequena (<<1)")


#b)Calcular a amplitude e o periodo no regime estacionario

t_estacionario = t[t > 60]
x_estacionario = x_a[t > 60]
maximos = []
for i in range(1, len(x_estacionario)-1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        maximos.append(x_estacionario[i])

if maximos:
    amplitude = np.mean(maximos)
    print(f"Amplitude no regime estacionário: {amplitude:.2f} m")
else:
    print("Não foram encontrados máximos")

indices_maximos = []
for i in range(1, len(x_estacionario)-1):
    if x_estacionario[i] > x_estacionario[i-1] and x_estacionario[i] > x_estacionario[i+1]:
        indices_maximos.append(i)

if len(indices_maximos) > 1:
    periodos = np.diff(t_estacionario[indices_maximos])
    periodo = np.mean(periodos)
    print(f"Período no regime estacionário: {periodo:.2f} s")
    print(f"Frequência no regime estacionário: {1/periodo:.2f} Hz")
else:
    print("Não foram encontrados máximos suficientes para calcular o período")


#c) Lei do movimento com novas condições iniciais
x0_c=-2.0
v0_c=-4.0

x_c = np.zeros(n)
v_c = np.zeros(n)
x_c[0] = x0_c
v_c[0] = v0_c

for i in range(n-1):
    F = -k * x_c[i]*(1+2*alpha*x_c[i]**2) - b*v_c[i] + F0*np.cos(wf*t[i])
    a = F / m
    v_c[i+1] = v_c[i] + a * dt
    x_c[i+1] = x_c[i] + v_c[i] * dt

plt.figure(figsize=(12, 6))
plt.plot(t, x_c, label='Posição (x)', color='red')
plt.title("Lei do movimento do oscilador quártico forçado e amortecido (x0=-2m, v0=-4m/s)")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.grid(True)
plt.show()

#d) Calcular a amplitude e o periodo no regime estacionario

x_estacionario_c = x_c[t > 60]

maximos_c = []
for i in range(1, len(x_estacionario_c)-1):
    if x_estacionario_c[i] > x_estacionario_c[i-1] and x_estacionario_c[i] > x_estacionario_c[i+1]:
        maximos_c.append(x_estacionario_c[i])

if maximos_c:
    amplitude_c = np.mean(maximos_c)
    print(f"Amplitude no regime estacionário (condições iniciais x0={x0_c}, v0={v0_c}): {amplitude_c:.2f} m")
else:
    print("Não foram encontrados máximos para as novas condições iniciais")

indices_maximos_c = []
for i in range(1, len(x_estacionario_c)-1):
    if x_estacionario_c[i] > x_estacionario_c[i-1] and x_estacionario_c[i] > x_estacionario_c[i+1]:
        indices_maximos_c.append(i)

if len(indices_maximos_c) > 1:
    periodos_c = np.diff(t_estacionario[indices_maximos_c])
    periodo_c = np.mean(periodos_c)
    print(f"Período no regime estacionário (condições iniciais x0={x0_c}, v0={v0_c}): {periodo_c:.2f} s")
    print(f"Frequência no regime estacionário: {1/periodo_c:.2f} Hz")
else:
    print("Não foram encontrados máximos suficientes para calcular o período")

#e) Calculo da energia mecanica

Ep_a = 0.5 * k * x_a**2 * (1 + 2 * alpha * x_a**2)
Ec_a = 0.5 * m * v_a**2
Em_a = Ep_a + Ec_a

Ep_c = 0.5 * k * x_c**2 * (1 + 2 * alpha * x_c**2)
Ec_c = 0.5 * m * v_c**2
Em_c = Ep_c + Ec_c

plt.figure(figsize=(12, 6))
plt.plot(t, Em_a, label='Energia Mecânica (Em)', color='blue')
plt.plot(t, Em_c, label='Energia Mecânica (Em)', color='red')
plt.title("Energia Mecânica do Oscilador Quártico Forçado e Amortecido")
plt.xlabel("Tempo (s)")
plt.ylabel("Energia Mecânica (J)")
plt.legend()
plt.grid(True)
plt.show()

Em_a_est = Em_a[t > 60]
var_Em_a = (np.max(Em_a_est) - np.min(Em_a_est)) / np.mean(Em_a_est)
print(f"Variação relativa da energia mecânica no regime estacionário (x0=3m, v0=0m/s): {var_Em_a:.4f}")

Em_c_est = Em_c[t > 60]
var_Em_c = (np.max(Em_c_est) - np.min(Em_c_est)) / np.mean(Em_c_est)
print(f"Variação relativa da energia mecânica no regime estacionário (x0={x0_c}m, v0={v0_c}m/s): {var_Em_c:.4f}")
print("A energia mecânica no regime estacionário deve ser praticamente constante, portanto a variação relativa deve ser pequena (<<1).")


