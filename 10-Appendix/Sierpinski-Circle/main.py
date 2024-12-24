import matplotlib.pyplot as plt
import numpy as np

def sierpinski_circle(ax, x, y, radius, depth):
    if depth == 0:
        circle = plt.Circle((x, y), radius, edgecolor='black', facecolor='none')
        ax.add_artist(circle)
    else:
        sierpinski_circle(ax, x, y, radius / 2, depth - 1)
        sierpinski_circle(ax, x - radius / 2, y, radius / 2, depth - 1)
        sierpinski_circle(ax, x + radius / 2, y, radius / 2, depth - 1)
        sierpinski_circle(ax, x, y - radius / 2, radius / 2, depth - 1)
        sierpinski_circle(ax, x, y + radius / 2, radius / 2, depth - 1)

# Parameters
depth = 4
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

# Draw the Sierpinski Circle
sierpinski_circle(ax, 0, 0, 1, depth)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
plt.title('Sierpinski Circle')
plt.show()
