import matplotlib.pyplot as plt
from Monte_Carlo import monte_carlo_call
from Black_Scholes import black_scholes_call
from fetch_av_inputs import option_inputs

S = option_inputs["S"]
K = option_inputs["K"]
T = option_inputs["T"]
r = option_inputs["r"]
sigma = option_inputs["sigma"]

# Get Monte Carlo results
mc_price, payoffs, ST = monte_carlo_call(S, K, T, r, sigma, return_all=True)
bs_price = black_scholes_call(S, K, T, r, sigma)

# Display prices
print("\n--- European Call Option Pricing ---")
print(f"Black-Scholes Price : {bs_price:.2f}")
print(f"Monte Carlo Price   : {mc_price:.2f}")

# Plot histogram of payoffs
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(payoffs, bins=100, color="skyblue", edgecolor="black", alpha=0.8)
plt.axvline(mc_price, color='red', linestyle='--', label=f'MC Price = {mc_price:.2f}')
plt.title("Payoff Distribution")
plt.xlabel("Payoff")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

# Plot histogram of simulated final prices ST
plt.subplot(1, 2, 2)
plt.hist(ST, bins=100, color="lightgreen", edgecolor="black", alpha=0.8)
plt.axvline(K, color='purple', linestyle='--', label=f'Strike Price = {K}')
plt.title("Simulated Final Prices (S_T)")
plt.xlabel("S_T (Final Price)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("option_pricing_distributions.png", dpi=300)
plt.show()
