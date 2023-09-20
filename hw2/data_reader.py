import pandas as pd
from plot_maker import make_plot

values_func = pd.read_csv("hw2/functions.txt", sep="\t", header=None)
values_points = pd.read_csv("hw2/points.txt", sep="\t", header=None)
X, Y, Y_lagrange, Y_newton, Y_lagrange_cheb, Y_newton_cheb = (values_func[i] for i in range(0,6))
grid, cheb_grid, y_grid, y_cheb_grid = (values_points[i] for i in range(0,4))

fig = make_plot(X, Y, Y_lagrange, Y_newton, Y_lagrange_cheb, Y_newton_cheb, grid, cheb_grid, y_grid, y_cheb_grid)
fig.savefig("hw2/interpolation_cpp.png")