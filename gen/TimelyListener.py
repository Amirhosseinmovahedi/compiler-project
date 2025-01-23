# Generated from C:/Users/Amirhossein/Desktop/Compiler/antlr_projects/compiler-project/grammar/Timely.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TimelyParser import TimelyParser
else:
    from TimelyParser import TimelyParser

# This class defines a complete listener for a parse tree produced by TimelyParser.
class TimelyListener(ParseTreeListener):

    # Enter a parse tree produced by TimelyParser#start.
    def enterStart(self, ctx:TimelyParser.StartContext):
        pass

    # Exit a parse tree produced by TimelyParser#start.
    def exitStart(self, ctx:TimelyParser.StartContext):
        pass


    # Enter a parse tree produced by TimelyParser#program.
    def enterProgram(self, ctx:TimelyParser.ProgramContext):
        pass

    # Exit a parse tree produced by TimelyParser#program.
    def exitProgram(self, ctx:TimelyParser.ProgramContext):
        pass


    # Enter a parse tree produced by TimelyParser#statement.
    def enterStatement(self, ctx:TimelyParser.StatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#statement.
    def exitStatement(self, ctx:TimelyParser.StatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#dataframeLoadStatement.
    def enterDataframeLoadStatement(self, ctx:TimelyParser.DataframeLoadStatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#dataframeLoadStatement.
    def exitDataframeLoadStatement(self, ctx:TimelyParser.DataframeLoadStatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#tickerLoadStatement.
    def enterTickerLoadStatement(self, ctx:TimelyParser.TickerLoadStatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#tickerLoadStatement.
    def exitTickerLoadStatement(self, ctx:TimelyParser.TickerLoadStatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#acfStatement.
    def enterAcfStatement(self, ctx:TimelyParser.AcfStatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#acfStatement.
    def exitAcfStatement(self, ctx:TimelyParser.AcfStatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#pacfStatement.
    def enterPacfStatement(self, ctx:TimelyParser.PacfStatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#pacfStatement.
    def exitPacfStatement(self, ctx:TimelyParser.PacfStatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#testStatement.
    def enterTestStatement(self, ctx:TimelyParser.TestStatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#testStatement.
    def exitTestStatement(self, ctx:TimelyParser.TestStatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#modelStatement.
    def enterModelStatement(self, ctx:TimelyParser.ModelStatementContext):
        pass

    # Exit a parse tree produced by TimelyParser#modelStatement.
    def exitModelStatement(self, ctx:TimelyParser.ModelStatementContext):
        pass


    # Enter a parse tree produced by TimelyParser#price_value.
    def enterPrice_value(self, ctx:TimelyParser.Price_valueContext):
        pass

    # Exit a parse tree produced by TimelyParser#price_value.
    def exitPrice_value(self, ctx:TimelyParser.Price_valueContext):
        pass


    # Enter a parse tree produced by TimelyParser#csv_address.
    def enterCsv_address(self, ctx:TimelyParser.Csv_addressContext):
        pass

    # Exit a parse tree produced by TimelyParser#csv_address.
    def exitCsv_address(self, ctx:TimelyParser.Csv_addressContext):
        pass


    # Enter a parse tree produced by TimelyParser#ticker_name.
    def enterTicker_name(self, ctx:TimelyParser.Ticker_nameContext):
        pass

    # Exit a parse tree produced by TimelyParser#ticker_name.
    def exitTicker_name(self, ctx:TimelyParser.Ticker_nameContext):
        pass


    # Enter a parse tree produced by TimelyParser#time.
    def enterTime(self, ctx:TimelyParser.TimeContext):
        pass

    # Exit a parse tree produced by TimelyParser#time.
    def exitTime(self, ctx:TimelyParser.TimeContext):
        pass


    # Enter a parse tree produced by TimelyParser#value.
    def enterValue(self, ctx:TimelyParser.ValueContext):
        pass

    # Exit a parse tree produced by TimelyParser#value.
    def exitValue(self, ctx:TimelyParser.ValueContext):
        pass


    # Enter a parse tree produced by TimelyParser#dataframe_name.
    def enterDataframe_name(self, ctx:TimelyParser.Dataframe_nameContext):
        pass

    # Exit a parse tree produced by TimelyParser#dataframe_name.
    def exitDataframe_name(self, ctx:TimelyParser.Dataframe_nameContext):
        pass


    # Enter a parse tree produced by TimelyParser#train_end.
    def enterTrain_end(self, ctx:TimelyParser.Train_endContext):
        pass

    # Exit a parse tree produced by TimelyParser#train_end.
    def exitTrain_end(self, ctx:TimelyParser.Train_endContext):
        pass


    # Enter a parse tree produced by TimelyParser#test_end.
    def enterTest_end(self, ctx:TimelyParser.Test_endContext):
        pass

    # Exit a parse tree produced by TimelyParser#test_end.
    def exitTest_end(self, ctx:TimelyParser.Test_endContext):
        pass


    # Enter a parse tree produced by TimelyParser#visualize.
    def enterVisualize(self, ctx:TimelyParser.VisualizeContext):
        pass

    # Exit a parse tree produced by TimelyParser#visualize.
    def exitVisualize(self, ctx:TimelyParser.VisualizeContext):
        pass


    # Enter a parse tree produced by TimelyParser#summary.
    def enterSummary(self, ctx:TimelyParser.SummaryContext):
        pass

    # Exit a parse tree produced by TimelyParser#summary.
    def exitSummary(self, ctx:TimelyParser.SummaryContext):
        pass


    # Enter a parse tree produced by TimelyParser#interval.
    def enterInterval(self, ctx:TimelyParser.IntervalContext):
        pass

    # Exit a parse tree produced by TimelyParser#interval.
    def exitInterval(self, ctx:TimelyParser.IntervalContext):
        pass


    # Enter a parse tree produced by TimelyParser#start_time.
    def enterStart_time(self, ctx:TimelyParser.Start_timeContext):
        pass

    # Exit a parse tree produced by TimelyParser#start_time.
    def exitStart_time(self, ctx:TimelyParser.Start_timeContext):
        pass


    # Enter a parse tree produced by TimelyParser#end_time.
    def enterEnd_time(self, ctx:TimelyParser.End_timeContext):
        pass

    # Exit a parse tree produced by TimelyParser#end_time.
    def exitEnd_time(self, ctx:TimelyParser.End_timeContext):
        pass


    # Enter a parse tree produced by TimelyParser#lags.
    def enterLags(self, ctx:TimelyParser.LagsContext):
        pass

    # Exit a parse tree produced by TimelyParser#lags.
    def exitLags(self, ctx:TimelyParser.LagsContext):
        pass


    # Enter a parse tree produced by TimelyParser#type.
    def enterType(self, ctx:TimelyParser.TypeContext):
        pass

    # Exit a parse tree produced by TimelyParser#type.
    def exitType(self, ctx:TimelyParser.TypeContext):
        pass


    # Enter a parse tree produced by TimelyParser#p.
    def enterP(self, ctx:TimelyParser.PContext):
        pass

    # Exit a parse tree produced by TimelyParser#p.
    def exitP(self, ctx:TimelyParser.PContext):
        pass


    # Enter a parse tree produced by TimelyParser#q.
    def enterQ(self, ctx:TimelyParser.QContext):
        pass

    # Exit a parse tree produced by TimelyParser#q.
    def exitQ(self, ctx:TimelyParser.QContext):
        pass


    # Enter a parse tree produced by TimelyParser#d.
    def enterD(self, ctx:TimelyParser.DContext):
        pass

    # Exit a parse tree produced by TimelyParser#d.
    def exitD(self, ctx:TimelyParser.DContext):
        pass


    # Enter a parse tree produced by TimelyParser#ps.
    def enterPs(self, ctx:TimelyParser.PsContext):
        pass

    # Exit a parse tree produced by TimelyParser#ps.
    def exitPs(self, ctx:TimelyParser.PsContext):
        pass


    # Enter a parse tree produced by TimelyParser#qs.
    def enterQs(self, ctx:TimelyParser.QsContext):
        pass

    # Exit a parse tree produced by TimelyParser#qs.
    def exitQs(self, ctx:TimelyParser.QsContext):
        pass


    # Enter a parse tree produced by TimelyParser#ds.
    def enterDs(self, ctx:TimelyParser.DsContext):
        pass

    # Exit a parse tree produced by TimelyParser#ds.
    def exitDs(self, ctx:TimelyParser.DsContext):
        pass



del TimelyParser