import matplotlib.pyplot as plt
import pandas as pd

def make_plot(X, Y_theor, Y):
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)

    ax.plot(X, Y_theor)  
    ax.plot(X, Y)
    ax.legend(["Теоретически", "Численно"])
    ax.set(xlabel = "x", ylabel = "f '(x)")

    return fig


def data_reader():
    values = pd.read_csv("hw3/functions.txt", sep="\t", header=None)
    X, Y_theor, Y = values[0], values[1], values[2]
    Z_theor, Z = values[3], values[4]

    fig1 = make_plot(X, Y_theor, Y)
    fig1.savefig("hw3/cppfigs/1deriv.png")

    fig2 = make_plot(X, Z_theor, Z)
    fig2.savefig("hw3/cppfigs/2deriv.png")


data_reader()