import matplotlib.pyplot as plt
import numpy as np
import warnings
import yfinance as yf
from arch import arch_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

warnings.filterwarnings("ignore")

#====================TICKER LOAD====================

my_data = yf.download("BTC-USD", start="2020-01-01", end="2023-01-01", interval="1d")
my_data = my_data[["Close"]]
my_data = my_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_my_data = my_data.loc[:train_end_date]
test_my_data = my_data.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_my_data.index, train_my_data["Close"], label="Training Data", color="blue")
plt.plot(test_my_data.index, test_my_data["Close"], label="Testing Data", color="orange")
plt.title("BTC-USD Close Price (Training and Testing Data)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

#====================LSTM MODEL====================

scaler_my_model = MinMaxScaler(feature_range=(0, 1))
train_scaled_my_model = scaler_my_model.fit_transform(train_my_data)
test_scaled_my_model = scaler_my_model.transform(test_my_data)

def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length, 0])
        y.append(data[i + sequence_length, 0])
    return np.array(X), np.array(y)

sequence_length_my_model = 60
X_train_my_model, y_train_my_model = create_sequences(train_scaled_my_model, sequence_length_my_model)
X_test_my_model, y_test_my_model = create_sequences(test_scaled_my_model, sequence_length_my_model)

X_train_my_model = X_train_my_model.reshape((X_train_my_model.shape[0], X_train_my_model.shape[1], 1))
X_test_my_model = X_test_my_model.reshape((X_test_my_model.shape[0], X_test_my_model.shape[1], 1))

my_model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train_my_model.shape[1], 1)),
    Dropout(0.2),
    
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

my_model.compile(optimizer="adam", loss="mean_squared_error")
my_model.summary()

history = my_model.fit(X_train_my_model, y_train_my_model, batch_size=32, epochs=10, validation_data=(X_test_my_model, y_test_my_model))

train_predictions_my_model = my_model.predict(X_train_my_model)
test_predictions_my_model = my_model.predict(X_test_my_model)

train_predictions_my_model = scaler_my_model.inverse_transform(train_predictions_my_model)
y_train_my_model = scaler_my_model.inverse_transform(y_train_my_model.reshape(-1, 1))
test_predictions_my_model = scaler_my_model.inverse_transform(test_predictions_my_model)
y_test_my_model = scaler_my_model.inverse_transform(y_test_my_model.reshape(-1, 1))

my_model.save("my_lstm_model.h5")


plt.figure(figsize=(12, 6))
plt.plot(train_my_data.index[sequence_length_my_model:], y_train_my_model, label="Training True Values", color="blue")
plt.plot(train_my_data.index[sequence_length_my_model:], train_predictions_my_model, label="Training Predictions", color="cyan")
plt.plot(test_my_data.index[sequence_length_my_model:], y_test_my_model, label="Testing True Values", color="orange")
plt.plot(test_my_data.index[sequence_length_my_model:], test_predictions_my_model, label="Testing Predictions", color="red")
plt.title("Price Prediction with LSTM")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.savefig("my_lstm_chart.png")


plt.show()

#====================AR MODEL====================

my_ar_model = ARIMA(train_my_data, order=(5, 0, 0))
my_ar_model_fitted = my_ar_model.fit()

ar_predictions_my_ar_model = my_ar_model_fitted.predict(start=len(train_my_data), end=len(train_my_data) + len(test_my_data) - 1)

my_ar_model_rmse = np.sqrt(mean_squared_error(test_my_data, ar_predictions_my_ar_model))
print("RMSE for AR model:", my_ar_model_rmse)

print(my_ar_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), test_my_data, label="Actual", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), ar_predictions_my_ar_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'my_data' (using AR(5))")
plt.legend()
plt.grid(True)

plt.show()

#====================MA MODEL====================

my_ma_model = ARIMA(train_my_data, order=(0, 0, 2))
my_ma_model_fitted = my_ma_model.fit()

ma_predictions_my_ma_model = my_ma_model_fitted.predict(start=len(train_my_data), end=len(train_my_data) + len(test_my_data) - 1)

my_ma_model_rmse = np.sqrt(mean_squared_error(test_my_data, ma_predictions_my_ma_model))
print("RMSE for MA model:", my_ma_model_rmse)

print(my_ma_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), test_my_data, label="Actual", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), ma_predictions_my_ma_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'my_data' (using MA(2))")
plt.legend()
plt.grid(True)

plt.show()

#====================ARMA MODEL====================

