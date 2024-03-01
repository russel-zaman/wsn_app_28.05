import numpy as np
import matplotlib.pyplot as plt

def generate_gaussian_points(mean, std_dev, num_points):
    return np.random.normal(mean, std_dev, (num_points, 2))

# Example usage
mean = [1,1]  # Mean of the Gaussian distribution
std_dev = 1  # Standard deviation of the Gaussian distribution
num_points = 100  # Number of points to generate

points = generate_gaussian_points(mean, std_dev, num_points)

# Scale the points to the network size of 100 x 100 m
scaled_points = points * np.array([100, 100])

# Extract x and y coordinates from the scaled points
x = scaled_points[:, 0]
y = scaled_points[:, 1]

bsx = 50
bsy = 50

# Plot the points using plot method
plt.plot(x, y, 'b^')
plt.plot(bsx, bsy,'r^',2)
plt.text(bsx-2, bsy-17, 'BS')

plt.grid(True)
plt.show()

