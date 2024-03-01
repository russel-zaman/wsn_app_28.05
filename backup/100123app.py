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
network_data = {}
@app.route('/',methods = ['POST', 'GET'])
def main():
    fig = plot_png()
    form_data = {}
    if request.method == "POST": 
        form_data = request.form
        print(form_data['nodes_no'])
    return render_template('index.html', data1 = selectDistribution, form_data = form_data, graph_image = fig)

plt.rcParams["figure.figsize"] = [5.50, 4.50]
plt.rcParams["figure.autolayout"] = True

def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Encode PNG image to base64 string---------------
    outputB64String = "data:image/png;base64,"
    outputB64String += base64.b64encode(output.getvalue()).decode('utf8')
    return outputB64String


def create_figure(x=50, y=50, num_of_nodes=50):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_values = []
    y_values = []
    for i in range(num_of_nodes):
        x_values.append(random.randint(0, x))
        y_values.append(random.randint(0, y))
    axis.plot(x_values, y_values,'b^',2)
    axis.plot(20, 20,'r^',2)
    axis.text(19, 17, 'BS')
    axis.set_title("Random Note Distribution")
    axis.set_xlabel('Network Length')
    axis.set_ylabel('Network Height')
    axis.grid()
    return fig

#Run Server
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)