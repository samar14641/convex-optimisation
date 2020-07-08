import numpy as np
import pandas as pd


def intervalBisection(tol, low, high):
    continue

def goldenSectionSearch(tol, low, high):
    continue

def main():
    tolerance = np.linspace(1e-08, 1, num = 50, endpoint = True)  # get tolerance values for each run

    for tol in tolerance:  # this loop runs 50 times i.e. len of tolerance
        # get search range from a uniform distro
        low = np.random.uniform(-10, 0)  # low ~ U[-10, 0]
        high = np.random.uniform(0, 10)  # high ~ U[0, 10]
        
        ibIter = intervalBisection(tol, low, high)
        gssIter = goldenSectionSearch(tol, low, high)

        
