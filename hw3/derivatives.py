import numpy as np
import matplotlib.pyplot as plt

# область определения [-3, 3]
def f(x):
    return np.arctan(np.sin(x))


# первая производная функции в аналитическом виде
def g1(x):
    return np.cos(x) / (np.sin(x)**2 + 1)


# вторая производная в аналитическом виде
def g2(x):
    return -np.sin(x)*(np.sin(x)**2 + 2*np.cos(x)**2 + 1) / (np.sin(x)**2 + 1)**2


def first_deriv(X, h, i):
    if i == 0:
        return (-3 * f(X[0]) + 4 * f(X[1]) - f(X[2])) / (2 * h)
    
    if i == len(X) - 1:
        return (3 * f(X[-1]) - 4 * f(X[-2]) + f(X[-3])) / (2 * h)
    
    return (f(X[i+1]) - f(X[i-1]))/(2*h)


def second_deriv(X, h, i):
    if i == 0:
        return (f(X[0]) - 2 * f(X[1]) + f(X[2])) / (h**2)
    
    if i == len(X) - 1:
        return (f(X[-3]) - 2 * f(X[-2]) + f(X[-1])) / (h**2)
    
    return (f(X[i+1]) - 2*f(X[i]) + f(X[i-1]))/(h**2)


def resid(X, F_deriv, goo):
    res = 0
    for i in range(len(X)):
        dif = abs(F_deriv[i] - goo(X[i]))
        if dif > res:
            res = dif
    return res


# строим график производной при заданном h
def plot_deriv(h, foo, goo):
    a, b = -3, 3
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    n = (b - a) / h + 1
    X = np.linspace(a, b, int(n))
    F_deriv = []
    for i in range(int(n)):
        F_deriv.append(foo(X, h, i))

    X0 = np.linspace(a, b, 100000)
    G = [goo(x) for x in X0]

    ax.plot(X0, G)  
    ax.plot(X, F_deriv)
    ax.legend(["Теоретически", "Численно"])
    ax.set(xlabel = "x", ylabel = "g(x)")
    return fig


# строим графики производной и погрешности для разных h
def make_h_dynamics(foo, goo):
    a, b = -3, 3
    legend = []
    resids1 = []

    fig1 = plt.figure()
    ax1 = plt.subplot(1, 1, 1)
    H = [10e-1, 10e-2, 10e-3, 10e-4, 10e-5]
    for h in H:
        n = (b - a) / h + 1
        X = np.linspace(a, b, int(n))
        F_deriv1 = []
        for i in range(int(n)):
            F_deriv1.append(foo(X, h, i))

        resids1.append(resid(X, F_deriv1, goo))
        
        ax1.plot(X, F_deriv1)
        legend.append(f"h = {h}")

    X = np.linspace(a, b, 100000)
    G1 = [goo(x) for x in X]     # истинные значения первой производной в узлах
    
    ax1.plot(X, G1)
    ax1.legend(legend + ["Теоретически"])
    ax1.set(xlabel = "x", ylabel = "f '(x)")
    #fig1.savefig("hw3/figs/first_derivative.png")

    fig2 = plt.figure()
    ax2 = plt.subplot(1, 1, 1)

    ax2.scatter(H, resids1)
    ax2.plot(H, resids1)
    ax2.set(xlabel = "h", ylabel = "R(h)")
    #fig2.savefig("hw3/figs/resids1.png")

    return fig1, fig2, resids1


def main():
    h = 10e-5

    fig_deriv1 = plot_deriv(h, first_deriv, g1)     # строим график первой производной
    fig_deriv1.savefig("hw3/figs/1deriv.png")
    _, _, resids1 = make_h_dynamics(first_deriv, g1)
    print("Погрешности первой производной: ", resids1)

    fig_deriv2 = plot_deriv(h, second_deriv, g2)     # строим график второй производной
    fig_deriv2.savefig("hw3/figs/2deriv.png")
    _, _, resids2 = make_h_dynamics(second_deriv, g2)
    print("Погрешности второй производной: ", resids2)


main()
