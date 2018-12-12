import matplotlib.pyplot as plt
from math import exp, log
from numpy.random import uniform, exponential

SAMPLE_SIZE = 10 ** 6

A = 0.3
C = 1 / (2 * A + 2 * exp(-A))
EPS = 0

BINS = 1000

def save_plot(filename, ys):
    plt.clf()
    xs = list(range(len(ys)))
    plt.plot(xs, ys)
    plt.savefig(filename)

def save_hist(filename, xs):
    plt.clf()
    plt.hist(xs, bins=BINS)
    plt.savefig(filename)

def gen1():
    y = uniform(0, 1)
    if y + EPS < C * exp(-A):
        x = log(y / C)
    elif y > C * exp(-A) + 2 * C * A + EPS:
        x = -log((1 - y) / C)
    else:
        x = y / C - exp(-A) - A

    return x

def gen2():
    y = uniform(0, 1)
    if y + EPS < C * exp(-A):
        x = -(exponential(1) + A)
    elif y > C * exp(-A) + 2 * C * A + EPS:
        x = exponential(1) + A
    else:
        x = uniform(-A, A)

    return x

def make_graphs(gen, suffix):
    sample = [gen() for i in range(SAMPLE_SIZE)]
    sample.sort()

    save_plot("plot" + suffix, sample)
    save_hist("hist" + suffix, sample)

if __name__ == "__main__":
    make_graphs(gen1, "1")
    make_graphs(gen2, "2")