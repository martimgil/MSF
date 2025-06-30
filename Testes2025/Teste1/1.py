#124833 Martim Lopes Gil

import numpy as np
import matplotlib.pyplot as plt

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

# Dados
c = np.array([1.2, 4.2, 11, 20, 22, 37, 45]) 
m = np.array([0.03, 0.54, 9.1, 38, 57, 230, 480])

#a) - Traçar o gráfico da massa em função do comprimento do fêmur

mr,b,r2,dm,db = minimos_quadrados(c,m)


print("\n Reta de regressão linear do gráfico")
print('m =',mr)
print('b =',b)
print('dm =',dm)
print('db =',db)
print('r2 =',r2)


print("\na) R.: O coeficiente de determinação r2 é {:.2f}".format(r2))

plt.scatter(c,m)
plt.plot(c, mr * c + b, label='Ajuste')
plt.title("Gráfico da massa em função do comprimento do fêmur")
plt.xlabel("Comprimento do fêmur (cm)")
plt.ylabel("Massa(kg)")
plt.show()

#b) 
#Gráfico do logaritmo da massa em função do comprimento 

plt.semilogy(c,m, 'bo')  
y = np.log(m) 

mr, b, r2, dm, db = minimos_quadrados(c, y)


print('m =',mr)
print('b =',b)
print('r2 =',r2)
print('dm =',dm)
print('db =',db)


plt.plot(c, np.exp(mr * c + b))
plt.legend()
plt.title("Gráfico do logaritmo da massa em função do comprimento do fémur")
plt.xlabel("Comprimento do fêmur (cm)")
plt.ylabel("log(Massa(kg))")
plt.show()

print("\n Reta de regressão linear do gráfico semilogy")
print('m =',mr)
print('b =',b)
print('r2 =',r2)
print('dm =',dm)
print('db =',db)


#Gráfico do logaritmo da massa em função do logaritmo do comprimento do fémur

log_c = np.log(c)
log_m = np.log(m)

mr, b, r2, dm, db = minimos_quadrados(log_c, log_m)

log_fit = mr*log_c+b

plt.loglog(c,m, 'bo')
plt.loglog(c, np.exp(log_fit), label='Ajuste Linear')
plt.title("Gráfico do logaritmo da massa em função do logaritmo do comprimento do fémur")
plt.xlabel("log(Comprimento do fêmur (cm))")
plt.ylabel("log(Massa(kg))")
plt.show()


print("\n Reta de regressão linear do gráfico loglog")
print('m =',mr)
print('b =',b)
print('r2 =',r2)
print('dm =',dm)
print('db =',db)


print("\n c) Pelos resultados obtidos na alinea anterior é possivel concluir que estes possuem uma relação de potencia")
print("y=x^n")
print("m = c^2.66")
