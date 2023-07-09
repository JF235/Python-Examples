import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, sqrt, degrees

plt.rcParams["mathtext.fontset"] = "cm"

g = 9.8 # m/s^2
l = .3 # m

f = lambda t, x: np.array([x[1], -g/l * sin(x[0])])

# Euler
total_time = 3 # s
steps_per_second = 600 # steps/s
no_steps = total_time * steps_per_second

t = np.linspace(0, total_time, no_steps)
dt = t[1] - t[0]

x = np.empty((no_steps + 1, 2))
# Initial Cond.
x[0] = np.array([np.pi/2, 0])
for i in range(no_steps):
    x[i+1] = x[i] + f(t[i], x[i]) * dt

plt.figure(1, figsize=(8,6))
plt.subplot(2, 1, 1)
plt.plot(t, degrees(x[:-1, 0]), label = "Pendulum")
plt.plot(t, degrees(x[0, 0])*cos(sqrt(g/l)*t), label = r"$\theta_0\cos(\omega t)$")
plt.title(r"$x_1 = \theta$")
ylim = plt.gca().get_ylim()
plt.yticks(np.arange(-90, 91, 30))
plt.ylim(ylim)
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, degrees(x[:-1, 1]))
plt.title(r"$x_2 = \dot{\theta}$")
plt.grid()

plt.tight_layout()
plt.savefig("LorenzAttractor/imgs/pendulumSolve02.jpeg", dpi=300)

plt.figure(2)
plt.plot(x[:-1, 0], x[:-1, 1])
plt.title("Phase Space")
plt.savefig("LorenzAttractor/imgs/pendulumSolve-Phase02.jpeg", dpi=300)
plt.show()