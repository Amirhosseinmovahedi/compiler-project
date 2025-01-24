import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf


#====================DATAFRAME LOAD====================

csv_data = pd.read_csv('my_data.csv')
csv_data['Date'] = pd.to_datetime(csv_data['Date'])
csv_data = csv_data.set_index('Date')

csv_data = csv_data[["Close"]]
csv_data = csv_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_csv_data = csv_data.loc[:train_end_date]
test_csv_data = csv_data.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_csv_data.index, train_csv_data['Close'], label='Training Data', color='blue')
plt.plot(test_csv_data.index, test_csv_data['Close'], label='Testing Data', color='orange')
plt.title('csv_data Close (Training and Testing Split)')
plt.xlabel('Date')
plt.ylabel('Close')
plt.legend()
plt.grid(True)
plt.show()

#====================TICKER LOAD====================

downloaded_data = yf.download("DOGE-USD", start="2020-01-01", end="2023-01-01", interval="1d")
downloaded_data = downloaded_data[["Close"]]
downloaded_data = downloaded_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_downloaded_data = downloaded_data.loc[:train_end_date]
test_downloaded_data = downloaded_data.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_downloaded_data.index, train_downloaded_data["Close"], label="Training Data", color="blue")
plt.plot(test_downloaded_data.index, test_downloaded_data["Close"], label="Testing Data", color="orange")
plt.title("DOGE-USD Close Price (Training and Testing Data)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

#====================ADF TEST====================

adf_result = adfuller(csv_data)
print('Dataframe:', 'csv_data')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\t{key}: {value}')
print('\n')

#====================ADF TEST====================

adf_result = adfuller(downloaded_data)
print('Dataframe:', 'downloaded_data')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\t{key}: {value}')
print('\n')

#====================ACF PLOT====================

plot_acf(csv_data, lags=100, title='ACF of csv_data')
plt.show()

#====================ACF PLOT====================

acf_vals = acf(downloaded_data)
num_lags = 10
plt.bar(range(num_lags), acf_vals[:num_lags])
plt.title('ACF of downloaded_data')
plt.show()

#====================PACF PLOT====================

plot_pacf(csv_data, lags=50, title='PACF of csv_data')
plt.show()

#====================PACF PLOT====================

pacf_vals = pacf(downloaded_data)
num_lags = 5
plt.bar(range(num_lags), pacf_vals[:num_lags])
plt.title('PACF of downloaded_data')
plt.show()

