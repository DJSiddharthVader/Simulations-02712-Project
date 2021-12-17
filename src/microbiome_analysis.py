import utils
import patterns_analysis as pa
import pandas as pd
import seaborn as sns
from tqdm.notebook import tqdm


METADATA_FILE = "../Data/filtered_hmp2_metadata.tsv"
ABUNDANCE_FILE = "../Data/filtered_taxonomic_profiles.tsv"


def load_data():
    """load_data.
    load metadata and abundances into pandas
    filtering out strains with sparse abundaces

    :param thresh: threshold at which to filter out
                   strains if the are too sparse
    """
    metadata = pd.read_csv(METADATA_FILE, sep='\t', header=0)
    abundances = pd.read_csv(ABUNDANCE_FILE, sep='\t', header=0)
    return metadata, abundances


def make_initial_conditions(abundances, metadata):
    """make_initial_conditions.
    Get abundance vetors grouped by which condition
    the paitent has (UC, CD, nonIBD)

    :param metadata: patient metadata
    :param abundances: microbial abundances
    """
    initials = {}
    for condition, indices in metadata.groupby('diagnosis').groups.items():
        patients = metadata.iloc[indices]['External ID'].values.astype(str)
        initials[condition] = abundances[patients].to_numpy().T
    return initials


def analyze(abundances, metadata, patterns, end_time, params=None):
    """analyze.
    Use each patient as a set of initial conditions and
    run simulations with different matrices. Compute
    statistics for each simulation.

    :param abundances: abundance matrix
    :param metadata: patient metadata
    :param patterns: matrix patterns to test
    :param end_time: time to run the simulation
    :param params: simulation parameters
    """
    dfs, conditinal_inits = [], make_initial_conditions(abundances, metadata)
    for condition, inits in tqdm(conditinal_inits.items(), desc='conditions'):
        results = pa.analyze(inits, patterns, end_time, params)
        results = utils.append_static_col(results, condition, "condition")
        dfs.append(results)
    return pd.concat(dfs)


def plot_ecdf(df, outpath=None):
    """plot_ecdf.
    plot the ECDF of each statistic computed in the
    dataframe for each condition

    :param df: datframe of stats to plot (produced by analyze())
    :param outpath: path to image file to save plot to
    """
    df['shannon_index'] = abs(df['shannon_index'])
    df = pd.melt(df,
                 id_vars=['init', 'pattern', 'condition'],
                 var_name='statistic',
                 value_name='value')
    plot = sns.FacetGrid(df, col='condition', row='statistic', hue='pattern',
                         aspect=16/9, sharex=False, sharey=True)
    plot.map_dataframe(sns.ecdfplot, x='value')
    plot.add_legend()
    plot.tight_layout()
    if outpath is None:
        plot.fig.show()
    else:
        plot.fig.savefig(outpath)
