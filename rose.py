import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def rose_curve(n, d):
    theta = np.linspace(0, 2 * np.pi, 1000)
    k = n / d
    r = np.sin(k * theta)

    return theta, r


# Set the initial parameters for the rose curve
initial_n = 1
initial_d = 1

# Generate the initial rose curve
theta, r = rose_curve(initial_n, initial_d)

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=0.15, bottom=0.25)

# Plot the initial rose curve
line, = ax.plot(x, y, color='red')
ax.axis('equal')
ax.set_title(f'Rose Curve: n = {initial_n}, d = {initial_d}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)

# Adjust the axis limits based on the maximum value of r
max_r = np.max(np.abs(r))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create the sliders
ax_n = plt.axes([0.15, 0.1, 0.7, 0.03])
ax_d = plt.axes([0.15, 0.05, 0.7, 0.03])

slider_n = Slider(ax=ax_n, label='n', valmin=1,
                  valmax=9, valstep=1, valinit=initial_n)
slider_d = Slider(ax=ax_d, label='d', valmin=1,
                  valmax=9, valstep=1, valinit=initial_d)

# Update the plot when the sliders are changed


def update(val):
    n = int(slider_n.val)
    d = int(slider_d.val)
    theta, r = rose_curve(n, d)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    line.set_xdata(x)
    line.set_ydata(y)
    ax.set_title(f'Rose Curve: n = {n}, d = {d}')
    fig.canvas.draw_idle()


slider_n.on_changed(update)
slider_d.on_changed(update)

plt.show()
