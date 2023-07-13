import numpy as np
from numpy import sin, cos, tan, exp, sqrt, pi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import hsv_to_rgb, rgb_to_hsv, to_rgb

def approx_integral(f, xinterval, no_divisions):
    """Calcula a aproximação da integral de f no intervalo xinterval.
    
    Usa uma soma de Riemann, com ponto central, de cada um dos intervalos.

    # Parameters:
        f (function): A função que será integrada
        xinterval (tuple): Extremos do intervalo de integração
        no_divisions (int): Número de divisões do intervalo

    # Returns:
        float: Resultado da integral
    """
    a, b = xinterval[0], xinterval[1]
    dx = (b - a)/no_divisions
    x = np.linspace(a + dx/2, b - dx/2, no_divisions)
    return sum(f(x)*dx)

def draw_centered_axis(ax):
    """Desenha um conjunto de eixos centrados em zero.
    
    Remove a origem.

    # Parameters:
        ax (axes): axes respectivo
    """
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    # Remove 0s
    locs, _ = plt.xticks()
    locs = locs[locs != 0]
    plt.xticks(locs)
    locs, _ = plt.yticks()
    locs = locs[locs != 0]
    plt.yticks(locs)
    

def plot_riemannsum(f, xinterval, no_divisions):
    """Faz um gráfico mostrando os retângulos em um
    procedimento de soma de Riemann.
    
    Colore de verde as áreas positivias e de vermelho
    as áreas negativas.

    # Parameters:
        f (function): A função que será integrada
        xinterval (tuple): Extremos do intervalo de integração
        no_divisions (int): Número de divisões do intervalo
    """
    a, b = xinterval[0], xinterval[1]
    dx = (b - a)/no_divisions
    
    plt.figure()
    ax = plt.gca()
    
    # Desenha a curva
    xpadding = (b-a)*.05
    x = np.linspace(a-xpadding, b+xpadding, 200)
    plt.plot(x, f(x), '-k', linewidth=2)
    
    xmid = np.linspace(a + dx/2, b - dx/2, no_divisions)
    for i in range(no_divisions):
        xi = xmid[i] - dx/2
        
        if f(xmid[i]) >= 0:
            color = "tab:green"
        else:
            color = "tab:red"   
         
        line, = plt.plot(xmid[i], f(xmid[i]), '.', color=color)
        edgecolor = rgb_to_hsv(to_rgb(color))
        edgecolor[2] = .7*edgecolor[2]
        edgecolor = hsv_to_rgb(edgecolor)
        line.set(markeredgecolor = edgecolor)
        
        ax.add_patch(Rectangle((xi, 0), dx, f(xmid[i]), facecolor=color, edgecolor=edgecolor))
    
    draw_centered_axis(ax)
    
arg = [lambda x: sin(x), (0, pi), 40]
plot_riemannsum(*arg)
result = approx_integral(*arg)
plt.text(1.5, -0.3, r"$\sum_{i=1}^{n}f(x_i)\Delta x" + f"={result:.3f}$", ha="center", fontdict=dict(fontsize=16))

plt.tight_layout()
plt.show()