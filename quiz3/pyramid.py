import numpy as np
import matplotlib.pyplot as plt


def pyramid(n, height):

    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)

    radius_base = 1.0
    radius_apex = 0.0

    x_base = radius_base * np.cos(theta)
    y_base = radius_base * np.sin(theta)
    z_base = np.zeros_like(x_base)

    x_apex = np.zeros_like(theta)
    y_apex = np.zeros_like(theta)
    z_apex = height * np.ones_like(theta)

    x_coords = np.array([x_base, x_apex])
    y_coords = np.array([y_base, y_apex])
    z_coords = np.array([z_base, z_apex])

    return x_coords, y_coords, z_coords


if __name__ == '__main__':
    fig = plt.figure(tight_layout=True)

    ax = fig.add_subplot(121, projection='3d')
    x, y, z = pyramid(4, 5)
    ax.contour3D(x, y, z, 50)
    ax.set_title("Square Pyramid")

    ax = fig.add_subplot(122, projection='3d')
    x, y, z = pyramid(6, 10)
    ax.contour3D(x, y, z, 50)
    ax.set_title("Hexagonal Pyramid")

    plt.show()
