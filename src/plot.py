import matrix
import model
import matplotlib.pyplot as plt

"""
Plotting utilities to generate figures

Plot idea:
 - plot gif of k_ac (decreasing sparsity) and model dynamics (1 k_ac per frame
 - left half is heatmap of K_ac matrix (0=white, 1=color)
 - right half is entire simulation of the model (all time steps for that K_ac)
 - x axis is time, y axis could be
   - model dynamics (just strain abundances as lines)
   - model properties (alpha/beta diversity, growth rate, etc.)
"""


def plot_model(results):
    t, N, S, E, P = results
    # Set up
    fig, ax = plt.subplots(2, 2, sharex=True)
    axN, axS, axE, axP = ax[0][0], ax[0][1], ax[1][0], ax[1][1]
    fig.suptitle("Model Simulation")
    # Plot Strains
    labels = ["N{}".format(i) for i in range(1, len(N)+1)]
    axN.plot(t, N.T, label=labels)
    axN.set_title("Strains")
    axN.legend()
    # Plot Signals
    labels = ["S{}".format(i) for i in range(1, len(S)+1)]
    axS.plot(t, S.T, label=labels)
    axS.set_title("Signals")
    axS.legend()
    # Plot Exo-Enzyme
    axE.plot(t, E)
    axE.set_title("Exo-Enzyme")
    # Plot Usable Nutrient
    axP.plot(t, P)
    axP.set_title("Usable Nutrient")
    # Formatting
    fig.tight_layout()
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', which='both',
                    top=False, bottom=False, left=False, right=False)
    plt.xlabel("Time")
    plt.show()


def run_model(K_ac, initial_N, time_steps,
              params=model.params, show=True):
    """run_model.
    Wrapper for running the model and plotting results

    :param K_ac: QS matrix
    :param initial_N: initial bacterial abundances
    :param time_steps: time steps to run the model
    """
    print('QS interaction matrix')
    if type(K_ac) == str:
        K_ac = matrix.pattern_K_acrix(K_ac, len(initial_N))
    print(K_ac.shape)
    print(K_ac)
    print('simulating...')
    results = model.simulate(K_ac,
                             initial_N,
                             time_steps,
                             params)
    print('finished simulating!')
    if show:
        print('plotting...')
        plot_model(results)
    else:
        return results


def matrix_comparisons(matrices, initial_N, time_steps, params=model.params):
    # Get results for each matrix
    mat_results = []
    for mat in matrices:
        if type(mat) == str:
            K_ac = matrix.pattern_matrix(mat, len(initial_N))
        results = model.simulate(K_ac, initial_N,
                                 time_steps, params=params)
        mat_results.append((results[0], results[1]))
    # plot all together
    plt.rcParams["figure.figsize"] = 16, 9
    fig, axs = plt.subplots(2, int(len(matrices)/2),
                            sharex=True,
                            sharey='row')
    labels = ["N{}".format(i) for i in range(1, len(initial_N)+1)]
    for i, ax in enumerate(axs.reshape(-1)):
        t, N = mat_results[i]
        ax.plot(t, N.T, label=labels)
        ax.set_title(matrices[i])
    # Formatting
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='right')
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', which='both',
                    top=False, bottom=False, left=False, right=False)
    plt.xlabel("Time")
    fig.tight_layout()
    # fig.suptitle("Comparison of Different K_ac Matrices")
    fig.suptitle('Initial: ({})'.format(', '.join(str(x) for x in initial_N)))
    plt.subplots_adjust(top=0.90, right=0.94, wspace=0)
    plt.savefig('../Documents/figures/k_ac_comparisons.png')
    plt.show()
