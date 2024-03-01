import io
import os
import random
import math
from pandas import *
from flask import Response
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
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

# plt.rcParams["figure.figsize"] = [5.50, 4.50]
# plt.rcParams["figure.autolayout"] = True

# plt.xlim(0, 100)
# plt.ylim(0, 100)

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
# plt.plot(x, y, 'bo')
# plt.plot(bsx, bsy,'r^',2)
# plt.text(bsx-2, bsy-5, 'BS')
# plt.show()

# ---------- Gaussian distribution 1 -----------------------

# import matplotlib.pyplot as plt
# import numpy as np

# # Generate 100 data points from a Gaussian distribution
# data = np.random.normal(0, 1, 100)

# # Convert the data to polar coordinates
# r = data
# theta = np.random.uniform(0, 2*np.pi, 100)

# # Plot the data in a circular shape
# plt.plot(r*np.cos(theta), r*np.sin(theta),'r^',2)

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Gaussian Distribution')

# # Show the plot
# plt.show()

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

# ---------- fixed points - test 2 (Read from CSV file) -----------------------

# # importing module
# from pandas import *
 
# # reading CSV file
# data = read_csv("node-data.csv")
 
# # converting column data to list
# x = data['x'].tolist()
# y = data['y'].tolist()

# print(x,y)
 
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

# ---------- poisson distribution -----------------------

# import numpy as np
# import matplotlib.pyplot as plt

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
# radius = 10
# n_samples = 100

# # Generate the samples
# samples = generate_poisson_samples(x_range, y_range, radius, n_samples)

# # Plot the samples
# x = [s[0] for s in samples]
# y = [s[1] for s in samples]
# plt.scatter(x, y)
# plt.show()

#-----------------

# import random
# import matplotlib.pyplot as plt

xm = 100
ym = 100
x = 0
y = 0

n=100
dead_nodes=0

sinkx = 50
sinky = 200

Eo = 2
Eelec = 50 * 10**(-9)
ETx = 50 * 10**(-9)
ERx = 50 * 10**(-9)
Eamp = 100 * 10**(-12)
EDA = 5 * 10**(-9)
k = 4000
p = 0.05
No = int(p * n)
rnd = 0

operating_nodes = n
transmissions = 0
temp_val = 0
flag1stdead = 0

tr = []
op = []
nrg =[]
avg_node =[]
CL = []
SN = []

for i in range(n):
    sn = dict()
    sn["id"] = i
    sn["x"] = random.random() * xm
    sn["y"] = random.random() * ym
    sn["E"] = Eo
    sn["role"] = 0
    sn["cluster"] = 0
    sn["cond"] = 1
    sn["rop"] = 0
    sn["rleft"] = 0
    sn["dtch"] = 0
    sn["dts"] = 0
    sn["tel"] = 0
    sn["rn"] = 0
    sn["chid"] = 0
    SN.append(sn)
    
    plt.plot(x, y, xm, ym, SN[i]["x"], SN[i]["y"], 'ob', sinkx, sinky, '*r')

plt.figure(1)
plt.title("Wireless Sensor Network")
plt.xlabel("(m)")
plt.ylabel("(m)")
plt.show()

