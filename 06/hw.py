import math
import random

import matplotlib.pyplot as plot
from scipy.stats import chi2, norm

N_FROM = 5
N_TO = 1000
GAMMA = 0.5
K = 10

def compute_plot(foo):
    ns = [x for x in range(N_FROM, N_TO)]
    ys = [sum([foo(n) / K for _ in range(K)]) for n in ns]
    return (ns, ys)

def save_plot(name, xs, ys):
    plot.clf()
    plot.plot(xs, ys)
    plot.savefig(name)

def build_plot(name, foo):
    xs, ys = compute_plot(foo)
    save_plot(name, xs, ys)

if __name__ == '__main__':
    build_plot("1",
               lambda n: sum([random.normalvariate(0, 1) ** 2 for _ in range(1, n)])
                         * (1 / chi2.ppf((1 - GAMMA) / 2, n) - 1 / chi2.ppf((1 + GAMMA) / 2, n)))

    build_plot("2",
               lambda n: sum([random.normalvariate(0, 1) for _ in range(1, n)]) ** 2
                         * (1 / (norm.ppf((3 - GAMMA) / 4) ** 2) - (1 / norm.ppf((3 + GAMMA) / 4) ** 2))
                         / n)
