import numpy as np
import pandas as pd
import matrix
import model
import analysis as an
from tqdm import tqdm


"""
Code to examine how sparsity of the K_ac matrix affects model
dynamics and statistics. Will produce a dataframe of statistics
by running analysis() and I will create plots with code in plot.py
"""


def analyze(size, num, lower, upper, sparsity, end_time):
    """analyze.
    Preform the sparsity analysis using different
    random initial populations for different
    populatin sizes between 2 and size.

    :param size: size of each population
    :param num: number of initial populations
    :param lower: minimum abundance
    :param upper: maximum abundance
    :param sparsity: maximum sparsity value to try
    :param end_time: time steps to simulate
    """
    pop_dfs = []
    for pop_size in tqdm(range(2, size+1), desc='|N|'):
        inits = an.make_random_abundances(pop_size, num, lower, upper)
        idfs = []
        for p_i, init in tqdm(enumerate(inits), desc='initial', leave=True):
            dfs = [analyze_run(init, sparsity, end_time)
                   for init in inits]
            dfs = [append_static_col(df, p_i, 'Init') for df in dfs]
            idfs += [pd.concat(dfs).reset_index(drop=True)]
        idf = pd.concat(idfs).reset_index(drop=True)
        idf = append_static_col(idf, pop_size, 'Size')
        pop_dfs += [idf]
    return pd.concat(pop_dfs)


def append_static_col(df, value, name):
    """append_static_col.
    Append a column with all with the
    same value to a data frame

    :param df: dataframe
    :param value: column value
    :param name: column name
    """
    col = pd.DataFrame({name: [value]*df.shape[0]})
    return pd.concat([df, col], axis=1)


def analyze_run(init, sparsity, end_time):
    """analyze_run.
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
        row = an.compute_stats(N)
        row["sparsity"] = np.sum(K_ac)/(n*n)
        rows.append(row)
    return pd.DataFrame(rows)
