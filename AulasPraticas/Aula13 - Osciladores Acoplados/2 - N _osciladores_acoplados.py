import numpy as np
import matplotlib.pyplot as plt

#Simular o movimento de N=5 massas por Euler-Cromes

N = 5
k=1.0
m = 1.0
dt = 0.01
t_max = 30.0
t = np.arange(0, t_max, dt)
n_steps = len(t)

u = np.zeros((N, n_steps))
v = np.zeros((N, n_steps))
u[0,0 ] = 1.0

for i in range(n_steps - 1):
    a = np.zeros(N)
    # Massa 0 (extremidade esquerda)
    a[0] = (-k*u[0,i] - k*(u[0,i] - u[1,i])) / m
    
        # Massas internas
    for j in range(1, N-1):
        a[j] = (-k*(u[j,i] - u[j-1,i]) - k*(u[j,i] - u[j+1,i])) / m
    
    # Massa N-1 (extremidade direita)
    a[N-1] = (-k*u[N-1,i] - k*(u[N-1,i] - u[N-2,i])) / m
    
    # Atualizar velocidades
    v[:, i+1] = v[:, i] + a * dt
    
    # Atualizar posições
    u[:, i+1] = u[:, i] + v[:, i+1] * dt

# Plot dos resultados
plt.figure(figsize=(12, 8))
for j in range(N):
    plt.plot(t, u[j, :], label=f'Massa {j}')
plt.title('Movimento de 5 osciladores acoplados - Uma massa inicialmente deslocada')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.legend()
plt.grid(True)
plt.show()

#b) Veriricacao do movimento com condicoes iniciais sinusoidais

# Função para gerar condições iniciais sinusoidais
def initial_conditions(l, N, A=1.0):
    return np.array([A * np.sin(2*np.pi*i*l/(N+1)) for i in range(N)])

# Simulação para cada modo l
plt.figure(figsize=(15, 10))

for l in range(1, N+1):
    # Inicializações
    u_mode = np.zeros((N, n_steps))
    v_mode = np.zeros((N, n_steps))
    
    # Condições iniciais sinusoidais
    u_mode[:, 0] = initial_conditions(l, N)
    
    # Método de Euler-Cromer
    for i in range(n_steps - 1):
        # Calcular acelerações
        a = np.zeros(N)
        
        # Massa 0
        a[0] = (-k*u_mode[0,i] - k*(u_mode[0,i] - u_mode[1,i])) / m
        
        # Massas internas
        for j in range(1, N-1):
            a[j] = (-k*(u_mode[j,i] - u_mode[j-1,i]) - k*(u_mode[j,i] - u_mode[j+1,i])) / m
        
        # Massa N-1
        a[N-1] = (-k*u_mode[N-1,i] - k*(u_mode[N-1,i] - u_mode[N-2,i])) / m
        
        # Atualizar velocidades e posições
        v_mode[:, i+1] = v_mode[:, i] + a * dt
        u_mode[:, i+1] = u_mode[:, i] + v_mode[:, i+1] * dt
    
    # Plot
    plt.subplot(N, 1, l)
    for j in range(N):
        plt.plot(t, u_mode[j, :], label=f'Massa {j}')
    plt.title(f'Modo Normal l={l} - Condições iniciais sinusoidais')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()