my_arma_model = ARIMA(train_my_data, order=(5, 0, 2))
my_arma_model_fitted = my_arma_model.fit()

arma_predictions_my_arma_model = my_arma_model_fitted.predict(start=len(train_my_data), end=len(train_my_data) + len(test_my_data) - 1)

my_arma_model_rmse = np.sqrt(mean_squared_error(test_my_data, arma_predictions_my_arma_model))
print("RMSE for ARMA model:", my_arma_model_rmse)

print(my_arma_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), test_my_data, label="Actual", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), arma_predictions_my_arma_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'my_data' (using ARMA(5,2))")
plt.legend()
plt.grid(True)

plt.show()

#====================ARIMA MODEL====================

my_arima_model = ARIMA(train_my_data, order=(5, 1, 2))
my_arima_model_fitted = my_arima_model.fit()

arima_predictions_my_arima_model = my_arima_model_fitted.predict(start=len(train_my_data), end=len(train_my_data) + len(test_my_data) - 1)

my_arima_model_rmse = np.sqrt(mean_squared_error(test_my_data, arima_predictions_my_arima_model))
print("RMSE for ARIMA model:", my_arima_model_rmse)

print(my_arima_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), test_my_data, label="Actual", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), arima_predictions_my_arima_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'my_data' (using ARIMA(5,1,2))")
plt.legend()
plt.grid(True)

plt.show()

#====================SARIMA MODEL====================

my_sarima_model = SARIMAX(train_my_data, order=(5, 1, 2), seasonal_order=(1, 0, 2, 12))
my_sarima_model_fitted = my_sarima_model.fit()

sarima_predictions_my_sarima_model = my_sarima_model_fitted.predict(start=len(train_my_data), end=len(train_my_data) + len(test_my_data) - 1)

my_sarima_model_rmse = np.sqrt(mean_squared_error(test_my_data, sarima_predictions_my_sarima_model))
print("RMSE for SARIMA model:", my_sarima_model_rmse)

print(my_sarima_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), test_my_data, label="Actual", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), sarima_predictions_my_sarima_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'my_data' (using SARIMA(5,1,2)(1,0,2,12))")
plt.legend()
plt.grid(True)

plt.show()

#====================ARCH MODEL====================

train_my_arch_model_returns = 100 * train_my_data.pct_change().dropna()
test_my_arch_model_returns = 100 * test_my_data.pct_change().dropna()
my_arch_model = arch_model(train_my_arch_model_returns, mean='Zero', vol='ARCH', p=4)
my_arch_model_fitted = my_arch_model.fit()

my_arch_model_arch_forecast = my_arch_model_fitted.forecast(horizon=len(test_my_data))
arch_predictions_my_arch_model = np.sqrt(my_arch_model_arch_forecast.variance.values[-1, :])

#my_arch_model_rmse = np.sqrt(mean_squared_error(test_my_data, arch_predictions_my_arch_model))
#print("RMSE for ARCH model:", my_arch_model_rmse)

print(my_arch_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_arch_model_returns)), test_my_arch_model_returns, label="Actual Returns", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), arch_predictions_my_arch_model, label="Predicted Volatility", color="orange")
plt.xlabel("Time")
plt.title("Actual Returns vs Predicted Volatility of 'my_data' (using ARCH(4))")
plt.legend()
plt.grid(True)

plt.show()

#====================GARCH MODEL====================

train_my_garch_model_returns = 100 * train_my_data.pct_change().dropna()
test_my_garch_model_returns = 100 * test_my_data.pct_change().dropna()
my_garch_model = arch_model(train_my_garch_model_returns, mean='Zero', vol='GARCH', p=4, q=2)
my_garch_model_fitted = my_garch_model.fit()

my_garch_model_garch_forecast = my_garch_model_fitted.forecast(horizon=len(test_my_data))
garch_predictions_my_garch_model = np.sqrt(my_garch_model_garch_forecast.variance.values[-1, :])

#my_garch_model_rmse = np.sqrt(mean_squared_error(test_my_data, garch_predictions_my_garch_model))
#print("RMSE for GARCH model:", my_garch_model_rmse)

print(my_garch_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_garch_model_returns)), test_my_garch_model_returns, label="Actual Returns", color="blue")
plt.plot(range(len(train_my_data), len(train_my_data) + len(test_my_data)), garch_predictions_my_garch_model, label="Predicted Volatility", color="orange")
plt.xlabel("Time")
plt.title("Actual Returns vs Predicted Volatility of 'my_data' (using GARCH(4,2))")
plt.legend()
plt.grid(True)

plt.show()

