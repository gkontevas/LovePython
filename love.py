import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from matplotlib.colors import LinearSegmentedColormap


def heart_curve(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y


t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_curve(t)


fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.axis('off')


for i in range(20):
    scale = 1 - i * 0.05
    alpha = 1 - i * 0.05
    ax.plot(scale * x, scale * y, color=(1, 0, 0, alpha), linewidth=2)





plt.show()
