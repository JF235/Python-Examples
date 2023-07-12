import numpy as np
import matplotlib.pyplot as plt
from newtonsMethodLib import *


plt.rcParams["mathtext.fontset"] = "cm"

def get_tangent(f, df, x0):
    return (lambda x: df(x0)*(x-x0) + f(x0))

def draw_tangent(f, df, x0, size=50, **kwargs):
    l = get_tangent(f, df, x0)
    ds = size/2
    dx = np.sqrt(ds**2/(1 + df(x0)**2))
    x = np.linspace(x0-dx, x0+dx, 3)
    plt.plot(x, l(x), **kwargs)

def draw_solve(f, df, x0, no_iterations = 4, tangents=False, **kwargs):
    x_gen = solve_gen(f, df, x0)
    
    xlist = []
    flist = []
    xlist.append(x0)
    flist.append(f(x0))
    for _ in range(no_iterations):
        x = next(x_gen)
        fx = f(x)
        xlist.append(x)
        flist.append(fx)
    xlist, flist = np.array(xlist), np.array(flist)
    plt.plot(xlist, flist, 'x', **kwargs)
    if tangents:
        alpha = 0.1
        for i, x in enumerate(xlist):
            alpha = (i+1)/len(xlist) - 0.1
            plt.plot(x, 0, "xk", alpha = alpha)
            plt.plot(x, f(x), "ok", alpha = alpha)
            draw_tangent(f, df, x, color="black", alpha=alpha)

# f = lambda x: 3*(x-2)*(x-4)*(x-6)
# df = lambda x: 3*(44 - 24*x + 3*x**2)
f = lambda x: x**2
df = lambda x: 2*x

x = np.linspace(-4, 4, 200)
plt.plot(x, f(x))

xlim = (-1, 3.5)
plt.xlim(xlim)
ylim = (-1, 10)
plt.ylim(ylim)


# plt.plot([2,4,6], [0,0,0], 'o', markerfacecolor="None", label="Raízes")

# Colored
# draw_solve(f, df, 3.1, no_iterations=20)
draw_solve(f, df, 3.1, no_iterations=3, tangents=True, color="None")
plt.title("Newton-Raphson Visualization")
plt.plot(0, 0, 'or')
#draw_tangent(f, df, 3.1)

plt.plot(50, 50, "xk", alpha = .7, label = "Intersecção da tangente, $x_{n+1}$")
plt.plot(50, 50, "ok", alpha = .7, label = "$f(x_{n})$")
plt.plot(50, 50, "k", alpha = .7, label = "Tangente em $x_n$")

plt.legend()
plt.grid()

plt.show()