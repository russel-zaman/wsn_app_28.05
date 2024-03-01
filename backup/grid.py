import io
import random
from flask import Response
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import numpy as np
from flask import Flask, render_template, request, url_for, redirect

# ------test1-----------------
# x = y = []
# for i in range(0,100):
#     x.append(i)
#     y.append(i + 1)
# plt.plot(x, y,)
# plt.show()

# ------test2-----------------
# def plot_points(x, y, num_points):
#     x_values = []
#     y_values = []
#     for i in range(num_points):
#         x_values.append(random.randint(0, x))
#         y_values.append(random.randint(0, y))
#     plt.scatter(x_values, y_values)
#     plt.show()

# plot_points(100, 100, 10)

# ------test3-----------------

# # Set the number of data points
# num_points = 10

# # Generate some random x and y values
# x = [i for i in range(num_points)]
# y = [i**2 for i in range(num_points)]

# # Plot the graph
# plt.plot(x, y)

# # Show the graph
# plt.show()

# ------mesh grid -----------------

# x = np.linspace(-4, 4, 9)
# y = np.linspace(-5, 5, 11)
# xv, yv = np.meshgrid(x, y)

# plt.plot(xv, yv, marker='o', color='k', linestyle='none')
# plt.show()

# xx, yy = np.meshgrid(np.arange(10), np.arange(10),  )
# plt.scatter(xx,yy)
# plt.show()

# ------m grid -----------------
# xv, yv = np.mgrid[-5:6, -5:6]

# plt.plot(xv, yv, marker='o', color='k', linestyle='none')
# plt.show()

# ------test 6 grid point -----------------

# x = np.random.randint(1, 14, 50)
# y = np.random.randint(1, 9, 50)

# plt.xticks(range(1, 14))
# plt.yticks(1, 9)
# plt.plot(x, y, 'bo')
# plt.grid(linestyle='dotted')
# plt.show()

# ------test 7 grid point -----------------

plt.rcParams["figure.figsize"] = [5.50, 4.50]
plt.rcParams["figure.autolayout"] = True


plt.xlim(0, 100)
plt.ylim(0, 100)


x =[]
for i in range(0, 100+20, 20):
    for j in range(6):
        x.append(i)    
# x = [0, 0, 0, 0, 0, 0, 20, 20, 20, 20, 20, 20, 40, 40, 40, 40, 40, 40, 60, 60, 60, 60, 60, 60, 80, 80, 80, 80, 80, 80, 100, 100, 100, 100, 100, 100]
y =[]
for i in range(6):
    for j in range(0, 100+20, 20):
        y.append(j)
# y = [0, 20, 40, 60, 80, 100, 0, 20, 40, 60, 80, 100, 0, 20, 40, 60, 80, 100, 0, 20, 40, 60, 80, 100, 0, 20, 40, 60, 80, 100, 0, 20, 40, 60, 80, 100]

bsx = 50
bsy = 50
plt.grid()
plt.plot(x, y, 'bo')
plt.plot(bsx, bsy,'r^',2)
plt.text(bsx-2, bsy-5, 'BS')
plt.show()

# ---------------------------------
# x =[]
# for i in range(0, 100+20, 20):
#     for j in range(6):
#         x.append(i)    

# y =[]
# for i in range(6):
#     for j in range(0, 100+20, 20):
#         y.append(j)

# print(x)
# print(y)