import numpy as np
from scipy.integrate import solve_ivp


# Model params specified in @eldar_2011
params = {
    "r": 0.5,
    "gamma_n": 0.01,
    "beta_S": 0.1,
    "beta_E": 0.2,
    "j_P_d": .20,
    "V_max": 20,
    "beta_P_D": 100,
    "m": 1,
    "K_RS": 0.025,
}


def make_init(N):
    """make_init.
    Make tthe initial condition vector given a
    vector of initial strain abundances

    :param N: vector of strain abundances
    """
    N = np.asarray(N)
    S = np.asarray([0] * len(N))
    return np.concatenate([N, S, [0], [0]])


def iterator(t, state, r, gamma_n, beta_S, beta_E, j_P_d,
             V_max, beta_P_D, m, K_RS, K_ac):
    """iterator.
    Computes the derivative of each strain, signal molecule,
    exo-enzyme and the public good for a single time step.
    This is passed to solve_ivp for simulating the model.

    :param t: time step (required by solve_ivp)
    :param state: current state (1 vector of all varialbes)
    :param r: growth cost of producing the public good
    :param gamma_n: spontaneous cell death rate
    :param beta_S: density dependant cell death rate
    :param beta_E: spontaneous enzyme degredation rate
    :param j_P_d: spontaneous usable nutrient production rate
    :param V_max: enzyme activity rate
    :param beta_P_D: usable nutrient consumption rate
    :param m: exponent in activation function f()
    :param K_RS: receptor-signal binding constant
    :param K_ac: receptor-signal activation matrix
    """
    # Set up state variables
    numStrains = int((len(state)-2)/2)  # number of strains being simulated
    n, S, = state[:numStrains], state[numStrains:numStrains * 2]
    n, S = n.reshape((n.shape[0],)), S.reshape((S.shape[0],))
    E, P = state[-2], state[-1]
    n_tot = sum(n)
    # Build active receptor-signal complex vector f(R_ac)
    numerator = np.matmul(S.T, K_ac)
    denominator = np.matmul(S.T, K_ac)  # + np.matmul(S.T, K_in)
    R_ac = numerator / (K_RS + denominator)
    f_R_ac = np.apply_along_axis(lambda x: x**m, 0, R_ac)
    # Calculating dn/dt
    dndt = (P / (P + 1)) * (1 - r * f_R_ac) - n_tot - gamma_n
    dndt = dndt * n  # element wise multiplication for each strain
    # Calculating dS/dt
    dSdt = beta_S * (n - S)
    # Calculating dE/dt
    dEdt = np.dot(f_R_ac, n) - beta_E * E
    dEdt = np.asarray([dEdt]).reshape((1,))
    # Calculating dP/dt
    dPdt = j_P_d + V_max * E - beta_P_D * (P / (P + 1)) * n_tot
    dPdt = np.asarray([dPdt]).reshape((1,))
    return np.concatenate([dndt, dSdt, dEdt, dPdt])


def simulate(K_ac, N, end, params=params):
    """simulate.
    Runs a simulation of the model with the given conditions

    :param N:      Initial bacterial abundance vector for
                   the simulation
    :param end:    Time to simulate until.
    :param params: Parameters for the model, dont really
                   need to be changed as we only ever use
                   the parameters from @eldar_2011
    """
    if len(N) != len(K_ac):
        raise ValueError('must have as many initial values as cols in matrix')
    init = make_init(N)
    params["K_ac"] = K_ac
    sim = solve_ivp(iterator,
                    t_span=(0, end),
                    y0=init,
                    args=params.values(),
                    vectorized=True)
    N = sim.y[:len(N)]  # matrix of strain abundance x timestep
    S = sim.y[len(N): len(N)*2]  # matrix of signal abundance x timestep
    E, P = sim.y[-2], sim.y[-1]
    return sim.t, N, S, E, P
