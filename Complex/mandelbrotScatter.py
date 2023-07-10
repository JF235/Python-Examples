import numpy as np
import matplotlib.pyplot as plt

def is_stable(no_iterations = 24):
    z = 0
    for _ in range(no_iterations):
        z = z**2 + M
    return abs(z) <= 2

pixel_density = 32
x = np.linspace(-2, 1, 3*pixel_density)
y = np.linspace(-1, 1, 2*pixel_density)
X, Y = np.meshgrid(x, y)
M = X + 1j*Y
plt.scatter(M[is_stable()].real, M[is_stable()].imag, s=8, c="black", marker="x")
plt.axis("off")

plt.show()