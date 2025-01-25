import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import yfinance as yf
from arch import arch_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.stattools import adfuller
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

warnings.filterwarnings("ignore")

#====================DATAFRAME LOAD====================

traffic = pd.read_csv('my_data.csv')
traffic['Date'] = pd.to_datetime(traffic['Date'])
traffic = traffic.set_index('Date')

traffic = traffic[["Close"]]
traffic = traffic.dropna()

train_end_date = "2021-09-01"
test_end_date = "2021-12-01"

train_traffic = traffic.loc[:train_end_date]
test_traffic = traffic.loc[train_end_date:test_end_date]

#====================TICKER LOAD====================

amazon = yf.download("AMZN", start="2020-01-01", end="2023-01-01", interval="1d")
amazon = amazon[["High"]]
amazon = amazon.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_amazon = amazon.loc[:train_end_date]
test_amazon = amazon.loc[train_end_date:test_end_date]

#====================ADF TEST====================

adf_result = adfuller(traffic)
print('Dataframe:', 'traffic')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\t{key}: {value}')
print('\n')

#====================ADF TEST====================

adf_result = adfuller(amazon)
print('Dataframe:', 'amazon')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\t{key}: {value}')
print('\n')

#====================ACF PLOT====================

plot_acf(traffic, lags=50, title='ACF of traffic')
plt.show()

#====================PACF PLOT====================

pacf_vals = pacf(amazon)
num_lags = 20
plt.bar(range(num_lags), pacf_vals[:num_lags])
plt.title("PACF of 'amazon'")
plt.show()

#====================AR MODEL====================

ar_traffic = ARIMA(train_traffic, order=(4, 0, 0))
ar_traffic_fitted = ar_traffic.fit()

ar_predictions_ar_traffic = ar_traffic_fitted.predict(start=len(train_traffic), end=len(train_traffic) + len(test_traffic) - 1)

ar_traffic_rmse = np.sqrt(mean_squared_error(test_traffic, ar_predictions_ar_traffic))
print("RMSE for AR model:", ar_traffic_rmse)

print(ar_traffic_fitted.summary())

#====================MA MODEL====================

ma_amazon = ARIMA(train_amazon, order=(0, 0, 2))
ma_amazon_fitted = ma_amazon.fit()

ma_predictions_ma_amazon = ma_amazon_fitted.predict(start=len(train_amazon), end=len(train_amazon) + len(test_amazon) - 1)

ma_amazon_rmse = np.sqrt(mean_squared_error(test_amazon, ma_predictions_ma_amazon))
print("RMSE for MA model:", ma_amazon_rmse)

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_amazon), len(train_amazon) + len(test_amazon)), test_amazon, label="Actual", color="blue")
plt.plot(range(len(train_amazon), len(train_amazon) + len(test_amazon)), ma_predictions_ma_amazon, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'amazon' (using MA(2))")
plt.legend()
plt.grid(True)

plt.show()

#====================ARMA MODEL====================

arma_combo = ARIMA(train_traffic, order=(3, 0, 2))
arma_combo_fitted = arma_combo.fit()

arma_predictions_arma_combo = arma_combo_fitted.predict(start=len(train_traffic), end=len(train_traffic) + len(test_traffic) - 1)

arma_combo_rmse = np.sqrt(mean_squared_error(test_traffic, arma_predictions_arma_combo))
print("RMSE for ARMA model:", arma_combo_rmse)

arma_combo_fitted.save("combo_arma.pkl")

#====================ARIMA MODEL====================

arima_traffic = ARIMA(train_traffic, order=(2, 1, 1))
arima_traffic_fitted = arima_traffic.fit()

arima_predictions_arima_traffic = arima_traffic_fitted.predict(start=len(train_traffic), end=len(train_traffic) + len(test_traffic) - 1)

arima_traffic_rmse = np.sqrt(mean_squared_error(test_traffic, arima_predictions_arima_traffic))
print("RMSE for ARIMA model:", arima_traffic_rmse)

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_traffic), len(train_traffic) + len(test_traffic)), test_traffic, label="Actual", color="blue")
plt.plot(range(len(train_traffic), len(train_traffic) + len(test_traffic)), arima_predictions_arima_traffic, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'traffic' (using ARIMA(2,1,1))")
plt.legend()
plt.grid(True)
plt.savefig("arima_forecast.png")

plt.show()

#====================SARIMA MODEL====================

sarima_amazon = SARIMAX(train_amazon, order=(1, 1, 1), seasonal_order=(1, 0, 1, 12))
sarima_amazon_fitted = sarima_amazon.fit()

sarima_predictions_sarima_amazon = sarima_amazon_fitted.predict(start=len(train_amazon), end=len(train_amazon) + len(test_amazon) - 1)

sarima_amazon_rmse = np.sqrt(mean_squared_error(test_amazon, sarima_predictions_sarima_amazon))
print("RMSE for SARIMA model:", sarima_amazon_rmse)

print(sarima_amazon_fitted.summary())

#====================ARCH MODEL====================

train_arch_amazon_returns = 100 * train_amazon.pct_change().dropna()
test_arch_amazon_returns = 100 * test_amazon.pct_change().dropna()
arch_amazon = arch_model(train_arch_amazon_returns, mean='Zero', vol='ARCH', p=1)
arch_amazon_fitted = arch_amazon.fit()

arch_amazon_arch_forecast = arch_amazon_fitted.forecast(horizon=len(test_amazon))
arch_predictions_arch_amazon = np.sqrt(arch_amazon_arch_forecast.variance.values[-1, :])

#arch_amazon_rmse = np.sqrt(mean_squared_error(test_amazon, arch_predictions_arch_amazon))
#print("RMSE for ARCH model:", arch_amazon_rmse)

#====================GARCH MODEL====================

train_garch_traffic_returns = 100 * train_traffic.pct_change().dropna()
test_garch_traffic_returns = 100 * test_traffic.pct_change().dropna()
garch_traffic = arch_model(train_garch_traffic_returns, mean='Zero', vol='GARCH', p=1, q=1)
garch_traffic_fitted = garch_traffic.fit()

garch_traffic_garch_forecast = garch_traffic_fitted.forecast(horizon=len(test_traffic))
garch_predictions_garch_traffic = np.sqrt(garch_traffic_garch_forecast.variance.values[-1, :])

#garch_traffic_rmse = np.sqrt(mean_squared_error(test_traffic, garch_predictions_garch_traffic))
#print("RMSE for GARCH model:", garch_traffic_rmse)

#====================LSTM MODEL====================

scaler_lstm_amazon = MinMaxScaler(feature_range=(0, 1))
train_scaled_lstm_amazon = scaler_lstm_amazon.fit_transform(train_amazon)
test_scaled_lstm_amazon = scaler_lstm_amazon.transform(test_amazon)

def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length, 0])
        y.append(data[i + sequence_length, 0])
    return np.array(X), np.array(y)

