import numpy as np
import matplotlib.pyplot as plt

#RELAÇAO DE POTENCIA

def minimos_quadrados(x, y):
    # Número de pontos
    N = x.size
    
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_y2 = np.sum(y ** 2)
    sum_xy = np.sum(x * y)

    # Coeficientes da reta
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (N * sum_x2 - sum_x ** 2)

    # Coeficiente de determinação
    r2 = ((N * sum_xy - sum_x * sum_y) ** 2) / ((N * sum_x2 - sum_x ** 2) * (N * sum_y2 - sum_y ** 2))

    # Incertezas
    dm = np.abs(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    db = dm * np.sqrt(sum_x2 / N)

    return m, b, r2, dm, db

# Parâmetros
m = np.array([0.15,0.20,0.16,0.11,0.25,0.32, 0.40, 0.45, 0.50,0.55])
t = np.array([1.21, 1.40, 1.26, 1.05, 1.60, 1.78, 2.00, 2.11, 2.22, 2.33])

md, b, r2, dm, db = minimos_quadrados(m, t)

print('m =',md)
print('b =',b)
print('r2 =',r2)
print('dm =',dm)
print('db =',db)


# Ajuste
plt.scatter(m,t)
plt.xlabel('Massa (kg)')
plt.ylabel('Período (s)')
plt.title('Período de oscilação x Massa')
plt.show()

#Gráfico loglog



m_log = np.log(m)
t_log = np.log(t)

md,b,r2,dm,db = minimos_quadrados(m_log, t_log)
plt.plot(m,np.exp(md*m_log+b))

plt.loglog(m,t, 'bo')
plt.xlabel('Massa (kg)')
plt.ylabel('Período (s)')
plt.title('Período de oscilação x Massa')
plt.show()

print('m =',md,'+-',dm)
print('b =',b,'+-',db)
print('r2 =',r2)

#Gráfico da relação

t2=t**2

plt.scatter(m,t2)
plt.xlabel('Massa (kg)')
plt.ylabel('Período^2 (s^2)')
plt.title('Período^2 de oscilação x Massa')

md,b,r2,dm,db = minimos_quadrados(m, t2)
plt.plot(m,md*m+b)
plt.show()

print('m =',md,'+-',dm)
print('b =',b,'+-',db)
print('r2 =',r2)

#Valor de constante elastica

k = 4*np.pi**2/md
dk = k*dm/md

print('k =',k,'+-',dk)