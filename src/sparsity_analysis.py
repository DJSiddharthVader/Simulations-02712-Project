import numpy as np
import pandas as pd
import matrix
import model
import analysis as an
from tqdm.notebook import tqdm


"""
Code to examine how sparsity of the K_ac matrix affects model
dynamics and statistics. Will produce a dataframe of statistics
by running analysis() and I will create plots with code in plot.py
"""


def analyze(sizes, n, lower, upper, get_sparsity, end_time):
    """analyze.
    Preform the sparsity analysis using different
    random initial populations for different
    population sizes. Takes a while to run due to
    how many combinations are tested.

    :param sizes: population sizes to simulate
    :param n: number of initial populations
    :param lower: minimum abundance
    :param upper: maximum abundance
    :param sparsity: fnc to calculate max sparsity
                     to test given n
    :param end_time: time steps to simulate
    """
    pop_dfs = []
    for size in tqdm(sizes, desc='size'):
        max_s = min(1, get_sparsity(size))
        dfs, K_acs = [], list(matrix.random_matrix_generator(size, max_s))
        for K_ac in tqdm(K_acs, desc='sparsity', leave=False):
            rows, inits = [], an.make_random_abundances(size, n, lower, upper)
            for p_i, init in enumerate(tqdm(inits, desc='init', leave=False)):
                # simulate
                t, N, S, E, P = model.simulate(K_ac, init, end_time)
                # calculate statistics
                row = an.compute_stats(N)
                row["init"] = p_i
                rows.append(row)
            # consolidate data for all inits all for K_ac
            df = pd.DataFrame(rows)
            sparsity = np.sum(K_ac)/(size*size)
            df = append_static_col(df, sparsity, "sparsity")
            dfs += [df]
        # consolidate data for all K_ac's for current size
        idf = pd.concat(dfs).reset_index(drop=True)
        idf = append_static_col(idf, size, 'Size')
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
