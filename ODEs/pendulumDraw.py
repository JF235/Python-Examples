from pendulumLib import *

# Configuracoes inicias
plt.rcParams["mathtext.fontset"] = "cm"
plt.ylim(3, 10)
plt.xlim(0, 10)
plt.gca().set_aspect('equal')

# Pendulos
P = (5, 10) # fixed point
length = 4 # length
for angle in [-45, 0, 45]:
    draw_pendulum(P, length, angle, zorder=3)

# Arcos
draw_arc(P, 1, 270, 360-45, r"$\theta$",
         label_dict=dict(fontsize=16, verticalalignment="top"))

# Vetores
# Vetor de forca
Q = get_pendulum_coords(P, length, -45)
draw_vector((0, -2), Q, label = r"$\vec{F}_g$",
            dx = .2, dy = -.2,
            arrowhead_dict=dict(markersize=12),
            segment_dict=dict(lw=2),
            label_dict=dict(fontsize=16),
            color='tab:blue', zorder=2)
# Vetor de braco
r = get_vector(P, Q, scale=.89)
draw_vector(r, P, label = r"$\vec{r}$",
            dx = 0, dy = -.5,
            arrowhead_dict=dict(markersize=12),
            segment_dict=dict(lw=2),
            label_dict=dict(fontsize=16),
            color='tab:orange', zorder=3)

plt.title("Pendulum Dynamics")
plt.tight_layout()
plt.savefig("LorenzAttractor/imgs/pendulumDraw01.jpeg", dpi=300)
plt.show()