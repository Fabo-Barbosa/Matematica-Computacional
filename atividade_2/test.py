import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0, 10, 200)

# Lista de funções (quadros)
funcoes = [
    lambda x: np.sin(x),
    lambda x: np.cos(x),
    lambda x: np.sin(2*x),
    lambda x: np.cos(2*x)
]

def update(frame):
    ax.clear()
    ax.plot(x, funcoes[frame](x))
    ax.set_title(f"Slide {frame+1}")

ani = FuncAnimation(fig, update, frames=len(funcoes), interval=1500, repeat=True)

plt.show()
