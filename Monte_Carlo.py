import numpy as np

def monte_carlo_call(S, K, T, r, sigma, num_simulations=100000, return_all=False):
    if T <= 0:
        payoff = max(S - K, 0)
        return (payoff, np.array([payoff]), np.array([S])) if return_all else payoff

    np.random.seed(42)
    Z = np.random.standard_normal(num_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(ST - K, 0)
    call_price = np.exp(-r * T) * np.mean(payoffs)

    return (call_price, payoffs, ST) if return_all else call_price
