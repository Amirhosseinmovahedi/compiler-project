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


    # Enter a parse tree produced by TimelyParser#ar_model.
    def enterAr_model(self, ctx:TimelyParser.Ar_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#ar_model.
    def exitAr_model(self, ctx:TimelyParser.Ar_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#ma_model.
    def enterMa_model(self, ctx:TimelyParser.Ma_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#ma_model.
    def exitMa_model(self, ctx:TimelyParser.Ma_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#arma_model.
    def enterArma_model(self, ctx:TimelyParser.Arma_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#arma_model.
    def exitArma_model(self, ctx:TimelyParser.Arma_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#arima_model.
    def enterArima_model(self, ctx:TimelyParser.Arima_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#arima_model.
    def exitArima_model(self, ctx:TimelyParser.Arima_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#sarima_model.
    def enterSarima_model(self, ctx:TimelyParser.Sarima_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#sarima_model.
    def exitSarima_model(self, ctx:TimelyParser.Sarima_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#arch_model.
    def enterArch_model(self, ctx:TimelyParser.Arch_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#arch_model.
    def exitArch_model(self, ctx:TimelyParser.Arch_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#garch_model.
    def enterGarch_model(self, ctx:TimelyParser.Garch_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#garch_model.
    def exitGarch_model(self, ctx:TimelyParser.Garch_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#lstm_model.
    def enterLstm_model(self, ctx:TimelyParser.Lstm_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#lstm_model.
    def exitLstm_model(self, ctx:TimelyParser.Lstm_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#save_model.
    def enterSave_model(self, ctx:TimelyParser.Save_modelContext):
        pass

    # Exit a parse tree produced by TimelyParser#save_model.
    def exitSave_model(self, ctx:TimelyParser.Save_modelContext):
        pass


    # Enter a parse tree produced by TimelyParser#save_chart.
    def enterSave_chart(self, ctx:TimelyParser.Save_chartContext):
        pass

    # Exit a parse tree produced by TimelyParser#save_chart.
    def exitSave_chart(self, ctx:TimelyParser.Save_chartContext):
        pass


    # Enter a parse tree produced by TimelyParser#price_value.
    def enterPrice_value(self, ctx:TimelyParser.Price_valueContext):
        pass

    # Exit a parse tree produced by TimelyParser#price_value.
    def exitPrice_value(self, ctx:TimelyParser.Price_valueContext):
        pass


    # Enter a parse tree produced by TimelyParser#coin_name.
    def enterCoin_name(self, ctx:TimelyParser.Coin_nameContext):
        pass

    # Exit a parse tree produced by TimelyParser#coin_name.
    def exitCoin_name(self, ctx:TimelyParser.Coin_nameContext):
        pass


    # Enter a parse tree produced by TimelyParser#ticker_name.
    def enterTicker_name(self, ctx:TimelyParser.Ticker_nameContext):
        pass

    # Exit a parse tree produced by TimelyParser#ticker_name.
    def exitTicker_name(self, ctx:TimelyParser.Ticker_nameContext):
        pass


    # Enter a parse tree produced by TimelyParser#model_name.
    def enterModel_name(self, ctx:TimelyParser.Model_nameContext):
        pass

    # Exit a parse tree produced by TimelyParser#model_name.
    def exitModel_name(self, ctx:TimelyParser.Model_nameContext):
        pass


    # Enter a parse tree produced by TimelyParser#model.
    def enterModel(self, ctx:TimelyParser.ModelContext):
        pass

    # Exit a parse tree produced by TimelyParser#model.
    def exitModel(self, ctx:TimelyParser.ModelContext):
        pass


    # Enter a parse tree produced by TimelyParser#chart_name.
    def enterChart_name(self, ctx:TimelyParser.Chart_nameContext):
        pass

    # Exit a parse tree produced by TimelyParser#chart_name.
    def exitChart_name(self, ctx:TimelyParser.Chart_nameContext):
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


    # Enter a parse tree produced by TimelyParser#visualize_bool.
    def enterVisualize_bool(self, ctx:TimelyParser.Visualize_boolContext):
        pass

    # Exit a parse tree produced by TimelyParser#visualize_bool.
    def exitVisualize_bool(self, ctx:TimelyParser.Visualize_boolContext):
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


    # Enter a parse tree produced by TimelyParser#n_layers.
    def enterN_layers(self, ctx:TimelyParser.N_layersContext):
        pass

    # Exit a parse tree produced by TimelyParser#n_layers.
    def exitN_layers(self, ctx:TimelyParser.N_layersContext):
        pass


    # Enter a parse tree produced by TimelyParser#batch_size.
    def enterBatch_size(self, ctx:TimelyParser.Batch_sizeContext):
        pass

    # Exit a parse tree produced by TimelyParser#batch_size.
    def exitBatch_size(self, ctx:TimelyParser.Batch_sizeContext):
        pass


    # Enter a parse tree produced by TimelyParser#n_epochs.
    def enterN_epochs(self, ctx:TimelyParser.N_epochsContext):
        pass

    # Exit a parse tree produced by TimelyParser#n_epochs.
    def exitN_epochs(self, ctx:TimelyParser.N_epochsContext):
        pass


    # Enter a parse tree produced by TimelyParser#drop_out.
    def enterDrop_out(self, ctx:TimelyParser.Drop_outContext):
        pass

    # Exit a parse tree produced by TimelyParser#drop_out.
    def exitDrop_out(self, ctx:TimelyParser.Drop_outContext):
        pass


    # Enter a parse tree produced by TimelyParser#lstm_neurons.
    def enterLstm_neurons(self, ctx:TimelyParser.Lstm_neuronsContext):
        pass

    # Exit a parse tree produced by TimelyParser#lstm_neurons.
    def exitLstm_neurons(self, ctx:TimelyParser.Lstm_neuronsContext):
        pass


    # Enter a parse tree produced by TimelyParser#optimizer.
    def enterOptimizer(self, ctx:TimelyParser.OptimizerContext):
        pass

    # Exit a parse tree produced by TimelyParser#optimizer.
    def exitOptimizer(self, ctx:TimelyParser.OptimizerContext):
        pass


    # Enter a parse tree produced by TimelyParser#loss.
    def enterLoss(self, ctx:TimelyParser.LossContext):
        pass

    # Exit a parse tree produced by TimelyParser#loss.
    def exitLoss(self, ctx:TimelyParser.LossContext):
        pass


    # Enter a parse tree produced by TimelyParser#seq_length.
    def enterSeq_length(self, ctx:TimelyParser.Seq_lengthContext):
        pass

    # Exit a parse tree produced by TimelyParser#seq_length.
    def exitSeq_length(self, ctx:TimelyParser.Seq_lengthContext):
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