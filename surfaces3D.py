import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Plot an elliptic paraboloid
Z = X**2 + Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Elliptic Paraboloid')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Plot an ellipsoid
a, b, c = 2, 1, 0.5
Z = (X**2 / a**2) + (Y**2 / b**2) + (Z**2 / c**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Ellipsoid')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Plot a cone
theta = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 1, 100)
Theta, R = np.meshgrid(theta, r)
Z = R
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Cone')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
