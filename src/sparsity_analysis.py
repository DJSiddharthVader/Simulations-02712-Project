import matrix
import model
import utils
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm.notebook import tqdm


"""
Code to examine how sparsity of the K_ac matrix affects model
dynamics and statistics. Will produce a dataframe of statistics
by running analyze() and create plots in the notebook.
"""


def plot_sparsity(df, outpath=None):
    """plot_sparsity.
    Plot the relation ship between the sparsity
    of K_ac and various population statistics
    for different population sizes.

    :param df: dataframe produced by analyze()
    :param outpath: path to save plot to
    """
    df['shannon_index'] = abs(df['shannon_index'])
    df = pd.melt(df,
                 id_vars=['init', 'density', 'size'],
                 var_name='statistic',
                 value_name='value')
    plot = sns.FacetGrid(df, col='statistic', row='size',
                         aspect=16/9, sharex=True, sharey=False)
    plot.map_dataframe(sns.lineplot, x='density', y='value', ci="sd")
    plot.add_legend()
    plot.tight_layout()
    if outpath is None:
        plot.fig.show()
    else:
        plot.fig.savefig(outpath)


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
    :param get_sparsity: fnc to calculate max sparsity
                         to test given n
    :param end_time: time steps to simulate
    """
    rows = []
    for size in tqdm(sizes, desc='size'):
        max_s = min(1, get_sparsity(size))
        K_acs = list(matrix.random_matrix_generator(size, max_s))
        for K_ac in tqdm(K_acs, desc='density', leave=False):
            density = np.sum(K_ac)/(size*size)
            inits = utils.make_random_abundances(size, n, lower, upper)
            for p_i, init in enumerate(tqdm(inits, desc='init', leave=False)):
                # simulate
                t, N, S, E, P = model.simulate(K_ac, init, end_time)
                # calculate statistics
                row = utils.compute_stats(N)
                row["init"] = p_i
                row['density'] = density
                row['size'] = size
                rows.append(row)
    return pd.DataFrame(rows)
