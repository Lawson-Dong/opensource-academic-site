import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi

# Ask the user for the values of r and theta
r = float(input("Enter r: "))
d = float(input("Enter theta in degrees: "))

# Convert the angle to radians
theta = d * pi / 180

# Calculate the equivalent Cartesian coordinates
x = r * cos(theta)
y = r * sin(theta)

# Print out the results
print("x = ", x, ", y = ", y)

# Create polar coordinate plot
fig = plt.figure(figsize=(8, 8))

# Add polar subplot
ax = fig.add_subplot(111, projection='polar')

# Plot the point
ax.plot(theta, r, 'ro', markersize=10, label=f'Point: (r={r}, θ={d}°)')

# Plot the radial line from origin to the point
ax.plot([0, theta], [0, r], 'b-', linewidth=2, alpha=0.7)

# Mark the origin
ax.plot(0, 0, 'ko', markersize=5)

# Set theta zero position to East (matplotlib default is East)
ax.set_theta_zero_location('E')
ax.set_theta_direction(1)  # 1 for counterclockwise, -1 for clockwise

# Add radial gridlines
ax.set_rgrids(radii=np.arange(0, r + 1, max(1, r/5)), angle=theta*180/pi, 
              fmt='%.1f', alpha=0.5)

# Set the maximum radius
ax.set_rmax(max(r + 1, 5))

# Add labels and title
ax.set_title(f'Polar Coordinate: (r={r}, θ={d}°)', fontsize=14, pad=20)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

# Add annotation for the point
ax.annotate(f'({r}, {d}°)', 
            xy=(theta, r), 
            xytext=(theta + 0.3, r + max(0.5, r/10)),
            fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))

plt.tight_layout()
plt.show()

