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

        elif item == "mr_model":
            self.generate_mr_model()

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

    def generate_program(self):
        res = ''
        for i in self.import_codes:
            res += i + '\n'

        res += '\n\n'
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
            save_statement += f"plt.savefig(f{temp_model_stack[save_chart_index][:-1]}.png\")\n\n"

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
plt.title("Actual vs Predicted Values")
plt.legend()
plt.grid(True)
{save_statement}
plt.show()\n\n""")

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
plt.title("BTC-USD Close Price (Training and Testing Data)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()\n\n""")
                self.import_codes.append("import matplotlib.pyplot as plt")

        self.import_codes.append("import yfinance as yf")

    def generate_dataframeLoadStatement(self):
        pass # TODO

    def generate_mr_model(self):
        pass # TODO

    def generate_arma_model(self):
        pass # TODO

    def generate_arima_model(self):
        pass # TODO

    def generate_sarima_model(self):
        pass # TODO

    def generate_arch_model(self):
        pass # TODO

    def generate_garch_model(self):
        pass # TODO

    def generate_acfStatement(self):
        pass # TODO

    def generate_pacfStatement(self):
        pass # TODO

    def generate_testStatement(self):
        pass # TODO












