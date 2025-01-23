grammar Timely;

start: program EOF;

program: statement+ ;

statement
    : dataframeLoadStatement
    | tickerLoadStatement
    | acfStatement
    | pacfStatement
    | testStatement
    | modelStatement;

dataframeLoadStatement
    : 'load' 'data' dataframe_name 'as' dataframe_name ',' 'time' '=' time ',' 'value' '=' value ',' 'trainEnd' '=' train_end ',' 'testEnd' '=' test_end (',' 'visualize' '=' visualize_bool)?
    ;

tickerLoadStatement
    : 'load' 'ticker' coin_name 'as' dataframe_name ',' 'interval' '=' interval ',' 'start' '=' start_time ',' 'end' '=' end_time ',' 'value' '=' price_value ',' 'trainEnd' '=' train_end ',' 'testEnd' '=' test_end (',' 'visualize' '=' visualize_bool)?
    ;

acfStatement
    : 'acf' 'data' '=' dataframe_name ',' 'lags' '=' lags ',' 'type' '=' type
    ;

pacfStatement
    : 'pacf' 'data' '=' dataframe_name ',' 'lags' '=' lags ',' 'type' '=' type
    ;

testStatement
    : 'test' 'adf' dataframe_name
    ;

modelStatement
    : ar_model
    | ma_model
    | arma_model
    | arima_model
    | sarima_model
    | arch_model
    | garch_model
    ;

ar_model: 'model' 'AR' dataframe_name '(' 'p' '=' p ')' dataframe_name (',' summary)? (',' visualize)? (',' save_model 'as' model_name)? (',' save_chart 'as' chart_name)?;
ma_model: 'model' 'MA' dataframe_name '(' 'q' '=' q ')' dataframe_name (',' summary)? (',' visualize)? (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?;
arma_model: 'model' 'ARMA' dataframe_name '(' 'p' '=' p ',' 'q' '=' q ')' dataframe_name (',' summary)? (',' visualize)? (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?;
arima_model: 'model' 'ARIMA' dataframe_name '(' 'p' '=' p ',' 'q' '=' q ',' 'd' '=' d ')' dataframe_name (',' summary)? (',' visualize)? (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?;
sarima_model: 'model' 'SARIMA' dataframe_name '(' 'p' '=' p ',' 'q' '=' q ',' 'd' '=' d ')''(' 'P' '=' ps ',' 'Q' '=' qs ',' 'D' '=' ds ')' dataframe_name (',' summary)? (',' visualize)? (',' save_model 'as' model_name)? (',' save_chart 'as' chart_name)?;
arch_model: 'model' 'ARCH' dataframe_name '(' 'p' '=' p ')' dataframe_name (',' summary)? (',' visualize)? (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?;
garch_model: 'model' 'GARCH' dataframe_name '(' 'p' '=' p ',' 'q' '=' q ')' dataframe_name (',' summary)? (',' visualize)? (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?;




save_model: 'save' 'model';
save_chart: 'save' 'chart';
price_value: 'Open' | 'High' | 'Low' | 'Close' | 'Adj Close';
coin_name: STRING;
ticker_name: ID;
model_name: STRING;
chart_name: STRING;
time: STRING;
value: STRING;
dataframe_name: ID;
train_end: DATE;
test_end: DATE;
visualize: 'visualize';
summary: 'summary';
visualize_bool: BOOL;
interval: STRING;
start_time: DATE;
end_time: DATE;
lags: INT;
type: 'Plot' | 'Bar';
p: INT;
q: INT;
d: INT;
ps: INT;
qs: INT;
ds: INT;


fragment YEAR: [0-9][0-9][0-9][0-9];
fragment MONTH: '0'?[0-9] | '1'[0-2];
fragment DAY: '0'?[0-9] | [1-2][0-9] | '3'[0-1];
DATE: YEAR '-' MONTH '-' DAY;
INT: [0-9]+;
BOOL: 'True' | 'False';
ID: [A-Za-z][A-Za-z_0-9]*;
STRING: '"' .*? '"';

WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
