from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums',
          'Grapes', 'Strawberries', "Wood Apple", "Dragon fruit"]
counts = [5, 3, 4, 2, 4, 6, 1, 3]

p = figure(y_range=fruits, plot_height=450, title="Fruit Counts",
           toolbar_location=None, tools="")

p.hbar(y=fruits, right=counts, height=0.9)

p.ygrid.grid_line_color = "red"
p.xgrid.grid_line_color = "purple"
p.x_range.start = 0

show(p)
