# Conjunto Mandelbrot

Dado um número complexo $\xi$, ele está no *conjunto de Mandelbrot* se a sequência recursiva
$$
\begin{cases}
z_0 = 0\\
z_{n+1} = z_n^2 + \xi
\end{cases}
$$
não diverge no infinito.

# Gerador Python

Em Python, a palavra-chave "yield" é usada no contexto de funções geradoras. Uma função geradora é uma função especial que retorna um objeto iterável, o qual pode ser percorrido sequencialmente. O "yield" é usado para pausar a execução da função geradora e retornar um valor temporariamente, sem encerrar completamente a função. Essa característica permite que a função seja retomada a partir do ponto onde foi pausada, mantendo seu estado interno.

---

# Referências

1. https://realpython.com/mandelbrot-set-python/