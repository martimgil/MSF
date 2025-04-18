
import numpy as np
import matplotlib.pyplot as plt



def euler(dt):

    v0 = 0
    vT = 6.80
    g = 9.80
   
    t0 = 0
    tf=5

    t = np.arange(t0,tf,dt)
    y = np.empty(np.size(t))
    v = np.empty(np.size(t))
    a = np.empty(np.size(t))

    y[0] = 0 
    v[0] = v0


    for i in range(np.size(t)-1):
        v[i + 1] = v[i] + g*dt
        y[i+1] = y[i] + v[i]*dt

    #Velocidade no instante 3s

    n3 = int(3/dt)
    n2 = int(2/dt)

    print("V[3s] = ", v[n3])
    print("X[3s] = ", y[n3])
    print("X[2s] = ", y[n2])
    print("dx (t=2) =", np.abs(y[n3]-19.6), "m")

euler(0.1)
euler(0.01)
euler(0.001)



"""   

#Gráfico da aceleração
plt.plot(t,a, 'b-')
plt.xlabel("Tempo, t(s)")
plt.ylabel("Aceleração, m/s2")
plt.show()

#Gráfico da velocidade
plt.plot(t,v, 'b-')
plt.xlabel("Tempo, t(s)")
plt.ylabel("Velocidade, m/s")
plt.show()

#Determinação da velocidade ao fim de 1 segundo

index1 = int(1/dt)
print(f"t[index1] = {t[index1]:.5f} s")
print("V(1) = {:.2f} km/h".format(v[10000]*3.6))

#Quanto tempo tem o volante reduzida a sua velocidade para metade do v0

v1 = v0/2
r = -1
for i in v:
    if i>=v1:
        r+=1

print(f"O tempo para reduzir a velocidade a 50% é t = {t[r]:.4f} s")

plt.plot(t, y, 'g-')
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.title("Posição em função do tempo")
plt.grid()
plt.show()


indext= -1
for i in y:
    if i<=4:
        indext+=1

print(t[indext])

"""