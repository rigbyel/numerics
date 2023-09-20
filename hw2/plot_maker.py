import matplotlib.pyplot as plt

def make_plot(X, Y, Y_lagrange, Y_newton, Y_lagrange_cheb, Y_newton_cheb, grid, cheb_grid, y_grid, y_cheb_grid):
    fig = plt.figure(figsize=(15, 10))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.plot(X, Y)
    ax1.plot(X, Y_lagrange)
    ax1.plot(X, Y_newton)
    ax1.scatter(grid, y_grid, zorder=5)
    ax1.set_title("Равномерная сетка")
    ax1.set(xlabel = "x", ylabel = "f(x)")

    ax2.plot(X, Y)
    ax2.plot(X, Y_lagrange_cheb)
    ax2.plot(X, Y_newton_cheb)
    ax2.scatter(cheb_grid, y_cheb_grid, zorder=5)
    ax2.set_title("Узлы Чебышева")
    ax2.set(xlabel = "x", ylabel = "f(x)")

    fig.legend(["Истинная функция", "Полином Лагранжа", "Полином Ньютона"])

    return fig
