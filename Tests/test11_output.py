import matplotlib.pyplot as plt
import numpy as np
import warnings
import yfinance as yf
from arch import arch_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.stattools import adfuller
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

warnings.filterwarnings("ignore")

#====================TICKER LOAD====================

litecoin = yf.download("LTC-USD", start="2024-10-01", end="2024-12-31", interval="1h")
litecoin = litecoin[["High"]]
litecoin = litecoin.dropna()

train_end_date = "2024-12-15"
test_end_date = "2024-12-31"

train_litecoin = litecoin.loc[:train_end_date]
test_litecoin = litecoin.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_litecoin.index, train_litecoin["High"], label="Training Data", color="blue")
plt.plot(test_litecoin.index, test_litecoin["High"], label="Testing Data", color="orange")
plt.title("LTC-USD High Price (Training and Testing Data)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

#====================ADF TEST====================

adf_result = adfuller(litecoin)
print('Dataframe:', 'litecoin')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\t{key}: {value}')
print('\n')

#====================GARCH MODEL====================

train_vol_model_returns = 100 * train_litecoin.pct_change().dropna()
test_vol_model_returns = 100 * test_litecoin.pct_change().dropna()
vol_model = arch_model(train_vol_model_returns, mean='Zero', vol='GARCH', p=2, q=2)
vol_model_fitted = vol_model.fit()

vol_model_garch_forecast = vol_model_fitted.forecast(horizon=len(test_litecoin))
garch_predictions_vol_model = np.sqrt(vol_model_garch_forecast.variance.values[-1, :])

#vol_model_rmse = np.sqrt(mean_squared_error(test_litecoin, garch_predictions_vol_model))
#print("RMSE for GARCH model:", vol_model_rmse)

print(vol_model_fitted.summary())

#====================LSTM MODEL====================

scaler_crypto_predictor = MinMaxScaler(feature_range=(0, 1))
train_scaled_crypto_predictor = scaler_crypto_predictor.fit_transform(train_litecoin)
test_scaled_crypto_predictor = scaler_crypto_predictor.transform(test_litecoin)

def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length, 0])
        y.append(data[i + sequence_length, 0])
    return np.array(X), np.array(y)

sequence_length_crypto_predictor = 48
X_train_crypto_predictor, y_train_crypto_predictor = create_sequences(train_scaled_crypto_predictor, sequence_length_crypto_predictor)
X_test_crypto_predictor, y_test_crypto_predictor = create_sequences(test_scaled_crypto_predictor, sequence_length_crypto_predictor)

X_train_crypto_predictor = X_train_crypto_predictor.reshape((X_train_crypto_predictor.shape[0], X_train_crypto_predictor.shape[1], 1))
X_test_crypto_predictor = X_test_crypto_predictor.reshape((X_test_crypto_predictor.shape[0], X_test_crypto_predictor.shape[1], 1))

crypto_predictor = Sequential([
    LSTM(200, return_sequences=True, input_shape=(X_train_crypto_predictor.shape[1], 1)),
    Dropout(0.4),
    
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(200, return_sequences=False),
    Dropout(0.4),
    Dense(100),
    Dense(1)
])

crypto_predictor.compile(optimizer="nadam", loss="mean_squared_error")


history = crypto_predictor.fit(X_train_crypto_predictor, y_train_crypto_predictor, batch_size=64, epochs=20, validation_data=(X_test_crypto_predictor, y_test_crypto_predictor))

train_predictions_crypto_predictor = crypto_predictor.predict(X_train_crypto_predictor)
test_predictions_crypto_predictor = crypto_predictor.predict(X_test_crypto_predictor)

train_predictions_crypto_predictor = scaler_crypto_predictor.inverse_transform(train_predictions_crypto_predictor)
y_train_crypto_predictor = scaler_crypto_predictor.inverse_transform(y_train_crypto_predictor.reshape(-1, 1))
test_predictions_crypto_predictor = scaler_crypto_predictor.inverse_transform(test_predictions_crypto_predictor)
y_test_crypto_predictor = scaler_crypto_predictor.inverse_transform(y_test_crypto_predictor.reshape(-1, 1))

crypto_predictor.save("ltc_lstm_v2.h5")


plt.figure(figsize=(12, 6))
plt.plot(train_litecoin.index[sequence_length_crypto_predictor:], y_train_crypto_predictor, label="Training True Values", color="blue")
plt.plot(train_litecoin.index[sequence_length_crypto_predictor:], train_predictions_crypto_predictor, label="Training Predictions", color="cyan")
plt.plot(test_litecoin.index[sequence_length_crypto_predictor:], y_test_crypto_predictor, label="Testing True Values", color="orange")
plt.plot(test_litecoin.index[sequence_length_crypto_predictor:], test_predictions_crypto_predictor, label="Testing Predictions", color="red")
plt.title("Price Prediction with LSTM")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.savefig("lstm_24h_forecast.png")


plt.show()

