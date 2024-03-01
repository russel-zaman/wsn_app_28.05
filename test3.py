import io
import os
import random
import math
#from pandas import *
from flask import Response
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
from flask import Flask, render_template, request, url_for, redirect

# ------Random Distribution-----------------
# def plot_points(x, y, num_points):
#     x_values = []
#     y_values = []
#     for i in range(num_points):
#         x_values.append(random.randint(0, x))
#         y_values.append(random.randint(0, y))
#     plt.scatter(x_values, y_values, marker='^', color='b',)

#     plt.scatter(50, 50, marker='^', color='r',)
#     plt.text(48, 44, 'BS')
    
#     # Add labels and title
#     plt.xlabel('X-axis in m')
#     plt.ylabel('Y-axis in m')
#     #plt.title('Random Node Distribution')
#     plt.grid()
#     plt.show()

# plot_points(100, 100, 100)

# ---------- fixed points - test 2 (Read from CSV file) -----------------------

# # importing module
# from pandas import *
 
# # reading CSV file
# data = read_csv("node-data-3.csv")
 
# # converting column data to list
# x = data['x'].tolist()
# y = data['y'].tolist()

# print(x,y)
 
# plt.rcParams["figure.figsize"] = [5.50, 4.50]
# plt.rcParams["figure.autolayout"] = True

# plt.xlim(0, 300)
# plt.ylim(0, 300)

# bsx = 150
# bsy = 150
# plt.grid()
# plt.plot(x, y, 'b^')
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-4, bsy-12, 'BS')
# plt.show()

# ------ grid point -----------------

# plt.rcParams["figure.figsize"] = [5.50, 4.50]
# plt.rcParams["figure.autolayout"] = True

# plt.xlim(-5, 100+5)
# plt.ylim(-5, 100+5)

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
# bsx = 50
# bsy = 50
# plt.grid()
# plt.xlabel('X-axis in m')
# plt.ylabel('Y-axis in m')
# plt.plot(x, y, 'b^')
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-2, bsy-5, 'BS')
# plt.show()

# ---------- poisson distribution -----------------------

# def generate_poisson_samples(x_range, y_range, radius, n_samples):
#     # Initialize an empty list to store the samples
#     samples = []
    
#     # Generate the first sample randomly
#     x, y = np.random.uniform(x_range[0], x_range[1]), np.random.uniform(y_range[0], y_range[1])
#     samples.append((x, y))
    
#     # Initialize an empty list to store the active samples
#     active_samples = [0]
    
#     while active_samples:
#         # Randomly select an active sample
#         index = np.random.choice(active_samples)
#         x, y = samples[index]
        
#         # Generate a new sample within the specified radius
#         found = False
#         for _ in range(30):
#             theta = np.random.uniform(0, 2 * np.pi)
#             r = np.random.uniform(radius, 2 * radius)
#             new_x = x + r * np.cos(theta)
#             new_y = y + r * np.sin(theta)
            
#             # Check if the new sample is within the range and not too close to any existing samples
#             if x_range[0] <= new_x < x_range[1] and y_range[0] <= new_y < y_range[1]:
#                 closest_distance = min([np.hypot(new_x - s[0], new_y - s[1]) for s in samples])
#                 if closest_distance > radius:
#                     samples.append((new_x, new_y))
#                     active_samples.append(len(samples) - 1)
#                     found = True
#                     break
                    
#         # If no new sample was found, remove the active sample from the list
#         if not found:
#             active_samples.remove(index)
            
#     return samples[:n_samples]

# # Set the range and radius for the samples
# x_range = (0, 100)
# y_range = (0, 100)
# radius = 20
# n_samples = 100

# # Generate the samples
# samples = generate_poisson_samples(x_range, y_range, radius, n_samples)

# # Plot the samples
# x = [s[0] for s in samples]
# y = [s[1] for s in samples]

# bsx = 50
# bsy = 50

# plt.xlabel('X-axis in m')
# plt.ylabel('Y-axis in m')

# plt.plot(x, y, 'b^')
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-2, bsy-5, 'BS')
# plt.show()

# ---------- Gaussian distribution 1 -----------------------

import matplotlib.pyplot as plt
import numpy as np

# Generate 100 data points from a Gaussian distribution
data = np.random.normal(0, 1, 100)

# Convert the data to polar coordinates
r = data
theta = np.random.uniform(0, 2*np.pi, 100)

bsx = 50
bsy = 50

plt.xlabel('X-axis in m')
plt.ylabel('Y-axis in m')

# Plot the data in a circular shape
plt.plot(r*np.cos(theta), r*np.sin(theta),'b^',2)
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-2, bsy-5, 'BS')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Gaussian Distribution')

# Show the plot
plt.show()

# ---------- Gaussian distribution 2 -----------------------

# import matplotlib.pyplot as plt
# import numpy as np

# #Generate x and y coordinates of the sensor nodes
# mean = [50, 50]
# cov = [[100, 0], [0, 100]]  # covariance matrix
# x, y = np.random.multivariate_normal(mean, cov, 100).T

# plt.xlim(0, 100)
# plt.ylim(0, 100)
# # Plot the sensor nodes
# plt.plot(x, y, 'o',2)

# # Add labels and title
# plt.xlabel('Network Length')
# plt.ylabel('Network Height')
# plt.title('Gaussian distribution')

# # Show the plot
# plt.show()

# ---------- test 10 Read file -----------------------

# # opening the file in read mode
# my_file = open("data-points.txt", "r") 
  
# # reading the file
# data = my_file.read()
  
# # replacing end of line('/n') with ' ' and
# # splitting the text it further when '.' is seen.
# #data_into_list = data.replace('\n', '\n')

# result=[]
# for x in data:
#     result.append(x.replace(' '))
  
# # printing the data
# print(result)
# my_file.close()

# ---------- fixed points (Read from CSV file) -----------------------

# # importing the module
# import csv
 
# # open the file in read mode
# data = open('node-data.csv', 'r')
 
# # creating dictreader object
# file = csv.DictReader(data)

# # creating empty lists
# x = []
# y = []

# # iterating over each row and append values to empty list
# for col in file:
#     x.append(int(col['x']))
#     y.append(int(col['y']))
 
# # printing lists
# print('X point:', x)
# print('Y points:', y)

# data.close()

# plt.rcParams["figure.figsize"] = [5.50, 4.50]
# plt.rcParams["figure.autolayout"] = True

# plt.xlim(0, 100)
# plt.ylim(0, 100)

# bsx = 50
# bsy = 50
# plt.grid()
# plt.plot(x, y, 'bo')
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-2, bsy-5, 'BS')
# plt.show()


