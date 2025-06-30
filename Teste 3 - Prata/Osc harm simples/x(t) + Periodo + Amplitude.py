import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

indextime1 = int(3/dt)
indextime2 = int(10/dt)
indextime3 = int(11/dt)
indextime4 = int(16/dt)
t = np.arange(0, 20+dt,dt)
k = 1
m = 1

v = np.zeros(t.size)
x = np.zeros(t.size)

v1 = np.zeros(t.size)
x1 = np.zeros(t.size)

f = np.zeros(t.size)
x[0] = 4
v[0] = 0
x1[0] = 4
v1[0] = 0

for i in range(t.size-1):
    f[i] =  -k * x1[i]
    a = f[i]/m
    v1[i+1] = v1[i] + a*dt
    x1[i+1] = x1[i] + v1[i+1]*dt
    

plt.plot(t,x1)
plt.xlabel("tempo")
plt.ylabel("x(m)")
#ax[1].plot(t,x1)

firstdivision = x1[indextime1:indextime2]
seconddivision = x1[indextime3:indextime4]

print(np.amax(firstdivision))
print(np.amax(seconddivision))

index1, = np.where(x1 == np.amax(firstdivision))
index2, = np.where(x1 == np.amax(seconddivision))

print(index1)
print(index2)

plt.plot(t[index1], np.amax(firstdivision), "bx")
plt.plot(t[index2], np.amax(seconddivision), "bx")

print("tempo entre cristas ->", t[index2]-t[index1])

#calcula a amplitude
amplitude = (np.amax(firstdivision) - np.amin(firstdivision))/2
print("amplitude ->", amplitude)

xtest1 = [3,3]
ytest1 = [-5,5]

xtest2 = [10,10]
ytest2 = [-5,5]

xtest3 = [16,16]
ytest3 = [-5,5]
plt.plot(xtest1,ytest1)
plt.plot(xtest2,ytest2)
plt.plot(xtest3,ytest3)
plt.show()