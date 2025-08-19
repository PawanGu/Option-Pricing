# 📈 Option Pricing Models in Python

This project implements and compares **Black-Scholes** and **Monte Carlo** methods for European call options. It fetches live or historical data using APIs like **Alpha Vantage**, estimates volatility, and visualizes results.

## Features

- ✅ Black-Scholes pricing
- ✅ Monte Carlo simulation
- ✅ Volatility estimation from historical data
- ✅ Plot payoff distributions & price vs variable (K, T, σ, r)
- ✅ Fetch data via Alpha Vantage

## Setup

```bash
git clone https://github.com/PawanGu/option-pricing.git
cd option-pricing
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt

## Run Examples
# Price using BS and MC
python scripts/price_option.py

# Visualize payoff histogram
python scripts/plot_payoff_hist.py

# Vary strike price (K)
python scripts/plot_vs_variable.py --var K

# Vary maturity (T)
python scripts/plot_vs_variable.py --var T
