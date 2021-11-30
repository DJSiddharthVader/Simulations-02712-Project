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


def normalize(abundance):
    """normalize.
    Normalize the abundance vector.

    :param abundance: unnormalized abundance
    """
    div = sum(abundance)
    return [x/div for x in abundance]


def growth_rate(timesteps):
    """growth_rate.
    Growth rate of the total population size.
    Population size is not constant in the model
    so can be useful to examine how it grows.

    :param timesteps: abundance vector at each time point
    """
    p1, pn = sum(timesteps[0]), sum(timesteps[-1])
    return (pn-p1)/(p1*len(timesteps))


def skewness(abundance):
    """skewness_.
    Calculate Fisher-Pearson coefficient of
    skewness for the abundance i.e. how far
    from normal are the abundaces distributed.

    :param abundnace: bacterial abundace vector
    """
    return skew(abundance)


def richness(abundance):
    """richness.
    Calculate species richness of a sample,
    this is a type of alpha diversity.

    :param abundance: bacterial abundance vector
    """
    return sum([1 for x in abundance if x > 0])/len(abundance)


def shannon_index(abundance):
    """shannon_index.
    Calculate the shannon index of a population,
    this is a type of alpha diversity.

    :param abundance: bacterial abundance vector
    """
    return -sum([p_i*np.log(p_i) for p_i in abundance])


def bray_curtis(abundance1, abundance2):
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
