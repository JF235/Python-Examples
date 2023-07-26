import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def add_glider(X, i, j):
    glider = np.array([
     [0, 0, 1],
     [1, 0, 1],   
     [0, 1, 1],   
    ])
    X[i:i+3, j:j+3] = glider

def apply_rule(X, s):
    newX = X.copy()
    for i in range(s):
        for j in range(s):
            # Toroidal neighbor
            total = int((X[i, (j-1)%s] + X[i, (j+1)%s] +
                         X[(i-1)%s, j] + X[(i+1)%s, j] +
                         X[(i-1)%s, (j-1)%s] + X[(i-1)%s, (j+1)%s] +
                         X[(i+1)%s, (j-1)%s] + X[(i+1)%s, (j+1)%s]))
            
            # Game Of Life Rules
            if X[i, j]  == 1:
                if (total < 2) or (total > 3):
                    newX[i, j] = 0
            else:
                if total == 3:
                    newX[i, j] = 1
    return newX


def update(frameNo, X, img, s, totalFrames):
    X[:] = apply_rule(X, s)
    img.set_data(X)
    print(f"{int(frameNo/totalFrames*100):02d}%\b\b\b", end="\r")
    return img,

s = 100
#X = np.zeros([s, s])
#add_glider(X, 4, 4)
np.random.seed(11)
X = np.random.randint(1, 11, (s, s))
X = (X < 3).astype(int)

# Plotting
fig, ax = plt.subplots()
img = ax.imshow(X, cmap='binary')
plt.xticks(np.arange(-.5, s, 1), [])
plt.yticks(np.arange(-.5, s, 1), [])
plt.xlim(-.5, s-.5)
plt.ylim(-.5, s-.5)
# plt.grid(linewidth=2)

totalFrames = 120*5
ani = animation.FuncAnimation(fig, update, frames=totalFrames, fargs=[X, img, s, totalFrames], repeat=True)
# repeat = True, garante que a animação roda em Loop Infinito
ani.save('animation.mp4', fps=12)
print()
plt.show()