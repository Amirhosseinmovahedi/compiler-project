import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA


#====================TICKER LOAD====================

eth_data = yf.download("ETH-USD", start="2021-01-01", end="2023-12-31", interval="1d")
eth_data = eth_data[["Close"]]
eth_data = eth_data.dropna()

train_end_date = "2023-06-30"
test_end_date = "2023-12-31"

train_eth_data = eth_data.loc[:train_end_date]
test_eth_data = eth_data.loc[train_end_date:test_end_date]

#====================MA MODEL====================

my_model = ARIMA(train_eth_data, order=(0, 0, 3))
my_model_fitted = my_model.fit()

ma_predictions_my_model = my_model_fitted.predict(start=len(train_eth_data), end=len(train_eth_data) + len(test_eth_data) - 1)

my_model_rmse = np.sqrt(mean_squared_error(test_eth_data, ma_predictions_my_model))
print("RMSE for MA model:", my_model_rmse)

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_eth_data), len(train_eth_data) + len(test_eth_data)), test_eth_data, label="Actual", color="blue")
plt.plot(range(len(train_eth_data), len(train_eth_data) + len(test_eth_data)), ma_predictions_my_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.grid(True)
plt.savefig("ma_eth_chart.png")


plt.show()

