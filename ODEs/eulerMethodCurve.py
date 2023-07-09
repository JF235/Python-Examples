import numpy as np
import matplotlib.pyplot as plt

x = lambda t: -(2-t)**2
dxdt = lambda t: 2*(2-t)

t0 = 0
tf = 4
t = np.linspace(t0, tf,100)
plt.plot(t, x(t))

# Euler Method
x0 = x(t0)
dts = [0.8,0.4, 0.1, 0.01]
for dt in dts:
    no_steps = int((tf-t0)/dt)
    x_arr = np.empty(no_steps + 1)
    t_arr = np.empty(no_steps + 1)
    t_arr[0] = t0
    x_arr[0] = x0
    for i in range(no_steps):
        x_arr[i+1] = x_arr[i] + dxdt(t_arr[i]) * dt
        t_arr[i+1] = t_arr[i] + dt
    
    plt.plot(t_arr, x_arr, label=f"dt = {dt}")

plt.legend()
plt.grid()
plt.title("Euler Method")
plt.tight_layout()
plt.savefig("LorenzAttractor/imgs/euler_method01.jpeg", dpi=300)
plt.show()