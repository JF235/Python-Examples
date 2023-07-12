import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

Y = "#FDE725"
B = "#20908D"
P = "#440D54"

plt.rcParams["mathtext.fontset"] = "cm"

def solve(f, df, x0, no_iterations = 10):
    x = x0
    for _ in range(no_iterations):
        x = x - f(x)/df(x)
    return x


f = lambda x: 3*(x-2)*(x-4)*(x-6)
df = lambda x: 3*(44 - 24*x + 3*x**2)
x = np.linspace(1.9, 6.1, 1024*8)
y = f(x)
xsol = solve(f, df, x, no_iterations=25)
# x = np.linspace(0, 3 * np.pi, 500)
# y = np.sin(x)
# xsol = np.cos(0.5 * (x[:-1] + x[1:]))
plt.plot(x, y, color="None")

# Copied
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
norm = plt.Normalize(xsol.min(), xsol.max())
# lc = LineCollection(segments, cmap='viridis', norm=norm)
# lc.set_array(xsol)
# lc.set_linewidth(2)
# line = plt.gca().add_collection(lc)
# plt.colorbar(line)

cmap = ListedColormap([Y, B, P])
norm = BoundaryNorm([1.9, 3.9, 5.9, 6.1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(xsol)
lc.set_linewidth(2)
line = plt.gca().add_collection(lc)
# plt.colorbar(line)
plt.autoscale(False)
plt.plot(0, 0, color = Y, label = "$x = 2$")
plt.plot(0, 0, color = B, label = "$x = 4$")
plt.plot(0, 0, color = P, label = "$x = 6$")


plt.legend()
plt.grid()
plt.show()