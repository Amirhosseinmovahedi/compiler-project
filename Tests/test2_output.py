import matplotlib.pyplot as plt
import pandas as pd


#====================DATAFRAME LOAD====================

my_data = pd.read_csv('my_data.csv')
my_data['time'] = pd.to_datetime(my_data['time'])
my_data = my_data.set_index('time')

my_data = my_data[["Close"]]
my_data = my_data.dropna()

train_end_date = "2022-06-30"
test_end_date = "2023-01-01"

train_my_data = my_data.loc[:train_end_date]
test_my_data = my_data.loc[train_end_date:test_end_date]

plt.figure(figsize=(12, 6))
plt.plot(train_my_data.index, train_my_data['Close'], label='Training Data', color='blue')
plt.plot(test_my_data.index, test_my_data['Close'], label='Testing Data', color='orange')
plt.title('my_data Close (Training and Testing Split)')
plt.xlabel('Date')
plt.ylabel('Close')
plt.legend()
plt.grid(True)
plt.show()
