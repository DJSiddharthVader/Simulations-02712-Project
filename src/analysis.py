import numpy as np
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


def compute_stats(N):
    """compute_stats.

    :param N:
    """
    stats = {}
    stats["growth_rate"] = growth_rate(N.T)
    N = np.apply_along_axis(normalize, 1, N.T).T
    return stats


def normalize(abundance):
    """normalize.
    Normalize the abundance vector.

    :param abundance: unnormalized abundance
    """
    div = sum(abundance)
    return [x/div for x in abundance]


# Statistics computed from all time steps
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


def skewness(timesteps):
    """skewness.
    Calculate Fisher-Pearson coefficient of
    skewness for the abundance i.e. how far
    from normal are the abundaces distributed.

    :param timesteps: abudance vector at each time step
    """
    t1, tn = skewness_(timesteps[0]), skewness_(timesteps[-1])
    return tn - t1


def shannon_index(timesteps):
    """shannon_index.
    Calculate the shannon index of a population,
    this is a type of alpha diversity.

    :param timesteps: abudance vector at each time step
    """
    t1, tn = shannon_index_(timesteps[0]), shannon_index_(timesteps[-1])
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
    t1, tn = timesteps[0], timesteps[-1]
    return bray_curtis_(tn, t1)


# Statistics computed on a single abundance vector
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
    return -sum([p_i*np.log(p_i) for p_i in abundance])


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
