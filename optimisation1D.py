import numpy as np
import pandas as pd
from pprint import pprint


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
    pass

def main():
    tolerance = np.linspace(1e-08, 1, num = 50, endpoint = True)  # get tolerance values for each run

    results = []

    for tol in tolerance:  # this loop runs 50 times i.e. len of tolerance
        # get search range from a uniform distro
        low = np.random.uniform(-10, 0)  # low ~ U[-10, 0]
        high = np.random.uniform(0, 10)  # high ~ U[0, 10]
        
        ibIter = intervalBisection(tol, low, high)
        # print(ibIter)
        # gssIter = goldenSectionSearch(tol, low, high)

        # results.append((tol, ibIter, gssIter))

    # df = pd.DataFrame(results, columns = ['tol', 'ibIter', 'gssIter'])

    # pprint(df)

main()