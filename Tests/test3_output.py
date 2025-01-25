import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA


#====================TICKER LOAD====================

my_df = yf.download("DOGE-USD", start="2020-01-01", end="2023-01-01", interval="1d")
my_df = my_df[["Close"]]
my_df = my_df.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_my_df = my_df.loc[:train_end_date]
test_my_df = my_df.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_my_df.index, train_my_df["Close"], label="Training Data", color="blue")
plt.plot(test_my_df.index, test_my_df["Close"], label="Testing Data", color="orange")
plt.title("DOGE-USD Close Price (Training and Testing Data)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

#====================AR MODEL====================

my_model = ARIMA(train_my_df, order=(5, 0, 0))
my_model_fitted = my_model.fit()

ar_predictions_my_model = my_model_fitted.predict(start=len(train_my_df), end=len(train_my_df) + len(test_my_df) - 1)

my_model_rmse = np.sqrt(mean_squared_error(test_my_df, ar_predictions_my_model))
print("RMSE for AR model:", my_model_rmse)

print(my_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_df), len(train_my_df) + len(test_my_df)), test_my_df, label="Actual", color="blue")
plt.plot(range(len(train_my_df), len(train_my_df) + len(test_my_df)), ar_predictions_my_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.grid(True)

plt.show()

my_model_fitted.save("ar_sales_model.pkl")

