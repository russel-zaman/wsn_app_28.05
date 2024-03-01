""" Shows how to use flask and matplotlib together.
Shows SVG, and png.
The SVG is easier to style with CSS, and hook JS events to in browser.
python3 -m venv venv
. ./venv/bin/activate
pip install flask matplotlib
python flask_matplotlib.py
"""
import io
import random
import matplotlib.pyplot as plt
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_svg import FigureCanvasSVG


from matplotlib.figure import Figure


app = Flask(__name__)


@app.route("/")
def index():
    """ Returns html with the img tag for your plot.
    """
    num_of_nodes = int(request.args.get("num_of_nodes", 50))
    x = int(request.args.get("x", 50))
    y = int(request.args.get("y", 50))
        
    return f"""
    <h1>WSN</h1>
    <h2>Random distribution with nodes={num_of_nodes}</h2>
    <form method=get action="/">
      <input name="num_of_nodes" type=number value="{num_of_nodes}" />
      <input name="x" type=number value="{x}" />
      <input name="y" type=number value="{y}" />
      <input type=submit value="update graph">
    </form>
    <h3>Plot as a png</h3>
    <img src="/matplot-as-image-{num_of_nodes}.png"
         alt="random points as png"
         height="200"
    >
    """

# @app.route("/matplot-as-image-<int:num_x_points>.png")
# def plot_png(num_x_points=50):
#     """ renders the plot on the fly.
#     """
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     x_points = range(num_x_points)
#     axis.plot(x_points, [random.randint(1, 40) for x in x_points])

#     output = io.BytesIO()
#     FigureCanvasAgg(fig).print_png(output)
#     return Response(output.getvalue(), mimetype="image/png")

@app.route("/matplot-as-image-<int:num_of_nodes>.png")
def plot_points(x=100, y=100,num_of_nodes=50):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_values = []
    y_values = []
    for i in range(num_of_nodes):
        x_values.append(random.randint(0, x))
        y_values.append(random.randint(0, y))
    axis.plot(x_values, y_values,'b^',2)
    axis.plot(20, 20,'r^',2)
    axis.grid()
    axis.set_title("Random Note Distribution")
    axis.set_xlabel('Network Length')
    axis.set_ylabel('Network Height')

    # axis.xticks(range(1, 200));
    # axis.yticks(range(1, 200));

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


#Run Server
if __name__ == '__main__':
    app.run('127.0.0.1', 7000, debug=True)