import numpy as np
import matplotlib.pyplot as plt

def lorenz(xyz, s=10, r=28, b=2.667):
    x, y, z = xyz
    return np.array([s*(y - x), 
                     x*(r-z) - y, 
                     x*y - b*z])


dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = [0., 1., 1.05]
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt 

ax = plt.figure().add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_title("Lorenz Attractor")
plt.tight_layout()
plt.savefig("LorenzAttractor/imgs/lorenz_attractor01.jpeg", dpi=300)
plt.show()