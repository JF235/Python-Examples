import numpy as np
import matplotlib.pyplot as plt


def is_stable(no_iterations = 24):
    z = 0
    for _ in range(no_iterations):
        z = z**2 + M
    return abs(z) <= 2

pixel_density = 4000
xspan = (-2, 1)
yspan = (-1.5, 1.5)
x = np.linspace(*xspan, int(xspan[1] - xspan[0])*pixel_density)
y = np.linspace(*yspan, int((yspan[1] - yspan[0])*pixel_density))
X, Y = np.meshgrid(x, y)
M = X + 1j*Y
plt.imshow(is_stable(), cmap = "binary")
plt.axis("off")
plt.tight_layout()
plt.savefig("Complex/imgs/mandelbrot_image.png", dpi = 400)

plt.show()