import numpy as np
import matplotlib.pyplot as plt
from bvp_solver import solve_bvp

# функции - коэффициенты в дифференциальном уравнение
def p(x):
    return np.tan(x)

def q(x):
    return -2*x / np.cos(x)

def f(x):
    return 2 - 2*x**3 / np.cos(x)


# теоретическое решение задачи
def u_theor(x):
    return np.sin(x) + x**2


def main():
    
    # параметры задачи
    a = 0
    b = 1
    h = 0.05
    n = int((b-a) / h + 1)

    # коэффиценты в граничных условиях
    # для левой границы
    alpha_a = 2
    beta_a = -1
    gamma_a = -1

    # для правой границы
    alpha_b = 3
    beta_b = 1
    gamma_b = 8.0647

    # решаем задачу методом конечных разностей
    sol = solve_bvp(a, b, h, p, q, f, (alpha_a, alpha_b), 
                    (beta_a, beta_b), (gamma_a, gamma_b),
                     precision=1)

    # построение графика теоретического решения
    X = np.linspace(a,b,1000)
    sol_theor = [u_theor(x) for x in X]
    plt.plot(X, sol_theor, label="theoretical")

    # построение графика численного решения
    grid = np.linspace(a, b, n)
    plt.plot(grid, sol, label="numerical")


    plt.legend()
    plt.savefig("bvp.png")

main()