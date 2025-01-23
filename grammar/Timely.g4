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
    : dataframe_name '=' '{' 'load' 'data' csv_address ',' 'time' '=' time ',' 'value' '=' value ',' 'trainEnd' '=' train_end ',' 'testEnd' '=' test_end (',' 'visualize' '=' visualize)  '}'
    ;

tickerLoadStatement
    : dataframe_name '=' '{' 'load' 'ticker' ticker_name ',' 'interval' '=' interval ',' 'start' '=' start_time ',' 'end' '=' end_time ',' 'value' '=' price_value ',' 'trainEnd' '=' train_end ',' 'testEnd' '=' test_end (',' 'visualize' '=' visualize)  '}'
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
    : 'model' 'AR' '(' 'p' '=' p ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' save_model 'as' model_name)? (',' save_chart 'as' chart_name)?
    | 'model' 'MA' '(' 'q' '=' q ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?
    | 'model' 'ARMA' '(' 'p' '=' p ',' 'q' '=' q ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?
    | 'model' 'ARIMA' '(' 'p' '=' p ',' 'q' '=' q ',' 'd' '=' d ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?
    | 'model' 'SARIMA' '(' 'p' '=' p ',' 'q' '=' q ',' 'd' '=' d ')''(' 'P' '=' ps ',' 'Q' '=' qs ',' 'D' '=' ds ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' save_model 'as' model_name)? (',' save_chart 'as' chart_name)?
    | 'model' 'ARCH' '(' 'p' '=' p ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?
    | 'model' 'GARCH' '(' 'p' '=' p ',' 'q' '=' q ')' dataframe_name (',' 'summary' '=' summary) (',' 'visualize' '=' visualize) (',' 'save' 'as' model_name)? (',' 'save_chart' 'as' chart_name)?
    ;

save_model: 'save' 'model';
save_chart: 'save' 'chart';
price_value: 'Open' | 'High' | 'Low' | 'Close' | 'Adj Close';
csv_address: ID;
ticker_name: ID;
model_name: STRING;
chart_name: STRING;
time: STRING;
value: STRING;
dataframe_name: ID;
train_end: DATE;
test_end: DATE;
visualize: BOOL;
summary: BOOL;
interval: 's' | 'm' | 'h' | 'd' | 'M' | 'y';
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
