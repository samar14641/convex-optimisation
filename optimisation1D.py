import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from math import sqrt
from pprint import pprint


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

def goldenSectionSearch(tol, low, high, phi):
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

    phi = (1 + sqrt(5)) / 2  # golden ratio

    results = []

    for tol in tolerance:  # this loop runs 50 times i.e. len of tolerance
        ibIter = intervalBisection(tol, low, high)
        gssIter = goldenSectionSearch(tol, low, high, phi)  # standard GSS
        gssIterPlus = goldenSectionSearch(tol, low, high, phi + 0.1 * phi)  # increasing phi by 10%
        gssIterMinus = goldenSectionSearch(tol, low, high, phi * 0.9)  # decreasing phi by 10%

        results.append((tol, ibIter, gssIter, gssIterPlus, gssIterMinus))

    df = pd.DataFrame(results, columns = ['tol', 'ibIter', 'gssIter', 'gssIterPlus', 'gssIterMinus'])
    # log10 transformations
    df['tol_log'] = np.log10(df['tol'])
    df['ibIter_log'] = np.log10(df['ibIter'])
    df['gssIter_log'] = np.log10(df['gssIter'])
    df['gssIterPlus_log'] = np.log10(df['gssIterPlus'])
    df['gssIterMinus_log'] = np.log10(df['gssIterMinus'])

    # plot
    plt.plot('tol_log', 'ibIter_log', data = df, marker = 'o', markersize = 1, color = '#0000ff', label = 'Interval bisection')
    plt.plot('tol_log', 'gssIter_log', data = df, marker = 'o', markersize = 1, color = '#ff0000', label = 'GSS')
    plt.plot('tol_log', 'gssIterPlus_log', data = df, marker = 'o', markersize = 1, color = '#00e2ff', label = 'GSS 110% phi')
    plt.plot('tol_log', 'gssIterMinus_log', data = df, marker = 'o', markersize = 1, color = '#ff00ff', label = 'GSS 90% phi')
    plt.title('log10 iterations vs log10 tolerance in the range [' + str(np.round(low, 3)) + ', ' + str(np.round(high, 3)) + ']')
    plt.xlabel('log10 tolerance')
    plt.ylabel('log10 iterations')
    plt.legend()
    plt.savefig(os.getcwd() + '\\Graphs\\optimisation1DAddn')  # save in 'Graphs' dir
    plt.close()

    pprint(df)

main()