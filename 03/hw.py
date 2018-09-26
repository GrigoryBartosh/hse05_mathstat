import math
import random

import matplotlib.pyplot as plot

THETA = 1
SAMPLE_SIZE = 100
ITRS = 1000
K_FROM = 1
K_TO = 100

def compute_plot(distr, estim):
    ks = list(range(K_FROM, K_TO + 1))

    devs = []
    for k in ks:
        dev_sum = 0
        for itr in range(ITRS):
            sample = [distr() for _ in range(SAMPLE_SIZE)]
            mean = sum(map(lambda x: x ** k, sample)) / SAMPLE_SIZE
            dev_sum += (THETA - estim(mean, k)) ** 2
        devs.append(dev_sum / ITRS)

    return ks, devs

def save_plot(name, xs, ys):
    plot.clf()
    plot.plot(xs, ys)
    plot.savefig(name)

def build_plot(name, distr, estim):
    xs, ys = compute_plot(distr, estim)
    save_plot(name, xs, ys)

if __name__ == '__main__':
    build_plot("uniform",
                lambda: random.uniform(0, THETA),
                lambda x, k: (x * (k + 1)) ** (1 / k))

    build_plot("exponential",
                lambda: random.expovariate(THETA),
                lambda x, k: (x / math.factorial(k)) ** (1 / k))