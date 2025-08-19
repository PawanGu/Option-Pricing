# 📈 Option Pricing Models in Python

This project implements and compares **Black-Scholes** and **Monte Carlo** methods for European call options. It fetches live or historical data using APIs like **Alpha Vantage**, estimates volatility, and visualizes results.

## Features

- ✅ Black-Scholes pricing
- ✅ Monte Carlo simulation
- ✅ Estimation of variable (K, T, σ, r) from historical data
- ✅ Plot payoff distributions & price vs variable (K, T, σ, r)
- ✅ comparing Black-Scholes and Monte Carlo methods
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
python price_option.py

# Vary strike price (K)
python bs_vs_mc_plot_variable.py --var K

# Vary maturity (T)
python bs_vs_mc_plot_variable.py --var T

# Vary Volatility (K)
python bs_vs_mc_plot_variable.py --var σ

# Vary interest rate (r)
python bs_vs_mc_plot_variable.py --var r
