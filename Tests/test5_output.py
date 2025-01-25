import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf


#====================DATAFRAME LOAD====================

climate_df = pd.read_csv('my_data.csv')
climate_df['Date'] = pd.to_datetime(climate_df['Date'])
climate_df = climate_df.set_index('Date')

climate_df = climate_df[["Close"]]
climate_df = climate_df.dropna()

train_end_date = "2020-12-31"
test_end_date = "2021-12-31"

train_climate_df = climate_df.loc[:train_end_date]
test_climate_df = climate_df.loc[train_end_date:test_end_date]

#====================ACF PLOT====================

acf_vals = acf(climate_df)
num_lags = 20
plt.bar(range(num_lags), acf_vals[:num_lags])
plt.title('ACF of climate_df')
plt.show()

#====================PACF PLOT====================

plot_pacf(climate_df, lags=20, title='PACF of climate_df')
plt.show()

#====================ARMA MODEL====================

my_model = ARIMA(train_climate_df, order=(2, 0, 1))
my_model_fitted = my_model.fit()

arma_predictions_my_model = my_model_fitted.predict(start=len(train_climate_df), end=len(train_climate_df) + len(test_climate_df) - 1)

my_model_rmse = np.sqrt(mean_squared_error(test_climate_df, arma_predictions_my_model))
print("RMSE for ARMA model:", my_model_rmse)

print(my_model_fitted.summary())

plt.figure(figsize=(12, 6))
plt.plot(range(len(train_climate_df), len(train_climate_df) + len(test_climate_df)), test_climate_df, label="Actual", color="blue")
plt.plot(range(len(train_climate_df), len(train_climate_df) + len(test_climate_df)), arma_predictions_my_model, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.grid(True)

plt.show()

