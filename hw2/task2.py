import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(np.exp(x / 3) / 10)


def coef_lagr(x, grid, i):
    xi = grid[i]
    new_grid = np.delete(grid, np.where(grid == xi))
    prod = 1

    for xj in new_grid:
        prod *= (x - xj) / (xi - xj)

    return prod


def lagr_polynom(x, grid, n):
    sum = 0

    for i in range(0, n):
        sum += f(grid[i]) * coef_lagr(x, grid, i)

    return sum

n = 20
grid = np.linspace(0, 10, n)
X = np.linspace(0, 10, 1000)

Y = [f(x) for x in X]
Y_interpol = [lagr_polynom(x, grid, n) for x in grid]


plt.plot(X, Y)
plt.plot(grid, Y_interpol)
plt.scatter(grid, [f(x) for x in grid], zorder=5)
plt.legend(["Истинная функция", "Полином Лагранжа"])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("hw2/interpolation.png")