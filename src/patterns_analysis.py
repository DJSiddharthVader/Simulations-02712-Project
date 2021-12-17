import pandas as pd
import seaborn as sns
from tqdm.notebook import tqdm
import matrix
import model
import utils


"""
Code to examine how sparsity of the K_ac matrix affects model
dynamics and statistics. Will produce a dataframe of statistics
by running analyze() and create plots in the notebook.
"""


def plot_ecdf(df, outpath=None):
    """plot_ecdf.
    plot the ECDF of each statistic computed in the
    dataframe and plot, save to outpath

    :param df: datframe of stats to plot (produced by analyze())
    :param outpath: path to image file to save plot to
    """
    df['shannon_index'] = abs(df['shannon_index'])
    df = pd.melt(df,
                 id_vars=['init', 'pattern'],
                 var_name='statistic',
                 value_name='value')
    plot = sns.FacetGrid(df, col='statistic', hue='pattern',
                         col_wrap=3, aspect=16/9,
                         sharex=False, sharey=True)
    plot.map_dataframe(sns.ecdfplot, x='value')
    plot.add_legend()
    plot.tight_layout()
    if outpath is None:
        plot.fig.show()
    else:
        plot.fig.savefig(outpath)


def analyze(inits, patterns, end_time, params=None):
    """analyze.
    For each set of initial conditions and patterns
    run a simulation, compute some statistics and
    return on organized dataframe of the results

    :param inits: sets of initial conditions for each simulation
    :param patterns: each matrix pattern to try
    :param end_time: simulation end_time
    :param params: simulation parameters, use defualt if not specified
    """
    dfs = []
    for pattern in tqdm(patterns, desc='pattern', leave=False):
        rows, K_ac = [], matrix.pattern_matrix(pattern, len(inits[0]))
        for p_i, init in enumerate(tqdm(inits, desc='init', leave=False)):
            # simulate
            t, N, S, E, P = model.simulate(K_ac, init, end_time, params=params)
            # calculate statistics
            row = utils.compute_stats(N)
            row["init"] = p_i
            rows.append(row)
        # consolidate data for all inits all for K_ac
        df = pd.DataFrame(rows)
        df = utils.append_static_col(df, pattern, "pattern")
        dfs += [df]
    return pd.concat(dfs)
