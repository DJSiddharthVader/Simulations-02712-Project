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
import matplotlib.pyplot as plt
# import seaborn as sns


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
