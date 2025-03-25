import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.5,4.5))      
plt.axis([-5, 3, -4.5, 1.0])

x = 0.0
y = 0.0
theta = 0.0
pos = np.array([[x, y, theta]])     

angs = [45,90,45,45,90]
dist = [3,2,3,2,3]

for i in range(len(angs)):
    ang = angs[i]
    d = dist[i]
    theta += ang
    x += d * np.cos(-theta * np.pi / 180)  
    y += d * np.sin(-theta * np.pi / 180)
    pos = np.append(pos, [[x, y, theta]], axis=0)
    plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), 
              color='r', width=0.01, head_width=0.1)


x_f = x
y_f = y
theta_f = theta

print('Posição final: x =', x_f, 'y =', y_f)
print('Orientação final:', theta_f)

plt.plot(pos[:,0], pos[:,1]) 
plt.show()

d = np.sqrt(x_f**2 + y_f**2)  
theta_alvo = np.degrees(np.arctan2(-y_f, -x_f)) 
ang = theta_alvo - theta_f  
ang = (ang + 180) % 360 - 180  

theta += ang
x += d * np.cos(-theta * np.pi / 180)
y += d * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], axis=0)

print("Instrução de retorno:")
print("ang = ({0:.2f})".format(ang))
print("dist = ({0:.2f})".format(d))

plt.figure(figsize=(6.5,4.5))
plt.axis([-4,2.5, -4, 0.5])
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), 
          color='b', width=0.01, head_width=0.1)
plt.plot(pos[:,0], pos[:,1], 'b')  
plt.show()
