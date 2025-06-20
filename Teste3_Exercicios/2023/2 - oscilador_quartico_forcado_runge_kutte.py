import numpy as np
import matplotlib.pyplot as plt

# a) Integração com RK4

# Parâmetros do sistema
m = 1.0
b = 0.02
alpha = 0.15
F0 = 7.5
w_f = 1.0
k = 1.0

# Função aceleração
def acelera(t, x, vx):
    return (-4*alpha*x**3 - b*vx - k*x + F0*np.cos(w_f*t)) / m

# Método de Runge-Kutta de 4ª ordem
def rk4_x_vx(t, x, vx, acelera, dt):
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

    xp = x + (c1x + 2.*c2x + 2.*c3x + c4x) / 6.
    vxp = vx + (c1v + 2.*c2v + 2.*c3v + c4v) / 6.
    return xp, vxp

x0 = 2.0
vx0 = 0.0
t0 = 0.0
tf = 100
dt = 0.01

# Integração da solução central (a)
t_vals = [t0]
x_vals = [x0]
vx_vals = [vx0]
t = t0
x = x0
vx = vx0

while t < tf:
    x, vx = rk4_x_vx(t, x, vx, acelera, dt)
    t += dt
    t_vals.append(t)
    x_vals.append(x)
    vx_vals.append(vx)


# b) Sensibilidade à condição inicial

x0_p = x0 + 0.001
x0_m = x0 - 0.001
vx_p = vx0
vx_m = vx0
x_vals_p = [x0_p]
x_vals_m = [x0_m]
t_b = t0

for _ in range(int(tf / dt)):
    x0_p, vx_p = rk4_x_vx(t_b, x0_p, vx_p, acelera, dt)
    x0_m, vx_m = rk4_x_vx(t_b, x0_m, vx_m, acelera, dt)
    x_vals_p.append(x0_p)
    x_vals_m.append(x0_m)
    t_b += dt

min_len = min(len(t_vals), len(x_vals), len(x_vals_p), len(x_vals_m))
t_vals_plot = np.array(t_vals[:min_len])
x_vals_plot = np.array(x_vals[:min_len])
x_vals_p_plot = np.array(x_vals_p[:min_len])
x_vals_m_plot = np.array(x_vals_m[:min_len])


plt.figure(figsize=(10, 5))
#plt.plot(t_vals_plot, x_vals_plot, label='x(t) - posição (a)', linewidth=2, color='blue')
plt.plot(t_vals_plot, x_vals_p_plot, '--', label='x(t) - +0.001m (b)', linewidth=2, color='red')
plt.plot(t_vals_plot, x_vals_m_plot, '--', label='x(t) - -0.001m (b)', linewidth=2, color='green')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição vs Tempo - Cores distintas e maior espessura')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("Até aproximadamente a partir dos 40s (os graficos começam a deixar de se sobrepor)")

