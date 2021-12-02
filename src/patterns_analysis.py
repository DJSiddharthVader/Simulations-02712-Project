import pandas as pd
from tqdm.notebook import tqdm
import matrix
import model
import analysis as an


"""
Code to examine how sparsity of the K_ac matrix affects model
dynamics and statistics. Will produce a dataframe of statistics
by running analyze() and create plots in the notebook.
"""


def analyze(size, num, lower, upper, patterns, end_time):
    dfs, inits = [], an.make_random_abundances(size, num, lower, upper)
    for pattern in tqdm(patterns, desc='pattern', leave=False):
        rows, K_ac = [], matrix.pattern_matrix(pattern, size)
        for p_i, init in enumerate(tqdm(inits, desc='init', leave=False)):
            # simulate
            t, N, S, E, P = model.simulate(K_ac, init, end_time)
            # calculate statistics
            row = an.compute_stats(N)
            row["init"] = p_i
            rows.append(row)
        # consolidate data for all inits all for K_ac
        df = pd.DataFrame(rows)
        df = an.append_static_col(df, pattern, "pattern")
        dfs += [df]
    return pd.concat(dfs)
