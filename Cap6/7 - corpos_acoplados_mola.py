import numpy as np
import matplotlib.pyplot as plt

k = 1.0
k_prime = 0.5
m = 1.0
xA_eq=1.0
xB_eq = 1.2

def derivatives(y):
    xA, vA, xB, vB = y

    F_A = -k*(xA - xA_eq) - k_prime*(xA-xB)
    F_B = -k_prime*(xB - xA_eq) - k*(xB - xB_eq)

    aA = F_A / m
    aB = F_B / m

    return np.array([vA, aA, vB, aB])

def euler_integrate(y0,t,dt):
    n = len(t)
    y = np.zeros((n,4))
    y[0] = y0

    for i in range(1,n):
        y[i] = y[i-1] + dt * derivatives(y[i-1])
    return y

dt = 0.01
t_max = 30.0
t = np.arange(0, t_max, dt)

# Casos iniciais
cases = [
    {'name': 'Caso i)', 'xA0': xA_eq + 0.05, 'xB0': xB_eq + 0.05, 'vA0': 0, 'vB0': 0},
    {'name': 'Caso ii)', 'xA0': xA_eq + 0.05, 'xB0': xB_eq - 0.05, 'vA0': 0, 'vB0': 0},
    {'name': 'Caso iii)', 'xA0': xA_eq + 0.05, 'xB0': xB_eq, 'vA0': 0, 'vB0': 0}
]

plt.figure(figsize=(15, 10))

for i, case in enumerate(cases):
    y0 = np.array([case['xA0'], case['vA0'], case['xB0'], case['vB0']])

    solution = euler_integrate(y0, t, dt)
    xA = solution[:, 0]
    xB = solution[:, 2]

    plt.subplot(3, 1, i + 1)
    plt.plot(t, xA, label='xA', color='blue')
    plt.plot(t, xB, label='xB', color='orange')
    plt.title(case['name'])
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

def find_period(t, x):
    peaks = np.where((x[1:-1] > x[:-2]) & (x[1:-1] > x[2:]))[0] + 1
    if len(peaks) < 2:
        return np.nan
    periods = np.diff(t[peaks])
    return np.mean(periods)


# Caso i
y0_i = np.array([cases[0]['xA0'], cases[0]['vA0'], cases[0]['xB0'], cases[0]['vB0']])
solution_i = euler_integrate(y0_i, t, dt)
T_i = find_period(t, solution_i[:, 0])
omega_i = 2*np.pi/T_i if not np.isnan(T_i) else np.nan

# Caso ii
y0_ii = np.array([cases[1]['xA0'], cases[1]['vA0'], cases[1]['xB0'], cases[1]['vB0']])
solution_ii = euler_integrate(y0_ii, t, dt)
T_ii = find_period(t, solution_ii[:, 0])
omega_ii = 2*np.pi/T_ii if not np.isnan(T_ii) else np.nan

print(f"Caso i) Período: {T_i:.2f} s, Frequência angular: {omega_i:.2f} rad/s")
print(f"Caso ii) Período: {T_ii:.2f} s, Frequência angular: {omega_ii:.2f} rad/s")