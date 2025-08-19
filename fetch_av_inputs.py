from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
from datetime import datetime

# --- CONFIG ---
symbol = 'AAPL'
api_key = "test_yf_fetch.py"
strike_price = 105.0
expiration_date = datetime(2024, 12, 20)
risk_free_rate = 0.052

# --- Fetch data ---
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta = ts.get_daily(symbol=symbol, outputsize='compact')  # last ~100 days

# --- Clean and process ---
data = data.sort_index()
close_prices = data["4. close"]
current_price = close_prices.iloc[-1]

# --- Compute time to maturity (T) ---
#today = datetime.now()
#T = max((expiration_date - today).days / 365.0, 0.0001)
T = 0.25
# --- Compute historical volatility (σ) ---
log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
sigma = np.std(log_returns) * np.sqrt(252)

# Bundle everything into a dictionary so it can be imported
option_inputs = {
    "S": round(current_price, 2),
    "K": strike_price,
    "T": round(T, 4),
    "r": round(risk_free_rate, 4),
    "sigma": round(sigma, 4)
}

# Optional printout for standalone run
if __name__ == "__main__":
    print("\n--- Option Pricing Inputs from Alpha Vantage ---")
    for key, value in option_inputs.items():
        print(f"{key:>10}: {value}")
