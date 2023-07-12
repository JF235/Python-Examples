import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from newtonsMethodLib import *

YELLOW = "#FDE725"
BLUE = "#20908D"
PURPLE = "#440D54"
BLACK = "#000000"

cmap = ListedColormap([BLACK, YELLOW, BLUE, PURPLE])

x = np.linspace(-1.5, 1.5, 5000)
y = np.linspace(-1.5, 1.5, 5000)
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

f = lambda z: z**3 + 1
df = lambda z: 3*z**2
M = solve(f, df, Z, no_iterations = 100, show_progress = True)
roots = [-1. +0.j, 0.5-0.87j, 0.5+0.87j]


M[-1, -1] = 20
convergenceMatrix = np.zeros(M.shape)
mask1 = abs(M - roots[0]) < .5
mask2 = abs(M - roots[1]) < .5
mask3 = abs(M - roots[2]) < .5
notConverge = np.invert(mask1 + mask2 + mask3)

masks = [mask1, mask2, mask3]

for i in range(len(masks)):
    convergenceMatrix[masks[i]] = i+1
    

plt.imshow(convergenceMatrix, cmap=cmap)
plt.tight_layout()
plt.axis("off")
plt.savefig("NewtonFractal.png", dpi=400)
plt.show()