sequence_length_lstm_amazon = 14
X_train_lstm_amazon, y_train_lstm_amazon = create_sequences(train_scaled_lstm_amazon, sequence_length_lstm_amazon)
X_test_lstm_amazon, y_test_lstm_amazon = create_sequences(test_scaled_lstm_amazon, sequence_length_lstm_amazon)

X_train_lstm_amazon = X_train_lstm_amazon.reshape((X_train_lstm_amazon.shape[0], X_train_lstm_amazon.shape[1], 1))
X_test_lstm_amazon = X_test_lstm_amazon.reshape((X_test_lstm_amazon.shape[0], X_test_lstm_amazon.shape[1], 1))

lstm_amazon = Sequential([
    LSTM(128, return_sequences=True, input_shape=(X_train_lstm_amazon.shape[1], 1)),
    Dropout(0.1),
    
    LSTM(128, return_sequences=False),
    Dropout(0.1),
    Dense(64),
    Dense(1)
])

lstm_amazon.compile(optimizer="adam", loss="mse")


history = lstm_amazon.fit(X_train_lstm_amazon, y_train_lstm_amazon, batch_size=16, epochs=50, validation_data=(X_test_lstm_amazon, y_test_lstm_amazon))

train_predictions_lstm_amazon = lstm_amazon.predict(X_train_lstm_amazon)
test_predictions_lstm_amazon = lstm_amazon.predict(X_test_lstm_amazon)

train_predictions_lstm_amazon = scaler_lstm_amazon.inverse_transform(train_predictions_lstm_amazon)
y_train_lstm_amazon = scaler_lstm_amazon.inverse_transform(y_train_lstm_amazon.reshape(-1, 1))
test_predictions_lstm_amazon = scaler_lstm_amazon.inverse_transform(test_predictions_lstm_amazon)
y_test_lstm_amazon = scaler_lstm_amazon.inverse_transform(y_test_lstm_amazon.reshape(-1, 1))

lstm_amazon.save("amazon_lstm.h5")


plt.figure(figsize=(12, 6))
plt.plot(train_amazon.index[sequence_length_lstm_amazon:], y_train_lstm_amazon, label="Training True Values", color="blue")
plt.plot(train_amazon.index[sequence_length_lstm_amazon:], train_predictions_lstm_amazon, label="Training Predictions", color="cyan")
plt.plot(test_amazon.index[sequence_length_lstm_amazon:], y_test_lstm_amazon, label="Testing True Values", color="orange")
plt.plot(test_amazon.index[sequence_length_lstm_amazon:], test_predictions_lstm_amazon, label="Testing Predictions", color="red")
plt.title("Price Prediction with LSTM")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()

