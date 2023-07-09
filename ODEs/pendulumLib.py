import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D
from math import cos, sin, pi, radians, degrees, atan2

def get_pendulum_coords(P, length, angle):
    """Obtém coordenadas da massa do pêndulo

    Args:
        P (tuple): Coordenadas xy
        length (float): Comprimento da corda
        angle (float): Ângulo (em graus)

    Returns:
        tuple: Coordenadas xy da massa
    """
    return (P[0] + length*sin(radians(angle)), 
            P[1] - length*cos(radians(angle)))

def get_vector(P, Q, scale = 1):
    """Obtém o vetor que vai de Q até P

    Args:
        P (tuple): Ponto de origem
        Q (tuple): Ponto de destino
        scale (int, optional): Escala do tamanho original. Defaults to 1.

    Returns:
        tuple: Vetor xy
    """
    return (scale*(Q[0] - P[0]), scale*(Q[1] - P[1]))

def draw_vector(v, o, label = "", dx = 0, dy = 0, segment_dict = {}, arrowhead_dict = {}, label_dict = {}, **kwargs):
    """Desenha o vetor v com origem em o
    IMPORTANTE: Só funciona corretamente com aspect ratio "equal"

    Args:
        v (tuple): Vetor a ser desenhado
        o (tuple): Ponto de origem do vetor
        label (str, optional): Rótulo. Defaults to "".
        dx (int, optional): Deslocamento em x do rótulo. Defaults to 0.
        dy (int, optional): Deslocamento em y do rótulo. Defaults to 0.
        segment_dict (dict, optional): Opções para modificar o segmento. Defaults to {}.
        arrowhead_dict (dict, optional): Opções para modificar a cabeça da flecha. Defaults to {}.
        label_dict (dict, optional): Opções para modificar o rótulo. Defaults to {}.
    """
    p = (o[0] + v[0], o[1] + v[1])
    if label:
        plt.text(o[0] + .5*v[0] + dx, o[1] + .5*v[1] + dy, label, **label_dict, **kwargs)
        
    plt.plot([o[0], p[0]], [o[1], p[1]], **segment_dict, **kwargs)
    theta = degrees(atan2(v[1], v[0])) - 90
    plt.plot(p[0], p[1], marker=(3, 0, theta), **arrowhead_dict, **kwargs)

def draw_pendulum(P, length, angle, **kwargs):
    """Desenha o pêndulo

    Args:
        P (tuple): Ponto de fixação do pêndulo
        length (float): Comprimento da corda
        angle (degrees): Ângulo (em graus)
    """
    Q = get_pendulum_coords(P, length, angle)
    plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k', lw=1)
    plt.plot(Q[0], Q[1], 'o', markersize=20, markerfacecolor='white', markeredgecolor='black', **kwargs)
    
def draw_arc(center, radius, theta1, theta2, label="", label_dict={}):
    """Desenha o arco com dado centro e raio, com ângulo inicial theta1 até o ângulo final theta2

    Args:
        center (tuple): Centro do arco
        radius (float): Raio do arco
        theta1 (float): Ângulo inicial em graus
        theta2 (float): Ângulo inicial em graus
        label (str, optional): Rótulo. Defaults to "".
        label_dict (dict, optional): Opções do rótulo. Defaults to {}.
    """
    arc = Arc(center, width=2*radius, height=2*radius, theta1=theta1, theta2=theta2)
    plt.gca().add_patch(arc)
    if label:
        theta_mid = radians(.5*(theta2 + theta1))
        label_pos = (center[0]+cos(theta_mid)*radius, 
                     center[1]+sin(theta_mid)*radius)
        plt.text(label_pos[0], label_pos[1], label, **label_dict)