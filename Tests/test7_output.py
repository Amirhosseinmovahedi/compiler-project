import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

#====================DATAFRAME LOAD====================

m_sales = pd.read_csv('my_data.csv')
m_sales['Date'] = pd.to_datetime(m_sales['Date'])
m_sales = m_sales.set_index('Date')

m_sales = m_sales[["Close"]]
m_sales = m_sales.dropna()

train_end_date = "2021-12-01"
test_end_date = "2022-05-01"

train_m_sales = m_sales.loc[:train_end_date]
test_m_sales = m_sales.loc[train_end_date:test_end_date]

#====================SARIMA MODEL====================

my_model = SARIMAX(train_m_sales, order=(2, 1, 1), seasonal_order=(1, 1, 1, 4))
my_model_fitted = my_model.fit()

sarima_predictions_my_model = my_model_fitted.predict(start=len(train_m_sales), end=len(train_m_sales) + len(test_m_sales) - 1)

my_model_rmse = np.sqrt(mean_squared_error(test_m_sales, sarima_predictions_my_model))
print("RMSE for SARIMA model:", my_model_rmse)

my_model_fitted.save("sarima_monthly.pkl")

