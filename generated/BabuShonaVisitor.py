# Generated from BabuShona.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BabuShonaParser import BabuShonaParser
else:
    from BabuShonaParser import BabuShonaParser

# This class defines a complete generic visitor for a parse tree produced by BabuShonaParser.

class BabuShonaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BabuShonaParser#script.
    def visitScript(self, ctx:BabuShonaParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#statement.
    def visitStatement(self, ctx:BabuShonaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#ifStmt.
    def visitIfStmt(self, ctx:BabuShonaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#elseIfStmt.
    def visitElseIfStmt(self, ctx:BabuShonaParser.ElseIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#elseStmt.
    def visitElseStmt(self, ctx:BabuShonaParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#printStmt.
    def visitPrintStmt(self, ctx:BabuShonaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#inputStmt.
    def visitInputStmt(self, ctx:BabuShonaParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#varDecl.
    def visitVarDecl(self, ctx:BabuShonaParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#forLoopStmt.
    def visitForLoopStmt(self, ctx:BabuShonaParser.ForLoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#block.
    def visitBlock(self, ctx:BabuShonaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#stringExpr.
    def visitStringExpr(self, ctx:BabuShonaParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#variableExpr.
    def visitVariableExpr(self, ctx:BabuShonaParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#notExpr.
    def visitNotExpr(self, ctx:BabuShonaParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#intExpr.
    def visitIntExpr(self, ctx:BabuShonaParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#booleanExpr.
    def visitBooleanExpr(self, ctx:BabuShonaParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#logicalExpr.
    def visitLogicalExpr(self, ctx:BabuShonaParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:BabuShonaParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:BabuShonaParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabuShonaParser#parenthesesExpr.
    def visitParenthesesExpr(self, ctx:BabuShonaParser.ParenthesesExprContext):
        return self.visitChildren(ctx)



del BabuShonaParser