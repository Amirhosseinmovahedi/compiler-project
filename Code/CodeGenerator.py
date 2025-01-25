class CodeGenerator:
    def __init__(self):
        self.non_operands = ['program', 'dataframeLoadStatement',
                             'tickerLoadStatement', 'acfStatement',
                             'pacfStatement', 'testStatement',
                             'ar_model',
                             'ma_model',
                             'arma_model',
                             'arima_model',
                             'sarima_model',
                             'arch_model',
                             'garch_model',
                             'lstm_model',
                             ]

        self.operand_stack = []
        self.code_stack = []
        self.import_codes = []

    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, post_order_array):
        for item in post_order_array:
            if not self.is_operand(item["label"]):
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string
        return result

    def generate_code_based_on_non_operand(self, item):
        if item == "program":
            self.generate_program()

        elif item == "dataframeLoadStatement":
            self.generate_dataframeLoadStatement()

        elif item == "ar_model":
            self.generate_ar_model()

        elif item == "ma_model":
            self.generate_ma_model()

        elif item == "arma_model":
            self.generate_arma_model()

        elif item == "arima_model":
            self.generate_arima_model()

        elif item == "sarima_model":
            self.generate_sarima_model()

        elif item == "arch_model":
            self.generate_arch_model()

        elif item == "garch_model":
            self.generate_garch_model()

        elif item == "acfStatement":
            self.generate_acfStatement()

        elif item == "pacfStatement":
            self.generate_pacfStatement()

        elif item == "testStatement":
            self.generate_testStatement()

        elif item == "tickerLoadStatement":
            self.generate_tickerLoadStatement()

        elif item == "lstm_model":
            self.generate_lstm_model()

    def generate_program(self):
        self.import_codes.append('import warnings')

        res = ''
        self.import_codes = list(set(self.import_codes))
        self.import_codes.sort(key=lambda x: (tuple(-ord(c) for c in x.split()[0]) ,x.split()[1]))
        for i in self.import_codes:
            res += i + '\n'

        res += '\nwarnings.filterwarnings("ignore")\n\n'
        self.code_stack.insert(0, res)

    def generate_ar_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        p = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================AR MODEL====================\n\n")

        self.code_stack.append(f"""{model_name} = ARIMA(train_{dataframe_name}, order=({p}, 0, 0))
{model_name}_fitted = {model_name}.fit()

ar_predictions_{model_name} = {model_name}_fitted.predict(start=len(train_{dataframe_name}), end=len(train_{dataframe_name}) + len(test_{dataframe_name}) - 1)

{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, ar_predictions_{model_name}))
print("RMSE for AR model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from statsmodels.tsa.arima.model import ARIMA")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), test_{dataframe_name}, label="Actual", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), ar_predictions_{model_name}, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of '{dataframe_name}' (using AR({p}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"{model_name}_fitted.save({temp_model_stack[index][:-1]}.pkl\")\n\n")

    def generate_tickerLoadStatement(self):
        temp_ticker_stack = []
        current_operand = self.operand_stack.pop()
        if current_operand != 'end_scope_operator':
            self.code_stack.append(current_operand)
            return
        while current_operand != 'begin_scope_operator':
            current_operand = self.operand_stack.pop()
            temp_ticker_stack.append(current_operand)
        temp_ticker_stack.pop()

        coin_name = temp_ticker_stack.pop()
        dataframe_name = temp_ticker_stack.pop()
        interval = temp_ticker_stack.pop()
        start = temp_ticker_stack.pop()
        end = temp_ticker_stack.pop()
        position = temp_ticker_stack.pop()
        train_end = temp_ticker_stack.pop()
        test_end = temp_ticker_stack.pop()

        self.code_stack.append("#====================TICKER LOAD====================\n\n")

        self.code_stack.append(f"""{dataframe_name} = yf.download({coin_name}, start="{start}", end="{end}", interval={interval})
{dataframe_name} = {dataframe_name}[["{position}"]]
{dataframe_name} = {dataframe_name}.dropna()

train_end_date = "{train_end}"
test_end_date = "{test_end}"

train_{dataframe_name} = {dataframe_name}.loc[:train_end_date]
test_{dataframe_name} = {dataframe_name}.loc[train_end_date:test_end_date]\n\n""")

        if len(temp_ticker_stack) > 0:
            visualize = temp_ticker_stack.pop()
            if visualize == 'True':
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(train_{dataframe_name}.index, train_{dataframe_name}["{position}"], label="Training Data", color="blue")
plt.plot(test_{dataframe_name}.index, test_{dataframe_name}["{position}"], label="Testing Data", color="orange")
plt.title("{coin_name[1:-1]} {position} Price (Training and Testing Data)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()\n\n""")
                self.import_codes.append("import matplotlib.pyplot as plt")

        self.import_codes.append("import yfinance as yf")

    def generate_dataframeLoadStatement(self):
        temp_stack = []
        current_operand = self.operand_stack.pop()
        if current_operand != 'end_scope_operator':
            self.code_stack.append(current_operand)
            return
        while current_operand != 'begin_scope_operator':
            current_operand = self.operand_stack.pop()
            temp_stack.append(current_operand)
        temp_stack.pop()  # Remove 'begin_scope_operator'
        temp_stack.reverse()

        # Extract parameters
        visualize_bool = temp_stack.pop() if len(temp_stack) == 7 else None
        test_end = temp_stack.pop()
        train_end = temp_stack.pop()
        value = temp_stack.pop().strip('"')
        time_col = temp_stack.pop().strip('"')
        alias = temp_stack.pop()
        source = temp_stack.pop().strip('"')

        # Generate code
        self.code_stack.append(f"""#====================DATAFRAME LOAD====================

{alias} = pd.read_csv('{source}.csv')
{alias}['{time_col}'] = pd.to_datetime({alias}['{time_col}'])
{alias} = {alias}.set_index('{time_col}')

{alias} = {alias}[["{value}"]]
{alias} = {alias}.dropna()

train_end_date = "{train_end}"
test_end_date = "{test_end}"

train_{alias} = {alias}.loc[:train_end_date]
test_{alias} = {alias}.loc[train_end_date:test_end_date]\n\n""")

        if visualize_bool == 'True':
            self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(train_{alias}.index, train_{alias}['{value}'], label='Training Data', color='blue')
