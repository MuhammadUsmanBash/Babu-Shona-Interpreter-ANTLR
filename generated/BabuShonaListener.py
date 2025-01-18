# Generated from BabuShona.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BabuShonaParser import BabuShonaParser
else:
    from BabuShonaParser import BabuShonaParser

# This class defines a complete listener for a parse tree produced by BabuShonaParser.
class BabuShonaListener(ParseTreeListener):

    # Enter a parse tree produced by BabuShonaParser#script.
    def enterScript(self, ctx:BabuShonaParser.ScriptContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#script.
    def exitScript(self, ctx:BabuShonaParser.ScriptContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#statement.
    def enterStatement(self, ctx:BabuShonaParser.StatementContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#statement.
    def exitStatement(self, ctx:BabuShonaParser.StatementContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#ifStmt.
    def enterIfStmt(self, ctx:BabuShonaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#ifStmt.
    def exitIfStmt(self, ctx:BabuShonaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#elseIfStmt.
    def enterElseIfStmt(self, ctx:BabuShonaParser.ElseIfStmtContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#elseIfStmt.
    def exitElseIfStmt(self, ctx:BabuShonaParser.ElseIfStmtContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#elseStmt.
    def enterElseStmt(self, ctx:BabuShonaParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#elseStmt.
    def exitElseStmt(self, ctx:BabuShonaParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#printStmt.
    def enterPrintStmt(self, ctx:BabuShonaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#printStmt.
    def exitPrintStmt(self, ctx:BabuShonaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#inputStmt.
    def enterInputStmt(self, ctx:BabuShonaParser.InputStmtContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#inputStmt.
    def exitInputStmt(self, ctx:BabuShonaParser.InputStmtContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#varDecl.
    def enterVarDecl(self, ctx:BabuShonaParser.VarDeclContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#varDecl.
    def exitVarDecl(self, ctx:BabuShonaParser.VarDeclContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#forLoopStmt.
    def enterForLoopStmt(self, ctx:BabuShonaParser.ForLoopStmtContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#forLoopStmt.
    def exitForLoopStmt(self, ctx:BabuShonaParser.ForLoopStmtContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#block.
    def enterBlock(self, ctx:BabuShonaParser.BlockContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#block.
    def exitBlock(self, ctx:BabuShonaParser.BlockContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#stringExpr.
    def enterStringExpr(self, ctx:BabuShonaParser.StringExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#stringExpr.
    def exitStringExpr(self, ctx:BabuShonaParser.StringExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#variableExpr.
    def enterVariableExpr(self, ctx:BabuShonaParser.VariableExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#variableExpr.
    def exitVariableExpr(self, ctx:BabuShonaParser.VariableExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#notExpr.
    def enterNotExpr(self, ctx:BabuShonaParser.NotExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#notExpr.
    def exitNotExpr(self, ctx:BabuShonaParser.NotExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#intExpr.
    def enterIntExpr(self, ctx:BabuShonaParser.IntExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#intExpr.
    def exitIntExpr(self, ctx:BabuShonaParser.IntExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#booleanExpr.
    def enterBooleanExpr(self, ctx:BabuShonaParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#booleanExpr.
    def exitBooleanExpr(self, ctx:BabuShonaParser.BooleanExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#logicalExpr.
    def enterLogicalExpr(self, ctx:BabuShonaParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#logicalExpr.
    def exitLogicalExpr(self, ctx:BabuShonaParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:BabuShonaParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:BabuShonaParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:BabuShonaParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:BabuShonaParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by BabuShonaParser#parenthesesExpr.
    def enterParenthesesExpr(self, ctx:BabuShonaParser.ParenthesesExprContext):
        pass

    # Exit a parse tree produced by BabuShonaParser#parenthesesExpr.
    def exitParenthesesExpr(self, ctx:BabuShonaParser.ParenthesesExprContext):
        pass



del BabuShonaParser