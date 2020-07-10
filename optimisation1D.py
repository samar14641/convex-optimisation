import numpy as np
import pandas as pd
from math import log10, sqrt
from pprint import pprint


phi = (1 + sqrt(5)) / 2  # golden ratio

def f(x):
    return x ** 2

def derivative(x):  # f(x) = x^2, hence f'(x) = 2x
    return 2 * x

def intervalBisection(tol, low, high):  # based on the interval bisection algorithm in the notes
    i = 0  # iterations
    a, b = low, high 
    deri = derivative(high)  # deri = f'(high)

    while (b - a) * deri > tol:
        if derivative((a + b) / 2) > 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
        
        i += 1

        if i == 1000:  # limit to 1000 iterations
            break

    return i

def goldenSectionSearch(tol, low, high):
    i = 0  # iterations
    x1, x4 = low, high
    x2 = x4 - ((x4 - x1) / phi)
    x3 = x1 + ((x4 - x1) / phi)

    while abs(x3 - x4) > tol:
        if f(x3) < f(x4):
            x4 = x3
        else:
            x1 = x2

        x2 = x4 - ((x4 - x1) / phi)
        x3 = x1 + ((x4 - x1) / phi)

        i += 1

        if i == 1000:  # limit to 1000 iterations
            break

    return i

def main():
    tolerance = np.linspace(1e-08, 1, num = 50, endpoint = True)  # get tolerance values for each run

    # get search range from a uniform distro
    low = np.random.uniform(-10, 0)  # low ~ U[-10, 0]
    high = np.random.uniform(0, 10)  # high ~ U[0, 10]

    results = []

    for tol in tolerance:  # this loop runs 50 times i.e. len of tolerance
        ibIter = intervalBisection(tol, low, high)
        gssIter = goldenSectionSearch(tol, low, high)

        results.append((tol, ibIter, gssIter))

    df = pd.DataFrame(results, columns = ['tol', 'ibIter', 'gssIter'])

    pprint(df)

main()