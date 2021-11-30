import numpy as np
import pandas as pd
import matrix
import model
import analysis as an


"""
Code to examine how sparsity of the K_ac matrix affects model
dynamics and statistics. Will produce a dataframe of statistics
by running analysis() and I will create plots with code in plot.py
"""


def analysis(init, sparsity, end_time):
    """sparsity_analysis.
    Generate simulation data to analyze how K_ac
    sparsity affects model dynamics.

    :param init:  inital abudance vector
    :param sparsity: maximum sparsity to test
    :param end_time: time steps to simulate
    """
    rows, n = [], len(init)
    for K_ac in matrix.random_matrix_generator(n, sparsity):
        # simulate model with given params
        t, N, S, E, P = model.simulate(K_ac, init, end_time)
        # Calculate statistics
        row = {"sparsity": np.sum(K_ac)/(n*n)}
        # N, S are variables by time points matrices
        row["growth_rate"] = an.growth_rate(N.T)
        N = np.apply_along_axis(an.normalize, 1, N.T).T
        # store for easy conversion to a dataframe
        rows.append(row)
    return pd.DataFrame(rows)


def skewness(timesteps):
    return None


def richness(timesteps):
    return None


def shannon_index(timesteps):
    return None


def bray_curtis(timesteps):
    return None
