from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.metrics import mean_squared_error
from tensorflow.keras.layers import LSTM, Dense, Dropout
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from tensorflow.keras.models import Sequential


my_data = yf.download("BTC-USD", start="2020-01-01", end="2023-01-01", interval="1d")
my_data = my_data[["Close"]]
my_data = my_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_my_data = my_data.loc[:train_end_date]
test_my_data = my_data.loc[train_end_date:test_end_date]

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
plt.title("Actual vs Predicted Values")
plt.legend()
plt.grid(True)

plt.show()

