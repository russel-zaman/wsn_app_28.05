import matplotlib.pyplot as plt

# Data for the first figure
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Data for the second figure
x2 = [1, 2, 3, 4, 5]
y2 = [3, 6, 9, 12, 15]

# Data for the third figure
x3 = [1, 2, 3, 4, 5]
y3 = [4, 8, 12, 16, 20]

# Data for the fourth figure
x4 = [1, 2, 3, 4, 5]
y4 = [5, 10, 15, 20, 25]

# Data for the fifth figure
x5 = [1, 2, 3, 4, 5]
y5 = [6, 12, 18, 24, 30]

# Creating subplots
plt.subplot(3, 2, 1)
plt.plot(x1, y1)
plt.title("First Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(3, 2, 2)
plt.plot(x2, y2)
plt.title("Second Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(3, 2, 3)
plt.plot(x3, y3)
plt.title("Third Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(3, 2, 4)
plt.plot(x4, y4)
plt.title("Fourth Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(3, 2, 5)
plt.plot(x5, y5)
plt.title("Fifth Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.tight_layout()
plt.show()