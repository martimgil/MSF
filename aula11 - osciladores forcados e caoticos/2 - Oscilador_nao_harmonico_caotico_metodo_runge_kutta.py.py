import numpy as np
import matplotlib.pyplot as plt

k = 0.2
alpha = 1.0
b = 0.01
F0 = 5.0
omega_f = 0.6

def aceleracao(t, x, vx):
    return -k*x - 4*alpha*x**3 - b*vx + F0*np.cos(omega_f*t)

def rk4_x_vx(t, x, vx, acelera, dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
    d2x/dt2 = ax(t,x,vx), com dx/dt= vx.
    Erro global proporcional a dt**4.
    """
    ax1 = acelera(t, x, vx)
    c1v = ax1 * dt
    c1x = vx * dt

    ax2 = acelera(t + dt/2., x + c1x/2., vx + c1v/2.)
    c2v = ax2 * dt
    c2x = (vx + c1v/2.) * dt

    ax3 = acelera(t + dt/2., x + c2x/2., vx + c2v/2.)
    c3v = ax3 * dt
    c3x = (vx + c2v/2.) * dt

    ax4 = acelera(t + dt, x + c3x, vx + c3v)
    c4v = ax4 * dt
    c4x = (vx + c3v) * dt

    xp = x + (c1x + 2*c2x + 2*c3x + c4x) / 6.
    vxp = vx + (c1v + 2*c2v + 2*c3v + c4v) / 6.
    return xp, vxp

x = 1.0
vx = 0.0
t = 0.0
dt = 0.01
tf = 50.0
n_steps = int(tf / dt)

t_arr = np.zeros(n_steps + 1)
x_arr = np.zeros(n_steps + 1)
vx_arr = np.zeros(n_steps + 1)

t_arr[0] = t
x_arr[0] = x
vx_arr[0] = vx

# a) -a) Use o método de Runge-Kutta da 4ª ordem para calcular numericamente a lei do movimento, de 
#0 até 50s, no caso em que a velocidade inicial é nula e a posição inicial é x=1 m. 


for i in range(1, n_steps + 1):
    x, vx = rk4_x_vx(t, x, vx, aceleracao, dt)
    t += dt
    t_arr[i] = t
    x_arr[i] = x
    vx_arr[i] = vx

plt.figure(figsize=(10,5))
plt.plot(t_arr, x_arr, label='Posição x(t)')
plt.plot(t_arr, vx_arr, label='Velocidade vx(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('x e vx')
plt.title('Oscilador quártico amortecido e forçado - RK4 4ª ordem')
plt.legend()
plt.grid(True)
plt.show()


#b) Exprimentar vários valores de dt


dt_list = [0.1, 0.05, 0.02, 0.01, 0.005]

resultados = []

for dt in dt_list:
    n_steps = int(tf / dt)
    x = 1.0
    vx = 0.0
    t = 0.0
    
    for i in range(n_steps):
        x, vx = rk4_x_vx(t, x, vx, aceleracao, dt)
        t += dt
    
    resultados.append((dt, x, vx))

print("Passo dt | Posição final x(50s) | Velocidade final vx(50s)")
for dt, x_final, vx_final in resultados:
    print(f"{dt:.4f}    | {x_final:.6f}          | {vx_final:.6f}")
#c) - Calcular novamente a lei do movimento
x = 1.0001
vx = 0.0
t = 0.0
dt = 0.01
tf = 100.0
n_steps = int(tf / dt)

t_arr = np.zeros(n_steps + 1)
x_arr = np.zeros(n_steps + 1)
vx_arr = np.zeros(n_steps + 1)

t_arr[0] = t
x_arr[0] = x
vx_arr[0] = vx

for i in range(1, n_steps + 1):
    x, vx = rk4_x_vx(t, x, vx, aceleracao, dt)
    t += dt
    t_arr[i] = t
    x_arr[i] = x
    vx_arr[i] = vx

plt.figure(figsize=(12,6))
plt.plot(t_arr, x_arr, label='Posição x(t)')
plt.plot(t_arr, vx_arr, label='Velocidade vx(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('x e vx')
plt.title('Oscilador quártico amortecido e forçado até 100s\nPosição inicial = 1.0001 m, vx inicial = 0')
plt.legend()
plt.grid(True)
plt.show()
 
 #d) Trajetoria no espaço fase 

 # Condições iniciais
x = 1.0001
vx = 0.0
t = 0.0
dt = 0.01
tf = 100.0
n_steps = int(tf / dt)

# Arrays para armazenar os resultados
t_arr = np.zeros(n_steps + 1)
x_arr = np.zeros(n_steps + 1)
vx_arr = np.zeros(n_steps + 1)

t_arr[0] = t
x_arr[0] = x
vx_arr[0] = vx

# Loop de integração numérica
for i in range(1, n_steps + 1):
    x, vx = rk4_x_vx(t, x, vx, aceleracao, dt)
    t += dt
    t_arr[i] = t
    x_arr[i] = x
    vx_arr[i] = vx

# Plot do espaço de fase (vx vs x)
plt.figure(figsize=(8,6))
plt.plot(x_arr, vx_arr, lw=0.8)
plt.xlabel('Posição x(t)')
plt.ylabel('Velocidade vx(t)')
plt.title('Espaço de fase do oscilador quártico amortecido e forçado\n(velocidade vs posição)')
plt.grid(True)
plt.show()
