import numpy as np
import matplotlib.pyplot as plt


def minimos_quadrados(x, y):
    N = len(x)  # Número de pontos

    # Somatórios necessários
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)

    # Coeficientes da reta
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)
    b = (sum_y * sum_x2 - sum_x * sum_xy) / (N * sum_x2 - sum_x**2)

    # Cálculo de r^2
    y_pred = m * x + b
    ssr = np.sum((y - y_pred)**2)  # Soma dos quadrados dos resíduos
    sst = np.sum((y - np.mean(y))**2)  # Soma total dos quadrados
    r2 = 1 - (ssr / sst)

    # Erros nos coeficientes
    dm = np.sqrt(ssr / ((N - 2) * np.sum((x - np.mean(x))**2)))
    db = dm * np.sqrt(np.sum(x**2) / N)

    return m, b, r2, dm, db


#a)
A = np.array([9.679, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])
T = np.array([0,5,10,15,20,25,30, 35, 40, 45])

plt.scatter(T,A)
plt.show()
#R: Não

#b) 

plt.semilogy(T, A, 'bo')  
y = np.log(A) 

m, b, r2, dm, db = minimos_quadrados(T, y)

plt.plot(T, np.exp(m * T + b), 'r-', label="Ajuste")
plt.legend()
plt.xlabel("tempo (dias)")
plt.ylabel("Atividade (mCi)")
plt.show()

print("m = {:.4f} +- {:.5f} dias-1".format(m, dm))