plt.plot(test_{alias}.index, test_{alias}['{value}'], label='Testing Data', color='orange')
plt.title('{alias} {value} (Training and Testing Split)')
plt.xlabel('Date')
plt.ylabel('{value}')
plt.legend()
plt.grid(True)
plt.show()\n\n""")
            self.import_codes.append("import matplotlib.pyplot as plt")
        self.import_codes.append("import pandas as pd")

    def generate_ma_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        q = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================MA MODEL====================\n\n")

        self.code_stack.append(f"""{model_name} = ARIMA(train_{dataframe_name}, order=(0, 0, {q}))
{model_name}_fitted = {model_name}.fit()

ma_predictions_{model_name} = {model_name}_fitted.predict(start=len(train_{dataframe_name}), end=len(train_{dataframe_name}) + len(test_{dataframe_name}) - 1)

{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, ma_predictions_{model_name}))
print("RMSE for MA model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from statsmodels.tsa.arima.model import ARIMA")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), test_{dataframe_name}, label="Actual", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), ma_predictions_{model_name}, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of '{dataframe_name}' (using MA({q}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"{model_name}_fitted.save({temp_model_stack[index][:-1]}.pkl\")\n\n")

    def generate_arma_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        p = temp_model_stack.pop()
        q = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================ARMA MODEL====================\n\n")

        self.code_stack.append(f"""{model_name} = ARIMA(train_{dataframe_name}, order=({p}, 0, {q}))
{model_name}_fitted = {model_name}.fit()

arma_predictions_{model_name} = {model_name}_fitted.predict(start=len(train_{dataframe_name}), end=len(train_{dataframe_name}) + len(test_{dataframe_name}) - 1)

{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, arma_predictions_{model_name}))
print("RMSE for ARMA model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from statsmodels.tsa.arima.model import ARIMA")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), test_{dataframe_name}, label="Actual", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), arma_predictions_{model_name}, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of '{dataframe_name}' (using ARMA({p},{q}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"{model_name}_fitted.save({temp_model_stack[index][:-1]}.pkl\")\n\n")

    def generate_arima_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        p = temp_model_stack.pop()
        d = temp_model_stack.pop()
        q = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================ARIMA MODEL====================\n\n")

        self.code_stack.append(f"""{model_name} = ARIMA(train_{dataframe_name}, order=({p}, {d}, {q}))
{model_name}_fitted = {model_name}.fit()

arima_predictions_{model_name} = {model_name}_fitted.predict(start=len(train_{dataframe_name}), end=len(train_{dataframe_name}) + len(test_{dataframe_name}) - 1)

{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, arima_predictions_{model_name}))
print("RMSE for ARIMA model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from statsmodels.tsa.arima.model import ARIMA")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), test_{dataframe_name}, label="Actual", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), arima_predictions_{model_name}, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of '{dataframe_name}' (using ARIMA({p},{d},{q}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"{model_name}_fitted.save({temp_model_stack[index][:-1]}.pkl\")\n\n")

    def generate_sarima_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        p = temp_model_stack.pop()
        d = temp_model_stack.pop()
        q = temp_model_stack.pop()
        ps = temp_model_stack.pop()
        ds = temp_model_stack.pop()
        qs = temp_model_stack.pop()
        s = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================SARIMA MODEL====================\n\n")

        self.code_stack.append(f"""{model_name} = SARIMAX(train_{dataframe_name}, order=({p}, {d}, {q}), seasonal_order=({ps}, {ds}, {qs}, {s}))
{model_name}_fitted = {model_name}.fit()

sarima_predictions_{model_name} = {model_name}_fitted.predict(start=len(train_{dataframe_name}), end=len(train_{dataframe_name}) + len(test_{dataframe_name}) - 1)

{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, sarima_predictions_{model_name}))
print("RMSE for SARIMA model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from statsmodels.tsa.statespace.sarimax import SARIMAX")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), test_{dataframe_name}, label="Actual", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), sarima_predictions_{model_name}, label="Predicted", color="orange")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Actual vs Predicted Values of '{dataframe_name}' (using SARIMA({p},{d},{q})({ps},{ds},{qs},{s}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"{model_name}_fitted.save({temp_model_stack[index][:-1]}.pkl\")\n\n")

    def generate_arch_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        p = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================ARCH MODEL====================\n\n")

        self.code_stack.append(f"""train_{model_name}_returns = 100 * train_{dataframe_name}.pct_change().dropna()
test_{model_name}_returns = 100 * test_{dataframe_name}.pct_change().dropna()
{model_name} = arch_model(train_{model_name}_returns, mean='Zero', vol='ARCH', p={p})
{model_name}_fitted = {model_name}.fit()

{model_name}_arch_forecast = {model_name}_fitted.forecast(horizon=len(test_{dataframe_name}))
arch_predictions_{model_name} = np.sqrt({model_name}_arch_forecast.variance.values[-1, :])

#{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, arch_predictions_{model_name}))
#print("RMSE for ARCH model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from arch import arch_model")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{model_name}_returns)), test_{model_name}_returns, label="Actual Returns", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), arch_predictions_{model_name}, label="Predicted Volatility", color="orange")
plt.xlabel("Time")
plt.title("Actual Returns vs Predicted Volatility of '{dataframe_name}' (using ARCH({p}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            self.import_codes.append("import pickle")
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"""with open({temp_model_stack[index][:-1]}.pkl\", 'wb') as file:
    pickle.dump({model_name}_fitted, file)\n\n""")

    def generate_garch_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        model_name = temp_model_stack.pop()
        p = temp_model_stack.pop()
        q = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n"

        self.code_stack.append("#====================GARCH MODEL====================\n\n")

        self.code_stack.append(f"""train_{model_name}_returns = 100 * train_{dataframe_name}.pct_change().dropna()
test_{model_name}_returns = 100 * test_{dataframe_name}.pct_change().dropna()
{model_name} = arch_model(train_{model_name}_returns, mean='Zero', vol='GARCH', p={p}, q={q})
{model_name}_fitted = {model_name}.fit()

{model_name}_garch_forecast = {model_name}_fitted.forecast(horizon=len(test_{dataframe_name}))
garch_predictions_{model_name} = np.sqrt({model_name}_garch_forecast.variance.values[-1, :])

#{model_name}_rmse = np.sqrt(mean_squared_error(test_{dataframe_name}, garch_predictions_{model_name}))
#print("RMSE for GARCH model:", {model_name}_rmse)\n\n""")

        self.import_codes.append("from arch import arch_model")
        self.import_codes.append("import numpy as np")
        self.import_codes.append("from sklearn.metrics import mean_squared_error")

        if len(temp_model_stack) > 0:
            if 'summary' in temp_model_stack:
                self.code_stack.append(f"print({model_name}_fitted.summary())\n\n")

            if 'visualize' in temp_model_stack:
                self.code_stack.append(f"""plt.figure(figsize=(12, 6))
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{model_name}_returns)), test_{model_name}_returns, label="Actual Returns", color="blue")
plt.plot(range(len(train_{dataframe_name}), len(train_{dataframe_name}) + len(test_{dataframe_name})), garch_predictions_{model_name}, label="Predicted Volatility", color="orange")
plt.xlabel("Time")
plt.title("Actual Returns vs Predicted Volatility of '{dataframe_name}' (using GARCH({p},{q}))")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

                self.import_codes.append("import matplotlib.pyplot as plt")

        if "save_model" in temp_model_stack:
            self.import_codes.append("import pickle")
            index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"""with open({temp_model_stack[index][:-1]}.pkl\", 'wb') as file:
    pickle.dump({model_name}_fitted, file)\n\n""")

    def generate_acfStatement(self):
        plot_type = self.operand_stack.pop()
        lags = self.operand_stack.pop()
        dataframe_name = self.operand_stack.pop()

        self.code_stack.append(f"""#====================ACF PLOT====================\n\n""")

        if plot_type == 'Bar':
            self.code_stack.append(f'''plot_acf({dataframe_name}, lags={lags}, title='ACF of {dataframe_name}')
plt.show()\n\n''')
            self.import_codes.append("from statsmodels.graphics.tsaplots import plot_acf")
        elif plot_type == 'Plot':
            self.code_stack.append(f'''acf_vals = acf({dataframe_name})
num_lags = {lags}
plt.bar(range(num_lags), acf_vals[:num_lags])
plt.title('ACF of '{dataframe_name}'')
plt.show()\n\n''')
            self.import_codes.append("from statsmodels.tsa.stattools import acf")
        else:
            raise ValueError('incorrect value for type argument')
        self.import_codes.append("import matplotlib.pyplot as plt")

    def generate_pacfStatement(self):
        plot_type = self.operand_stack.pop()
        lags = self.operand_stack.pop()
        dataframe_name = self.operand_stack.pop()

        self.code_stack.append(f"""#====================PACF PLOT====================\n\n""")

        if plot_type == 'Bar':
            self.code_stack.append(f'''plot_pacf({dataframe_name}, lags={lags}, title='PACF of {dataframe_name}')
plt.show()\n\n''')
            self.import_codes.append("from statsmodels.graphics.tsaplots import plot_pacf")
        elif plot_type == 'Plot':
            self.code_stack.append(f'''pacf_vals = pacf({dataframe_name})
num_lags = {lags}
plt.bar(range(num_lags), pacf_vals[:num_lags])
plt.title('PACF of '{dataframe_name}'')
plt.show()\n\n''')
            self.import_codes.append("from statsmodels.tsa.stattools import pacf")
        else:
            raise ValueError('incorrect value for type argument')
        self.import_codes.append("import matplotlib.pyplot as plt")

    def generate_testStatement(self):
        dataframe_name = self.operand_stack.pop()

        self.code_stack.append(f"""#====================ADF TEST====================

adf_result = adfuller({dataframe_name})
print('Dataframe:', '{dataframe_name}')
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])
print('Critical Values:')
for key, value in adf_result[4].items():
    print(f'\\t{{key}}: {{value}}')
print('\\n')\n\n""")

        self.import_codes.append("from statsmodels.tsa.stattools import adfuller")

    def generate_lstm_model(self):
        temp_model_stack = []
        current_code = self.operand_stack.pop()
        if current_code != 'end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != 'begin_scope_operator':
            current_code = self.operand_stack.pop()
            temp_model_stack.append(current_code)
        temp_model_stack.pop()
        print(temp_model_stack)

        model_name = temp_model_stack.pop()
        n_layers = temp_model_stack.pop()
        batch_size = temp_model_stack.pop()
        n_epochs = temp_model_stack.pop()
        drop_out = temp_model_stack.pop()
        lstm_neurons = temp_model_stack.pop()
        dense_neurons = temp_model_stack.pop()
        optimizer = temp_model_stack.pop()
        loss_function = temp_model_stack.pop()
        seq_length = temp_model_stack.pop()
        dataframe_name = temp_model_stack.pop()

        summary_code = ''
        if 'summary' in temp_model_stack:
            summary_code += f"{model_name}.summary()"

        additioanl_layers_statement = ''
        number_of_additional_layers = int(n_layers) - 2
        if number_of_additional_layers > 0:
            for i in range(number_of_additional_layers):
                additioanl_layers_statement += f"""
    LSTM(50, return_sequences=True),
    Dropout(0.2),"""

        self.code_stack.append("#====================LSTM MODEL====================\n\n")

        self.code_stack.append(f"""scaler_{model_name} = MinMaxScaler(feature_range=(0, 1))
train_scaled_{model_name} = scaler_{model_name}.fit_transform(train_{dataframe_name})
test_scaled_{model_name} = scaler_{model_name}.transform(test_{dataframe_name})

def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length, 0])
        y.append(data[i + sequence_length, 0])
    return np.array(X), np.array(y)

sequence_length_{model_name} = {seq_length}
X_train_{model_name}, y_train_{model_name} = create_sequences(train_scaled_{model_name}, sequence_length_{model_name})
X_test_{model_name}, y_test_{model_name} = create_sequences(test_scaled_{model_name}, sequence_length_{model_name})

X_train_{model_name} = X_train_{model_name}.reshape((X_train_{model_name}.shape[0], X_train_{model_name}.shape[1], 1))
X_test_{model_name} = X_test_{model_name}.reshape((X_test_{model_name}.shape[0], X_test_{model_name}.shape[1], 1))

{model_name} = Sequential([
    LSTM({lstm_neurons}, return_sequences=True, input_shape=(X_train_{model_name}.shape[1], 1)),
    Dropout({drop_out}),
    {additioanl_layers_statement}
    LSTM({lstm_neurons}, return_sequences=False),
    Dropout({drop_out}),
    Dense({dense_neurons}),
    Dense(1)
])

{model_name}.compile(optimizer={optimizer}, loss={loss_function})
{summary_code}

history = {model_name}.fit(X_train_{model_name}, y_train_{model_name}, batch_size={batch_size}, epochs={n_epochs}, validation_data=(X_test_{model_name}, y_test_{model_name}))

train_predictions_{model_name} = {model_name}.predict(X_train_{model_name})
test_predictions_{model_name} = {model_name}.predict(X_test_{model_name})

train_predictions_{model_name} = scaler_{model_name}.inverse_transform(train_predictions_{model_name})
y_train_{model_name} = scaler_{model_name}.inverse_transform(y_train_{model_name}.reshape(-1, 1))
test_predictions_{model_name} = scaler_{model_name}.inverse_transform(test_predictions_{model_name})
y_test_{model_name} = scaler_{model_name}.inverse_transform(y_test_{model_name}.reshape(-1, 1))\n\n""")

        self.import_codes.append("from sklearn.preprocessing import MinMaxScaler")
        self.import_codes.append("from tensorflow.keras.models import Sequential")
        self.import_codes.append("from tensorflow.keras.layers import LSTM, Dense, Dropout")
        self.import_codes.append("import numpy as np")

        save_statement = ''
        if "save_chart" in temp_model_stack:
            save_chart_index = temp_model_stack.index("save_chart") - 1
            save_statement += f"plt.savefig({temp_model_stack[save_chart_index][:-1]}.png\")\n\n"

        if "save_model" in temp_model_stack:
            save_model_index = temp_model_stack.index("save_model") - 1
            self.code_stack.append(f"{model_name}.save({temp_model_stack[save_model_index][:-1]}.h5\")\n\n")

        if "visualize" in temp_model_stack:
            self.code_stack.append(f"""
plt.figure(figsize=(12, 6))
plt.plot(train_{dataframe_name}.index[sequence_length_{model_name}:], y_train_{model_name}, label="Training True Values", color="blue")
plt.plot(train_{dataframe_name}.index[sequence_length_{model_name}:], train_predictions_{model_name}, label="Training Predictions", color="cyan")
plt.plot(test_{dataframe_name}.index[sequence_length_{model_name}:], y_test_{model_name}, label="Testing True Values", color="orange")
plt.plot(test_{dataframe_name}.index[sequence_length_{model_name}:], test_predictions_{model_name}, label="Testing Predictions", color="red")
plt.title("Price Prediction with LSTM")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

            self.import_codes.append("import matplotlib.pyplot as plt")











