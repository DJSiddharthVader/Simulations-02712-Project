import numpy as np
import pandas as pd
from scipy.stats import skew


"""
Functions to analyze simulation results from the model,
generally comparing the initial state (abundance vector
of bacteria) to the final state after stability or
a given set of time steps.

Most functions accept a timesteps argument which is
the abundance vector at each time step of the model.

The diversity measures are taken from @calle_2019
"""


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


def normalize(abundance):
    """normalize.
    Normalize the abundance vector.

    :param abundance: unnormalized abundance
    """
    div = sum(abundance)
    return [x/div for x in abundance]


def make_random_abundances(size, num, lower, upper):
    """make_random_abundaces.
    Produce a random abundance vector with the
    specified properties, used as initial
    conditions.

    :param size: size of each vector
    :param num: number of vectors
    :param lower: lower bound on abundance
    :param upper: upper bound on abundance
    """
    return np.random.uniform(lower, upper, [num, size])


# Statistics computed from all time steps
def compute_stats(N):
    """compute_stats.
    Compute population stats for the results
    of a simulation of the ODE model.

    :param N: |strains| by |time points| matrix
    """
    stats = {}
    stats["total"] = total(N.T)
    stats["growth_rate"] = growth_rate(N.T)
    stats["has_grown"] = has_grown(N.T)
    # stats["skew"] = skewness(N.T)
    stats["euclidian"] = euclidian(N.T)
    # normalize for diversity metrics
    N = np.apply_along_axis(normalize, 1, N.T).T
    stats["shannon_index"] = shannon_index(N.T)
    stats["bray_curtis"] = bray_curtis(N.T)
    return stats


def total(timesteps):
    """total.
    Total population at the final time step

    :param timesteps: abundance vector at each time step
    """
    return sum(timesteps[-1])


def growth_rate(timesteps):
    """growth_rate.
    Growth rate of the total population size.
    Population size is not constant in the model
    so can be useful to examine how it grows.

    :param timesteps: abundance vector at each time step
    """
    p1, pn = sum(timesteps[0]), sum(timesteps[-1])
    return (pn-p1)/(p1*len(timesteps))


def has_grown(timesteps):
    """has_grown.
    Proportion of strains that have increased in
    abundance by the end of the simulation

    :param timesteps: abudance vector at each time step
    """
    t1s, tns = timesteps[0], timesteps[-1]
    return sum([1 for t1, tn in zip(t1s, tns) if tn > t1])/len(t1s)


def euclidian(timesteps):
    """euclidian.
    euclidian distance between 2 vectors

    :param timesteps: abudance vector at each time step
    """
    tn, t1 = timesteps[-1], timesteps[0]
    return euclidian_(tn, t1)


def skewness(timesteps):
    """skewness.
    Calculate Fisher-Pearson coefficient of
    skewness for the abundance i.e. how far
    from normal are the abundaces distributed.

    :param timesteps: abudance vector at each time step
    """
    tn, t1 = skewness_(timesteps[-1]), skewness_(timesteps[0])
    return tn - t1


def shannon_index(timesteps):
    """shannon_index.
    Calculate the shannon index of a population,
    this is a type of alpha diversity.

    :param timesteps: abudance vector at each time step
    """
    tn, t1 = shannon_index_(timesteps[-1]), shannon_index_(timesteps[0])
    return tn - t1


def bray_curtis(timesteps):
    """bray_curtis.
    Calculate the bray curtis distance between 2
    abundnace vectors. Assumes that both vectors
    contain the same OTU set in the same order
    (entries can be zero). This is a type of
    beta diversity.

    :param timesteps: abudance vector at each time step
    """
    tn, t1 = timesteps[-1], timesteps[0]
    return bray_curtis_(tn, t1)


# Statistics computed on a single abundance vector
def euclidian_(abundance1, abundance2):
    """euclidian.
    euclidian distance between 2 vectors

    :param abundance1: bacterial abundance vector
    :param abundance2: bacterial abundance vector
    """
    # return np.sqrt(np.sum(abundance1-abundance2)**2)
    return np.linalg.norm(abundance1 - abundance2)


def skewness_(abundance):
    """skewness_.
    Calculate Fisher-Pearson coefficient of
    skewness for the abundance i.e. how far
    from normal are the abundaces distributed.

    :param abundnace: bacterial abundace vector
    """
    return skew(abundance)


def shannon_index_(abundance):
    """shannon_index.
    Calculate the shannon index of a population,
    this is a type of alpha diversity.

    :param abundance: bacterial abundance vector
    """
    return -sum([p_i*np.log2(p_i) for p_i in abundance])


def bray_curtis_(abundance1, abundance2):
    """bray_curtis.
    Calculate the bray curtis distance between 2
    abundnace vectors. Assumes that both vectors
    contain the same OTU set in the same order
    (entries can be zero). This is a type of
    beta diversity.

    :param abundance1: bacterial abundance vector
    :param abundance2: bacterial abundance vector
    """
    c = [min(x, y) for x, y in zip(abundance1, abundance2)]
    return 1-2*sum(c)/(sum(abundance1)+sum(abundance2))
