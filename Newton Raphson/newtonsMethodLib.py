def solve(f, df, x0, no_iterations = 10, show_progress = False):
    x = x0
    for i in range(no_iterations):
        if show_progress:
            print(f"Progresso: {i/no_iterations*100:.0f}%")
        x = x - f(x)/df(x)
            
    return x

# Generator
def solve_gen(f, df, x0):
    x = x0
    while True:
        x = x - f(x)/df(x)
        yield x