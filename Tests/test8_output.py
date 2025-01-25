import matplotlib.pyplot as plt
import numpy as np
import pickle
import warnings
import yfinance as yf
from arch import arch_model
from sklearn.metrics import mean_squared_error

warnings.filterwarnings("ignore")

#====================TICKER LOAD====================

spy_data = yf.download("SPY", start="2015-01-01", end="2023-01-01", interval="1d")
spy_data = spy_data[["Close"]]
spy_data = spy_data.dropna()

train_end_date = "2022-01-01"
test_end_date = "2023-01-01"

train_spy_data = spy_data.loc[:train_end_date]
test_spy_data = spy_data.loc[train_end_date:test_end_date]

#====================ARCH MODEL====================

train_arch_returns = 100 * train_spy_data.pct_change().dropna()
test_arch_returns = 100 * test_spy_data.pct_change().dropna()
arch = arch_model(train_arch_returns, mean='Zero', vol='ARCH', p=2)
arch_fitted = arch.fit()

arch_arch_forecast = arch_fitted.forecast(horizon=len(test_spy_data))
arch_predictions_arch = np.sqrt(arch_arch_forecast.variance.values[-1, :])

#arch_rmse = np.sqrt(mean_squared_error(test_spy_data, arch_predictions_arch))
#print("RMSE for ARCH model:", arch_rmse)

print(arch_fitted.summary())

with open("test.pkl", 'wb') as file:
    pickle.dump(arch_fitted, file)

#====================GARCH MODEL====================

train_garch_returns = 100 * train_spy_data.pct_change().dropna()
test_garch_returns = 100 * test_spy_data.pct_change().dropna()
garch = arch_model(train_garch_returns, mean='Zero', vol='GARCH', p=1, q=1)
garch_fitted = garch.fit()

garch_garch_forecast = garch_fitted.forecast(horizon=len(test_spy_data))
garch_predictions_garch = np.sqrt(garch_garch_forecast.variance.values[-1, :])

#garch_rmse = np.sqrt(mean_squared_error(test_spy_data, garch_predictions_garch))
#print("RMSE for GARCH model:", garch_rmse)

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_spy_data), len(train_spy_data) + len(test_garch_returns)), test_garch_returns, label="Actual Returns", color="blue")
plt.plot(range(len(train_spy_data), len(train_spy_data) + len(test_spy_data)), garch_predictions_garch, label="Predicted Volatility", color="orange")
plt.xlabel("Time")
plt.title("Actual Returns vs Predicted Volatility of 'spy_data' (using GARCH(1,1))")
plt.legend()
plt.grid(True)
plt.savefig("garch_spy.png")

plt.show()

