# Game of Life

O **Game of Life**, também conhecido como **Life**, é um **Autómato Celular** desenvolvido pelo matemático britânico John Conway em 1970. Trata-se de um *jogo de zero jogadores*, significando que a evolução é dada somente pelo estado inicial do jogo.

## Regras

As regras são:
- Qualquer célula viva, com menos de 2 vizinhos vivos, morre por subpopulação.
- Qualquer célula viva, com 2 ou 3 vizinhos vivos, continua viva.
- Qualquer célula viva, com mais de 3 vizinhos vivos, morre por superpopulação.
- Qualquer célula morta com 3 vizinhos, nasce.

# Adição Externa

Em analogia, ao produto externo $u \otimes v$, dados dois vetores $u$ e $v$, a **adição externa** pode ser definida como

$$
u \oplus v
= 
\begin{bmatrix}
u_1 \\
u_2 \\
\vdots \\
u_m
\end{bmatrix}
+
\begin{bmatrix}
v_1 \\
v_2 \\
\vdots \\
v_n
\end{bmatrix}
= \begin{bmatrix}
u_1v_1 & u_1v_2 & \cdots & u_1v_n\\
u_2v_1 & u_2v_2 & \cdots & u_2v_n\\
\vdots & \vdots & \ddots & \vdots\\
u_mv_1 & u_mv_2 & \cdots & u_mv_n\\
\end{bmatrix}
$$

# Referências

1. Wikipedia, Outer Product.[Link](https://en.wikipedia.org/wiki/Outer_product)
