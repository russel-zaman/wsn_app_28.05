import matplotlib.pyplot as plt
import numpy as np

def scale_coordinates(x, y, width, height):
    x_scaled = (x - np.min(x)) / (np.max(x) - np.min(x)) * width
    y_scaled = (y - np.min(y)) / (np.max(y) - np.min(y)) * height
    return x_scaled, y_scaled

#Generate x and y coordinates of the sensor nodes
mean = [1, 1]
cov = [[10, 0], [0, 10]]  # covariance matrix
x, y = np.random.multivariate_normal(mean, cov, 100).T

print(cov)
print(mean)

# plt.xlim(0, 100)
# plt.ylim(0, 100)
# Plot the sensor nodes
bsx = 50
bsy = 50
# Scale the coordinates to a 100 x 100 m area
x_scaled, y_scaled = scale_coordinates(x, y, 100, 100)

plt.grid()
plt.plot(x_scaled, y_scaled, 'b^')

# plt.grid()
# plt.plot(x, y, 'bo')
plt.plot(bsx, bsy,'r^',2)
plt.text(bsx-2, bsy-5, 'BS')
# plt.xlabel('Network Length')
# plt.ylabel('Network Height')
# plt.title('Gaussian distribution')

# Show the plot
plt.show()