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


def lagr_polynom(x, grid):
    sum = 0
    for i in range(0, len(grid)):
        sum += f(grid[i]) * coef_lagr(x, grid, i)
    return sum


def divided_diff(grid):
    sum = 0
    if len(grid) == 1:
        return f(grid[0])
    
    for i in range(0,len(grid)):
        prod = 1
        for j in range(0, len(grid)):
            if j != i:
                prod *= (grid[i] - grid[j])
        sum += f(grid[i]) / prod
    return sum


def coef_newton(i, grid):
    return divided_diff(grid[0:i+1])


def newton_polynom(x, i, grid):
    if i == len(grid) - 1:
        return coef_newton(i-1, grid) + (x - grid[i-1]) * coef_newton(i, grid)
    return newton_polynom(x, i + 1, grid) * (x - grid[i-1]) +  coef_newton(i-1, grid)
        

def cheb_points(j, a, b, n):
    return (a + b) / 2 + (b - a) * np.cos((2*j+1) * np.pi / (2*n)) / 2


n = 20
a = 0
b = 10

grid = np.linspace(a, b, n)
cheb_grid = [cheb_points(j, a, b, n) for j in range(0,n)]
X = np.linspace(0, 10, 1000)

Y = [f(x) for x in X]
Y_lagrange = [lagr_polynom(x, grid) for x in grid]
Y_newton = [newton_polynom(x, 1, grid) for x in grid]

Y_lagrange_cheb = [lagr_polynom(x, grid) for x in cheb_grid]
Y_newton_cheb = [newton_polynom(x, 1, grid) for x in cheb_grid]


fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(X, Y)
ax1.plot(grid, Y_lagrange)
ax1.plot(grid, Y_newton)
ax1.scatter(grid, [f(x) for x in grid], zorder=5)
ax1.set_title("Равномерная сетка")
ax1.set(xlabel = "x", ylabel = "f(x)")

ax2.plot(X, Y)
ax2.plot(cheb_grid, Y_lagrange_cheb)
ax2.plot(cheb_grid, Y_newton_cheb)
ax2.scatter(cheb_grid, [f(x) for x in cheb_grid], zorder=5)
ax2.set_title("Узлы Чебышева")
ax2.set(xlabel = "x", ylabel = "f(x)")

fig.legend(["Истинная функция", "Полином Лагранжа", "Полином Ньютона"])
fig.savefig("hw2/interpolation.png")
