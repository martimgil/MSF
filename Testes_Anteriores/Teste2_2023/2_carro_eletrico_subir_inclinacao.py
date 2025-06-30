import numpy as np

# Parâmetros
m = 2000  # kg
g = 9.81  # m/s²
theta = np.radians(5)
p_subida = 40000  # W
p_descida = -10000  # W
distancia = 2000  # m
dt = 0.01  # passo de tempo pequeno para precisão

# ---------------------
# SUBIDA
# ---------------------
tempo = 0
v = 1.0  # velocidade inicial
x = 0
while x < distancia:
    f_grav = m * g * np.sin(theta)
    f_motor = p_subida / v
    a = (f_motor - f_grav) / m
    v += a * dt
    x += v * dt
    tempo += dt

tempo_subida = tempo
trabalho_subida = p_subida * tempo_subida  # J

# ---------------------
# DESCIDA
# ---------------------
tempo = 0
v = 20.0  # velocidade inicial na descida
x = 0
while x < distancia:
    f_grav = m * g * np.sin(theta)
    f_motor = p_descida / v
    a = (f_grav + f_motor) / m
    v += a * dt
    x += v * dt
    tempo += dt

tempo_descida = tempo
trabalho_descida = p_descida * tempo_descida  # J
energia_recuperada = 0.5 * abs(trabalho_descida)

# ---------------------
# DIFERENÇA NA BATERIA
# ---------------------
delta_energia = -trabalho_subida + energia_recuperada

# ---------------------
# RESULTADOS
# ---------------------
print(f"(b) Tempo da subida: {tempo_subida:.2f} s")
print(f"(c) Trabalho na subida: {trabalho_subida / 1000:.0f} kJ")
print(f"(d) Tempo da descida: {tempo_descida:.2f} s")
print(f"    Trabalho regenerativo: {trabalho_descida / 1000:.0f} kJ")
print(f"(e) Δ Energia da bateria: {delta_energia / 1000:.0f} kJ")
