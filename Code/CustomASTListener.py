from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.TimelyListener import TimelyListener


class CustomASTListener(TimelyListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['dataframeLoadStatement', 'tickerLoadStatement', 'acfStatement', 'pacfStatement', 'testStatement', 'modelStatement', 'program']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx):
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)

    def exitDataframeLoadStatement(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "dataframeLoadStatement", keep_node=True)

    def exitTickerLoadStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "tickerLoadStatement", keep_node=True)

    def exitAcfStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "acfStatement", keep_node=True)

    def exitPacfStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "pacfStatement", keep_node=True)

    def exitTestStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "testStatement", keep_node=True)

    def exitModelStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "modelStatement", keep_node=True)