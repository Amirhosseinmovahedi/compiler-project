import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from sklearn.metrics import mean_squared_error


my_data = yf.download("BTC-USD", start="2020-01-01", end="2023-01-01", interval="1d")
my_data = my_data[["Close"]]
my_data = my_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_my_data = my_data.loc[:train_end_date]
test_my_data = my_data.loc[train_end_date:test_end_date]

my_model = ARIMA(train_my_data, order=(10, 0, 0))
my_model_fitted = my_model.fit()

ar_predictions_my_model = my_model_fitted.predict(start=len(train_my_data), end=len(train_my_data) + len(test_my_data) - 1)

my_model_rmse = np.sqrt(mean_squared_error(test_my_data, ar_predictions_my_model))
print("RMSE for AR model:", my_model_rmse)

print(my_model_fitted.summary())