while operating_nodes > 0:
    t = p / (1 - p * (rnd % (1/p)))
    tleft = rnd % (1/p)
    CLheads = 0
    energy = 0

    for i in range(n):
        SN.append({
            'cluster': 0,
            'role': 0,
            'chid': 0,
        })
        if SN[i]['rleft'] > 0:
            SN[i]['rleft'] -= 1
        if SN[i]['E'] > 0 and SN[i]['rleft'] == 0:
            generate = random.random()
            if generate < t:
                SN[i]['role'] = 1
                SN[i]['rn'] = random.random()
                SN[i]['tel'] += 1
                SN[i]['rleft'] = 1/p - tleft
                SN[i]['dts'] = math.sqrt((sinkx - SN[i]['x'])**2 + (sinky - SN[i]['y'])**2)
                CLheads += 1
                SN[i]['cluster'] = CLheads
                CL.append({
                    'x': SN[i]['x'],
                    'y': SN[i]['y'],
                    'id': i
                })


    CL = CL[:CLheads]
    for i in range(n):
        if SN[i]['role'] == 0 and SN[i]['E'] > 0 and CLheads > 0:
            d = [0] * CLheads
            for m in range(CLheads):
                d[m] = math.sqrt((CL[m]['x'] - SN[i]['x']) ** 2 + (CL[m]['y'] - SN[i]['y']) ** 2)
            
            d = d[:CLheads]
            M = min(d)
            I = d.index(M)
            Row, Col = divmod(I, len(d))
            SN[i]['cluster'] = Col
            SN[i]['dtch'] = d[Col]
            SN[i]['chid'] = CL[Col]['id']


    for i in range(n):
        if (SN[i]['cond'] == 1) and (SN[i]['role'] == 0) and (CLheads > 0):
            if SN[i]['E'] > 0:
                ETx = Eelec * k + Eamp * k * SN[i]['dtch']**2
                SN[i]['E'] = SN[i]['E'] - ETx
                energy = energy + ETx
                
                if SN[SN[i]['chid']]['E'] > 0 and SN[SN[i]['chid']]['cond'] == 1 and SN[SN[i]['chid']]['role'] == 1:
                    ERx = (Eelec + EDA) * k
                    energy = energy + ERx
                    SN[SN[i]['chid']]['E'] = SN[SN[i]['chid']]['E'] - ERx
                    if SN[SN[i]['chid']]['E'] <= 0:
                        SN[SN[i]['chid']]['cond'] = 0
                        SN[SN[i]['chid']]['rop'] = rnd
                        dead_nodes += 1
                        operating_nodes -= 1
                        
            if SN[i]['E'] <= 0:
                dead_nodes += 1
                operating_nodes -= 1
                SN[i]['cond'] = 0
                SN[i]['chid'] = 0
                SN[i]['rop'] = rnd


    for i in range(n):
        if SN[i]["cond"] == 1 and SN[i]["role"] == 1:
            if SN[i]["E"] > 0:
                ETx = (Eelec + EDA) * k + Eamp * k * SN[i]["dts"]**2
                SN[i]["E"] = SN[i]["E"] - ETx
                energy += ETx
            if SN[i]["E"] <= 0:
                dead_nodes += 1
                operating_nodes -= 1
                SN[i]["cond"] = 0
                SN[i]["rop"] = rnd


    if operating_nodes < n and temp_val == 0:
        temp_val = 1
        flag1stdead = rnd

    transmissions += 1
    if CLheads == 0:
        transmissions -= 1

    rnd += 1
    # tr.append(transmissions)
    # op.append(operating_nodes)

    # tr = [0] * (transmissions + 1)
    #tr[transmissions] = operating_nodes
    # op = [0] * (rnd + 1)
    #op[rnd] = operating_nodes

    for i in range(n):
        tr.append(operating_nodes)
    tr[transmissions] = operating_nodes

    for i in range(n):
        op.append(operating_nodes)
    op[rnd] = operating_nodes

    if energy > 0:
        # nrg.append(energy)
        # nrg = [0] * (transmissions + 1)
        # nrg[transmissions] = energy

        for i in range(n):
            nrg.append(energy)
        nrg[transmissions] = energy

sum = 0
for i in range(flag1stdead):
    sum += nrg[i]

temp1 = sum / flag1stdead
temp2 = temp1 / n

for i in range(flag1stdead):
    # avg_node.append(temp2)
    # avg_node = [0] * (i + 1)
    # avg_node[i] = temp2

    for i in range(flag1stdead):
        avg_node.append(temp2)
    avg_node[i] = temp2

# Plotting Simulation Results "Operating Nodes per Round"
plt.figure(2)
plt.plot(range(1, rnd), op[1:rnd], '-r', linewidth=2)
plt.title("LEACH Operating Nodes per Round")
plt.xlabel("Rounds")
plt.ylabel("Operational Nodes")
# plt.hold(True)

# Plotting Simulation Results
plt.figure(3)
plt.plot(range(1, transmissions), tr[1:transmissions], '-r', linewidth=2)
plt.title("LEACH Operational Nodes per Transmission")
plt.xlabel("Transmissions")
plt.ylabel("Operational Nodes")
# plt.hold(True)

# Plotting Simulation Results
plt.figure(4)
plt.plot(range(1, flag1stdead), nrg[1:flag1stdead], '-r', linewidth=2)
plt.title("LEACH Energy consumed per Transmission")
plt.xlabel("Transmission")
plt.ylabel("Energy (J)")
# plt.hold(True)

test_flag1stdead = 809
print(len(avg_node))
# Plotting Simulation Results
plt.figure(5)
plt.plot(range(1, test_flag1stdead), avg_node[1:test_flag1stdead], '-r', linewidth=2)
plt.title("LEACH Average Energy consumed by a Node per Transmission")
plt.xlabel("Transmissions")
plt.ylabel("Energy (J)")
# plt.hold(True)

plt.show()


