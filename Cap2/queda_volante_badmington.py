import numpy as np
import matplotlib.pyplot as plt
import sympy as sy


vT = 6.80
g = 9.80
t = np.linspace(0, 3, 100) 
y = (vT**2 / g) * np.log(np.cosh(g * t / vT))

plt.plot(t, y)  
plt.xlabel("t (s)")
plt.ylabel("y (m)")
plt.title("Queda Volante com vy(0)=0")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

x,y,m,b = sy.symbols('x,y,m,b')
t = sy.symbols('t')
y = (vT**2 / g) * sy.log(sy.cosh(g * t / vT))
v = sy.diff(y,t)
print(v)
v_func = sy.lambdify(t,v, 'numpy')

t = np.linspace(0, 4, 100)
v2 = v_func(t)

plt.plot(t,v2)
plt.xlabel("t(s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade em função do tempo")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()