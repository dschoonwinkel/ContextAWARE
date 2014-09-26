# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
# #                       np.arange(-0.8, 1, 0.2),
# #                       np.arange(-0.8, 1, 0.8))

# # u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
# # v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
# # w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
# #      np.sin(np.pi * z))
# x = 0
# y = 0
# z = 0
# u = 1
# v = 1
# w = 1

# ax.quiver(x, y, z, u, v, w, length=0.1)

# plt.show()

# First import everthing you need
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Create some random data, I took this piece from here:
# http://matplotlib.org/mpl_examples/mplot3d/scatter3d_demo.py
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin
n = 100
xx = randrange(n, 23, 32)
yy = randrange(n, 0, 100)
zz = randrange(n, -50, -25)

# Create a figure and a 3D Axes
fig = plt.figure()
ax = Axes3D(fig)

# Create an init function and the animate functions.
# Both are explained in the tutorial. Since we are changing
# the the elevation and azimuth and no objects are really
# changed on the plot we don't have to return anything from
# the init and animate function. (return value is explained
# in the tutorial.
def init():
    x = np.linspace(0, 100, 100)
    y = np.linspace(0, 100, 100)
    ax.scatter(xx, yy, zz, marker='o', s=20, c="goldenrod", alpha=0.6)

def animate(i):
    ax.view_init(elev=10., azim=i)

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=False)
# Save
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])