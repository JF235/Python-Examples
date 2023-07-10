import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 1, 10)
y = np.linspace(-1, 1, 5)
X, Y = np.meshgrid(x, y)
M = X + 1j*Y

plt.figure(1)
plt.scatter(M.real, M.imag, marker="s")

plt.figure(2)

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

plt.figure(3)

pixel_density = 4000
xspan = (-2, 1)
yspan = (-1.5, 1.5)
x = np.linspace(*xspan, int(xspan[1] - xspan[0])*pixel_density)
y = np.linspace(*yspan, int((yspan[1] - yspan[0])*pixel_density))
X, Y = np.meshgrid(x, y)
M = X + 1j*Y
plt.imshow(is_stable())
plt.axis("off")
plt.tight_layout()
plt.savefig("imgs/mandelbrot_image.png", dpi=400)

plt.show()