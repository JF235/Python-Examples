import numpy as np
import matplotlib.pyplot as plt

xlim = (-10, 10)
ylim = (0, 10)
pixel_density = 5
x = np.linspace(-10, 10, pixel_density*(xlim[1] - xlim[0]))
y = np.linspace(0, 10, pixel_density*(ylim[1] - ylim[0]))
X, Y = np.meshgrid(x, y)
M = X + 1j*Y

# Circle of radius 2
circle_mask = abs(M - 2j) <= 2

plt.gca().set_aspect("equal")
# Plot grid
plt.scatter(M.real, M.imag, marker=".", color ="green")
# Plot circle
plt.scatter(M[circle_mask].real, M[circle_mask].imag, marker=".", color="blue")
plt.xlim(-15, 15)
plt.ylim(-5, 15)
plt.tight_layout()
plt.show()