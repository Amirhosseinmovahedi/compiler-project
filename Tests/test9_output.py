import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential


#====================TICKER LOAD====================

apple = yf.download("AAPL", start="2024-01-01", end="2024-12-31", interval="1h")
apple = apple[["Close"]]
apple = apple.dropna()

train_end_date = "2024-10-31"
test_end_date = "2024-12-31"

train_apple = apple.loc[:train_end_date]
test_apple = apple.loc[train_end_date:test_end_date]

#====================LSTM MODEL====================

scaler_apple_lstm = MinMaxScaler(feature_range=(0, 1))
train_scaled_apple_lstm = scaler_apple_lstm.fit_transform(train_apple)
test_scaled_apple_lstm = scaler_apple_lstm.transform(test_apple)

def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length, 0])
        y.append(data[i + sequence_length, 0])
    return np.array(X), np.array(y)

sequence_length_apple_lstm = 30
X_train_apple_lstm, y_train_apple_lstm = create_sequences(train_scaled_apple_lstm, sequence_length_apple_lstm)
X_test_apple_lstm, y_test_apple_lstm = create_sequences(test_scaled_apple_lstm, sequence_length_apple_lstm)

X_train_apple_lstm = X_train_apple_lstm.reshape((X_train_apple_lstm.shape[0], X_train_apple_lstm.shape[1], 1))
X_test_apple_lstm = X_test_apple_lstm.reshape((X_test_apple_lstm.shape[0], X_test_apple_lstm.shape[1], 1))

apple_lstm = Sequential([
    LSTM(100, return_sequences=True, input_shape=(X_train_apple_lstm.shape[1], 1)),
    Dropout(0.3),
    
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(100, return_sequences=False),
    Dropout(0.3),
    Dense(50),
    Dense(1)
])

apple_lstm.compile(optimizer="rmsprop", loss="mae")


history = apple_lstm.fit(X_train_apple_lstm, y_train_apple_lstm, batch_size=64, epochs=20, validation_data=(X_test_apple_lstm, y_test_apple_lstm))

train_predictions_apple_lstm = apple_lstm.predict(X_train_apple_lstm)
test_predictions_apple_lstm = apple_lstm.predict(X_test_apple_lstm)

train_predictions_apple_lstm = scaler_apple_lstm.inverse_transform(train_predictions_apple_lstm)
y_train_apple_lstm = scaler_apple_lstm.inverse_transform(y_train_apple_lstm.reshape(-1, 1))
test_predictions_apple_lstm = scaler_apple_lstm.inverse_transform(test_predictions_apple_lstm)
y_test_apple_lstm = scaler_apple_lstm.inverse_transform(y_test_apple_lstm.reshape(-1, 1))

apple_lstm.save("apple_lstm.h5")


plt.figure(figsize=(12, 6))
plt.plot(train_apple.index[sequence_length_apple_lstm:], y_train_apple_lstm, label="Training True Values", color="blue")
plt.plot(train_apple.index[sequence_length_apple_lstm:], train_predictions_apple_lstm, label="Training Predictions", color="cyan")
plt.plot(test_apple.index[sequence_length_apple_lstm:], y_test_apple_lstm, label="Testing True Values", color="orange")
plt.plot(test_apple.index[sequence_length_apple_lstm:], test_predictions_apple_lstm, label="Testing Predictions", color="red")
plt.title("Price Prediction with LSTM")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()

