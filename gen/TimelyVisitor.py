# Generated from C:/Users/Amirhossein/Desktop/Compiler/antlr_projects/compiler-project/grammar/Timely.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TimelyParser import TimelyParser
else:
    from TimelyParser import TimelyParser

# This class defines a complete generic visitor for a parse tree produced by TimelyParser.

class TimelyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TimelyParser#start.
    def visitStart(self, ctx:TimelyParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#program.
    def visitProgram(self, ctx:TimelyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#statement.
    def visitStatement(self, ctx:TimelyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#dataframeLoadStatement.
    def visitDataframeLoadStatement(self, ctx:TimelyParser.DataframeLoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#tickerLoadStatement.
    def visitTickerLoadStatement(self, ctx:TimelyParser.TickerLoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#acfStatement.
    def visitAcfStatement(self, ctx:TimelyParser.AcfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#pacfStatement.
    def visitPacfStatement(self, ctx:TimelyParser.PacfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#testStatement.
    def visitTestStatement(self, ctx:TimelyParser.TestStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#modelStatement.
    def visitModelStatement(self, ctx:TimelyParser.ModelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#price_value.
    def visitPrice_value(self, ctx:TimelyParser.Price_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#csv_address.
    def visitCsv_address(self, ctx:TimelyParser.Csv_addressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#ticker_name.
    def visitTicker_name(self, ctx:TimelyParser.Ticker_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#time.
    def visitTime(self, ctx:TimelyParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#value.
    def visitValue(self, ctx:TimelyParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#dataframe_name.
    def visitDataframe_name(self, ctx:TimelyParser.Dataframe_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#train_end.
    def visitTrain_end(self, ctx:TimelyParser.Train_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#test_end.
    def visitTest_end(self, ctx:TimelyParser.Test_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#visualize.
    def visitVisualize(self, ctx:TimelyParser.VisualizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#summary.
    def visitSummary(self, ctx:TimelyParser.SummaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#interval.
    def visitInterval(self, ctx:TimelyParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#start_time.
    def visitStart_time(self, ctx:TimelyParser.Start_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#end_time.
    def visitEnd_time(self, ctx:TimelyParser.End_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#lags.
    def visitLags(self, ctx:TimelyParser.LagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#type.
    def visitType(self, ctx:TimelyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#p.
    def visitP(self, ctx:TimelyParser.PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#q.
    def visitQ(self, ctx:TimelyParser.QContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#d.
    def visitD(self, ctx:TimelyParser.DContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#ps.
    def visitPs(self, ctx:TimelyParser.PsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#qs.
    def visitQs(self, ctx:TimelyParser.QsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TimelyParser#ds.
    def visitDs(self, ctx:TimelyParser.DsContext):
        return self.visitChildren(ctx)



del TimelyParser