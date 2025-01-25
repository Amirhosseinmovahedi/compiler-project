import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

warnings.filterwarnings("ignore")

#====================DATAFRAME LOAD====================

nvda = pd.read_csv('my_data.csv')
nvda['Date'] = pd.to_datetime(nvda['Date'])
nvda = nvda.set_index('Date')

nvda = nvda[["Close"]]
nvda = nvda.dropna()

train_end_date = "2022-01-01"
test_end_date = "2022-04-01"

train_nvda = nvda.loc[:train_end_date]
test_nvda = nvda.loc[train_end_date:test_end_date]

#====================ADF TEST====================

adf_result = adfuller(nvda)
print('Dataframe:', 'nvda')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\t{key}: {value}')
print('\n')

#====================ARIMA MODEL====================

my_model = ARIMA(train_nvda, order=(1, 1, 1))
my_model_fitted = my_model.fit()

arima_predictions_my_model = my_model_fitted.predict(start=len(train_nvda), end=len(train_nvda) + len(test_nvda) - 1)

my_model_rmse = np.sqrt(mean_squared_error(test_nvda, arima_predictions_my_model))
print("RMSE for ARIMA model:", my_model_rmse)

print(my_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_nvda), len(train_nvda) + len(test_nvda)), test_nvda, label="Actual", color="blue")
plt.plot(range(len(train_nvda), len(train_nvda) + len(test_nvda)), arima_predictions_my_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of 'nvda' (using ARIMA(1,1,1))")
plt.legend()
plt.grid(True)

plt.show()

my_model_fitted.save("nvda_arima.pkl")

