import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt('0.txt')
l=len(data)
print(l)


fig, ax = plt.subplots()
ln, = ax.plot(data)
ax.grid(True)

E = np.eye(l)
p = np.zeros((1, l - 1))
a = np.zeros((l, 1))
B = np.hstack([np.vstack([p, ((-1) * (np.eye(l - 1)).astype(np.uint8))]), a])
A = E + B
A[0][l-1]=-1

def update(frame):
    global data
    data = data - 0.5 * np.dot(A, data)
    ln.set_ydata(data)
    ax.set_title(f'Moment {frame}')
    return ln,


anim = FuncAnimation(fig, update, 255)
# anim.save('ex3.gif')
plt.show()
