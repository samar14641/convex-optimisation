import matplotlib.pyplot as plt
import numpy as np
import os
from pprint import pprint
from scipy.optimize import minimize


def p(v):
    return ((1 - v[0]) ** 2) + 100 * ((v[1] - v[0] ** 2) ** 2)

def main():
    v1 = np.arange(-3, 12.1, step = 0.1)  # v1 in [-3, 12] in steps of 0.1
    v2 = np.arange(-6, 61)  # v2 in [-6, 60] in steps of 1.0
    vMin = np.array([1, 1])  # the global minima of p(v)
    
    X, Y = np.meshgrid(v1, v2)  # create the contour grid
    nmZ, cgZ = [], []

    for x in v1:
        nm_z, cg_z = [], []

        for y in v2:
            v = np.array([x, y])

            res = minimize(p, v, method = 'nelder-mead', options = {'maxiter': 5})
            nm_z.append(np.linalg.norm(res.x - vMin))  # calculate Euclidean dist from [1, 1]

            res = minimize(p, v, method = 'CG', options = {'maxiter': 5})
            cg_z.append(np.linalg.norm(res.x - vMin))  # calculate Euclidean dist from [1, 1]

        nmZ.append(nm_z)
        cgZ.append(cg_z)

    # plot nelder-mead contours
    nmZ = np.transpose(np.log10(np.array(nmZ)))

    nmPlt = plt.contourf(X, Y, nmZ, 4)
    cbar = plt.colorbar(nmPlt)
    cbar.set_label('log10 of Euclidean dist from [1, 1]')
    plt.title('Nelder-Mead Contour Plot zoomed in')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig(os.getcwd() + '\\Graphs\\nelderMeadContour')  # save in 'Graphs' dir
    plt.close()

    # plot CG contours
    cgZ = np.transpose(np.log10(np.array(cgZ)))

    cgPlt = plt.contourf(X, Y, cgZ, 4)
    cbar = plt.colorbar(cgPlt)
    cbar.set_label('log10 of Euclidean dist from [1, 1]')
    plt.title('Conjugate Gradient Descent Contour Plot zoomed in')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig(os.getcwd() + '\\Graphs\\conjGradContour')  # save in 'Graphs' dir
    plt.close()

main()