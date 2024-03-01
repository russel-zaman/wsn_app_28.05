from flask import Flask, render_template, request, url_for, redirect

import io
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

@app.route('/', methods = ['POST', 'GET'])
def main():
    fig = plot_png()
    form_data = {}
    if request.method == "POST": 
        form_data = request.form 
        print(form_data)
    return render_template('index.html', data1 = selectDistribution, form_data = form_data, graph_image = fig)

# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form 
#     return render_template('index.html', data1 = selectDistribution, form_data = request.form  )

#return redirect(request.referrer)
#return redirect(url_for('home', data=data))

plt.rcParams["figure.figsize"] = [5.50, 4.50]
plt.rcParams["figure.autolayout"] = True

def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Encode PNG image to base64 string---------------
    outputB64String = "data:image/png;base64,"
    outputB64String += base64.b64encode(output.getvalue()).decode('utf8')

    # plt.savefig('/static/images/new_plot.png')
    # return Response(output.getvalue(), mimetype='image/png')
    # return render_template('home.html', name = 'new_plot', url ='/static/images/new_plot.png')
    # return render_template("index.html", graph_image=outputB64String)
    return outputB64String 

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = np.random.rand(20)
    ys = np.random.rand(20)
    axis.plot(xs, ys,'b^','linewidth',2)
    axis.text(20, 5, 'matplotlib')
    axis.set_title("Random Note Distribution")
    axis.set_xlabel('Network Length')
    axis.set_ylabel('Network Height')
    axis.grid()
    # axis.plot(xs, ys,'r^','linewidth',2)
    # axis.text(22, 7,['matplotlib'])
    return fig



#Run Server
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)