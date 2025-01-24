import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import adfuller


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

downloaded_data = yf.download("BTC-USD", start="2020-01-01", end="2023-01-01", interval="1d")
downloaded_data = downloaded_data[["Close"]]
downloaded_data = downloaded_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_downloaded_data = downloaded_data.loc[:train_end_date]
test_downloaded_data = downloaded_data.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_downloaded_data.index, train_downloaded_data["Close"], label="Training Data", color="blue")
plt.plot(test_downloaded_data.index, test_downloaded_data["Close"], label="Testing Data", color="orange")
plt.title("BTC-USD Close Price (Training and Testing Data)")
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

