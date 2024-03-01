import matplotlib.pyplot as plt
import numpy as np

#Generate x and y coordinates of the sensor nodes
mean = [5, 5]
cov = [[10, 0], [0, 10]]  # covariance matrix
x, y = np.random.multivariate_normal(mean, cov, 200).T

print(cov)
print(mean)

# plt.xlim(0, 100)
# plt.ylim(0, 100)
# Plot the sensor nodes
# bsx = 50
# bsy = 50
plt.grid()
plt.plot(x, y, 'bo')
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-2, bsy-5, 'BS')
plt.xlabel('Network Length')
plt.ylabel('Network Height')
plt.title('Gaussian distribution')

# Show the plot
plt.show()