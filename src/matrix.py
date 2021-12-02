import numpy as np
from itertools import product
import networkx as nx
from networkx import generators as gen

"""
Code to generate matrices for input to the QS model,
ultimately to see how different matrices affect model dynamics.

Specifically the matrix K_ac is defined @eldar_2011, but it
represents compatible signal molecule-receptor pairs that
are present in a given OTU in the population

All matrices are binary (either the receptor-signal pair is present
or not), so one can define the set of signals and receptors in each strain
to make this matrix.
If there are
Lets say strain 1 is R1S1 and strain 2 R2S2, this corresponds
If strain 1 is R1S1 and strain 2 R0S0 (no receptors or signals),
this corresponds the following matrix.

         1 0
         0 0

If strain 1 is R1S1S2 and strain 2 R2S2, these strains correspond
to the following matrix

         1 0
         1 1

In this code we only generate matrices but we could generate random
combinations of receptor and singals and use these to build the matrix.
For the empirically derived matrix from [@citation_needed] this is how
we build K_ac, looking at the signal-receptor sets for each strain.

Note that a given matrix can result from different R-S combinnation
among the strains.
Also @eldar_2011 also defines an inhibhitory matrix K_in but we ignore
that matrix, which is equiivalent as having it be all zeros (i.e.
no inhibhitory QS interactions).
"""


def random_matrix_generator(n, s, m=-1):
    """random_matrix_generator.
    Generator that returns a binary matrix
    with one more random entry set to 1
    after each iteration.

    :param n: numer of rows
    :param s: sparsity param (in [0,1])
    :param m: number of cols, if not specified matrix is square
    """
    if m == -1:
        m = n
    matrix = np.zeros((n, m))
    # randomoly sample matrix cells w/o replacement
    indices = list(product(range(m), range(n)))
    non_zero_entries = np.random.choice(m*n, int(m*n*s), replace=False)
    non_zero_entries = [indices[x] for x in non_zero_entries]
    # make the random cells 1
    for i, j in non_zero_entries:
        matrix[i][j] = 1
        yield matrix


def random_matrix(n, s, m=-1):
    """random_matrix.
    Return a random matrix with the specific
    level of sparsity s. Wrapper generator

    :param n: numer of rows
    :param s: sparsity param (in [0,1])
    :param m: number of cols, if not specified matrix is square
    """
    *_, final = iter(random_matrix_generator(n, s, m=m))
    return final


def pattern_matrix(pattern, n):
    """patterned_matrix.
    Return a matrix that is an adjacency matrix
    of a specific graph, generally taken from
    builtin graphs in the networkx package.

    :param pattern: string specifing which matrix
    :param n: size of the matrix (always square)
    """
    if pattern == 'null':
        # no QS interactions
        return np.zeros((n, n))
    elif pattern == 'ident':
        # Each OTU can only interact with its
        # own QS system (diagonal matrix)
        return np.diag([1]*n)
    elif pattern == 'naive':
        # naive coopertor from @eldar_2011
        # make one row all 1s (all strains
        # have that receptor)
        base = np.zeros((n, n))
        base[np.random.randint(0, n)] = np.ones(n)
        return base
    elif pattern == 'immune':
        # immune coopertor from @eldar_2011
        # make one col all 1s (all strains
        # produce that signal)
        base = np.zeros((n, n))
        base[np.random.randint(0, n)] = np.ones(n)
        return base.T
    elif pattern == 'barbell':
        # 2 complete subgraphs of size n/2 connected
        # by a single edge
        if n % 2 != 0:
            raise ValueError('barbell graph must take in an even n value > 2')
        graph = gen.classic.barbell_graph(int(n/2), 0)
    elif pattern == 'cycle':
        # simple cycle graph on all nodes
        graph = gen.classic.cycle_graph(n)
    elif pattern == 'complete':
        # every receptor binds every singal
        graph = gen.complete_graph(n)
    elif pattern == 'star':
        # central node connected to all others
        graph = gen.classic.star_graph(n-1)
    elif pattern == 'empirical':
        # graph that resembles a system of
        # QS interactions observed experimentally,
        # specifically from @[citation_needed]
        graph = None
    else:
        raise ValueError('Invalid matrix pattern')
    return nx.adjacency_matrix(graph).toarray().reshape((n, n))
