from flask import Flask, render_template, request, url_for, redirect
from pandas import *
import io
import os
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
def forms():
    form_data = {}
    if request.method == "POST":
        if "form1_submit" in request.form:
            return upload()
        elif "form2_submit" in request.form:
            return main()
    else:
        print("waiting for data from user input")
        fig = plot_blank()

    return render_template('fixed.html', data1 = selectDistribution, form_data = form_data, graph_image = fig )

@app.route('/', methods=['POST'])
def upload():
    global csv_data 
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join("static/files", filename))
    data = os.path.join("static/files", filename)
    csv_data = read_csv(data)
    print(csv_data)

    return redirect(request.url)

@app.route('/',methods = ['POST', 'GET'])
def main():   
    form_data = {}
    if request.method == "POST": 
        form_data = request.form

    if bool(form_data):
        print("Dictionary Contains Data!")
        x = int(form_data['net_size_x'])
        y = int(form_data['net_size_y'])
        bsx = int(form_data['bs_x'])
        bsy = int(form_data['bs_y'])
        fig = plot_png(x, y, bsx, bsy)
    else:
        print("No input data")
    
    # fig = plot_blank()
    return render_template('fixed.html', data1 = selectDistribution, form_data = form_data, graph_image = fig )

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

def plot_png(xx, yy, bsx, bsy):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    # converting column data to list
    xx = csv_data['x'].tolist()
    yy = csv_data['y'].tolist()

    axis.plot(xx, yy,'b^',2)

    axis.plot(bsx, bsy,'r^',2)
    axis.text(bsx-2, bsy-5, 'BS')
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
    app.run('127.0.0.1', 7000, debug=True)