import matplotlib.pyplot as plt
import numpy as np

#LEI EXPONENCIAL
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
 
t = np.array([0, 48, 96, 144, 192, 240, 288, 336, 384])
a = np.array([10.03, 7.06,4.88, 3.38, 2.26, 1.66, 1.14, 0.79, 0.58])


m, b, r2, dm, db = minimos_quadrados(t, a)

print("m = {0:.4f}".format(m))
print("b = {0:.2f} cm".format(b))
print("r² = {0:.4f}...".format(r2))
print("dm = {0:.4f}".format(dm))
print("db = {0:.2f} cm".format(db))



plt.scatter(t,a)
plt.plot(t, m*t+b)
plt.xlabel("tempo, (dias)")
plt.ylabel("Atividade radioativa")
plt.show()

#b) 

x = t
y = np.log(a)

m,b,r2,dm,db = minimos_quadrados(x,y)

print("m = {0:.4f}".format(m))
print("b = {0:.2f} cm".format(b))
print("r² = {0:.4f}...".format(r2))
print("dm = {0:.4f}".format(dm))
print("db = {0:.2f} cm".format(db))


plt.semilogy(t,a, 'bo')
plt.plot(t, np.exp(m*t+b))
plt.title('Atividade radioativa vs Tempo')
plt.title('Log(A) vs Tempo')
plt.xlabel("Tempo, t (dias)")
plt.ylabel("log(A)")
plt.show()


#c)
t3 = -np.log(2)/m
print("t 1/2 =", t3)
print("dt 1/2 =", dm/m*t3)
