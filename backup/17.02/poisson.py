from flask import Flask, render_template, request, url_for, redirect

import io
import random
import base64
import numpy as np
from flask import Response
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Init app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yourSecretKey'

selectDistribution=[{'distribution': 'random'}, {'distribution': 'gaussian'}, {'distribution': 'grid'}, {'distribution': 'fixed'}]

def generate_poisson_samples(x_range, y_range, radius, n_samples):
    # Initialize an empty list to store the samples
    samples = []
    
    # Generate the first sample randomly
    x, y = np.random.uniform(x_range[0], x_range[1]), np.random.uniform(y_range[0], y_range[1])
    samples.append((x, y))
    
    # Initialize an empty list to store the active samples
    active_samples = [0]
    
    while active_samples:
        # Randomly select an active sample
        index = np.random.choice(active_samples)
        x, y = samples[index]
        
        # Generate a new sample within the specified radius
        found = False
        for _ in range(30):
            theta = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(radius, 2 * radius)
            new_x = x + r * np.cos(theta)
            new_y = y + r * np.sin(theta)
            
            # Check if the new sample is within the range and not too close to any existing samples
            if x_range[0] <= new_x < x_range[1] and y_range[0] <= new_y < y_range[1]:
                closest_distance = min([np.hypot(new_x - s[0], new_y - s[1]) for s in samples])
                if closest_distance > radius:
                    samples.append((new_x, new_y))
                    active_samples.append(len(samples) - 1)
                    found = True
                    break
                    
        # If no new sample was found, remove the active sample from the list
        if not found:
            active_samples.remove(index)
            
    return samples[:n_samples]

@app.route('/',methods = ['POST', 'GET'])
def main():   
    form_data = {}
    if request.method == "POST": 
        form_data = request.form

    if bool(form_data):
        print("Dictionary Contains Data!")
        x = int(form_data['net_size_x'])
        y = int(form_data['net_size_y'])
        nodes_no = int(form_data['nodes_no'])
        bsx = int(form_data['bs_x'])
        bsy = int(form_data['bs_y'])
        r = int(form_data['n_radius'])
        fig = plot_png(x, y, r, nodes_no, bsx, bsy)
    else:
        print("Dictionary Empty!")
        fig = plot_blank()
    
    # fig = plot_blank()
    return render_template('poisson.html', data1 = selectDistribution, form_data = form_data, graph_image = fig )

plt.rcParams["figure.figsize"] = [5.50, 4.50]
plt.rcParams["figure.autolayout"] = True

def plot_blank():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot()
    axis.set_title("Network Distribution title")
    axis.set_xlabel('Network Length')
    axis.set_ylabel('Network Height')
    axis.grid()

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Encode PNG image to base64 string---------------
    outputB64String = "data:image/png;base64,"
    outputB64String += base64.b64encode(output.getvalue()).decode('utf8')
    return outputB64String

def plot_png(x, y, r, nodes_no, bsx, bsy):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    x_range = (0, x)
    y_range = (0, y)
    radius = r
    n_samples = nodes_no

    # Generate the samples
    samples = generate_poisson_samples(x_range, y_range, radius, n_samples)
    # Plot the samples
    x_values = [s[0] for s in samples]
    y_values = [s[1] for s in samples]

    axis.plot(x_values, y_values,'b^',2)

    axis.plot(bsx, bsy,'r^',2)
    axis.text(bsx+10, bsy-15, 'BS')
    axis.set_title("Random Node Distribution")
    axis.set_xlabel('Network Length')
    axis.set_ylabel('Network Height')
    axis.grid()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Encode PNG image to base64 string---------------
    outputB64String = "data:image/png;base64,"
    outputB64String += base64.b64encode(output.getvalue()).decode('utf8')
    return outputB64String



#Run Server
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)