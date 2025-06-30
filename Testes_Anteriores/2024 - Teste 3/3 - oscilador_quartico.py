import numpy as np
import matplotlib.pyplot as plt


#Dados
m = 0.2
k = 1
x0 = -1
xf = 2


#a) - Diagrama de energia desta energia potencial entre x = -1 e x = 2

x = np.linspace(x0, xf, 10000)
Ep = k*((x-1)**2)*(x+1) 
plt.plot(x, Ep, label='Energia Potencial', color='blue')
plt.title('Energia Potencial do Oscilador Harmônico')
plt.xlabel('Posição (x)')
plt.ylabel('Energia Potencial (Joules)')
plt.show()

#b) Lei do movimento
x0 = 1.5
v0 = 0

#Metodo de Euler

def euler_integration(x0, v0, dt=0.0001, t_total = 30):
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
        f = -3*k*x[i-1]**2 + 2*k*x[i-1] + k
        v[i] = v[i-1] + f * dt / m

    return t, x, v


t,x,v = euler_integration(x0, v0)
plt.plot(euler_integration(x0, v0)[0], euler_integration(x0, v0)[1], label='Posição x(t)', color='orange')
plt.title('Movimento do Oscilador Quântico')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.show()

#c) Energia cinetica, potencial e total

Ec = 0.5*m*v**2
Ep = k*((x-1)**2)*(x+1) 
Et = Ec + Ep

plt.plot(x, Ec, label='Energia Cinética', color='green')
plt.plot(x, Ep, label='Energia Potencial', color='red')
plt.plot(x, Et, label='Energia Total', color='purple')
plt.title('Energias do Oscilador Quântico')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (Joules)')
plt.legend()
plt.show()


# d) Velocidade quando x = 0.5 m usando conservação da energia
# Energia total inicial
Ep_inicial = k * ((x0 - 1)**2) * (x0 + 1)
Ec_inicial = 0.5 * m * v0**2
E_total = Ep_inicial + Ec_inicial

# Energia potencial em x = 0.5
x_d = 0.5
Ep_d = k * ((x_d - 1)**2) * (x_d + 1)

# Energia cinética em x = 0.5
Ec_d = E_total - Ep_d

# Velocidade
if Ec_d >= 0:
    v_d = np.sqrt(2 * Ec_d / m)
    print(f"Velocidade em x = 0.5 m: {v_d:.4f} m/s")
else:
    print("Erro: Energia cinética negativa. Movimento impossível em x = 0.5 m.")
