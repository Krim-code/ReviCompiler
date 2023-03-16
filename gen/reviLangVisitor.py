# Generated from C:/Users/Redmi/Documents/Programming/Python/ReviCompiler/grammar\reviLang.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .reviLangParser import reviLangParser
else:
    from reviLangParser import reviLangParser

# This class defines a complete generic visitor for a parse tree produced by reviLangParser.

class reviLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by reviLangParser#program.
    def visitProgram(self, ctx:reviLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#function.
    def visitFunction(self, ctx:reviLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#functionHead.
    def visitFunctionHead(self, ctx:reviLangParser.FunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#arg.
    def visitArg(self, ctx:reviLangParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#arguments.
    def visitArguments(self, ctx:reviLangParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#functionBody.
    def visitFunctionBody(self, ctx:reviLangParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#statement.
    def visitStatement(self, ctx:reviLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:reviLangParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#returnStatement.
    def visitReturnStatement(self, ctx:reviLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#whileStatement.
    def visitWhileStatement(self, ctx:reviLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#convert_type.
    def visitConvert_type(self, ctx:reviLangParser.Convert_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#moveValueVariable.
    def visitMoveValueVariable(self, ctx:reviLangParser.MoveValueVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#printStatement.
    def visitPrintStatement(self, ctx:reviLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#ifStatement.
    def visitIfStatement(self, ctx:reviLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionAdd.
    def visitExpressionAdd(self, ctx:reviLangParser.ExpressionAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionMul.
    def visitExpressionMul(self, ctx:reviLangParser.ExpressionMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionNumber.
    def visitExpressionNumber(self, ctx:reviLangParser.ExpressionNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionFunctionCall.
    def visitExpressionFunctionCall(self, ctx:reviLangParser.ExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionNested.
    def visitExpressionNested(self, ctx:reviLangParser.ExpressionNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionToType.
    def visitExpressionToType(self, ctx:reviLangParser.ExpressionToTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionPow.
    def visitExpressionPow(self, ctx:reviLangParser.ExpressionPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#expressionString.
    def visitExpressionString(self, ctx:reviLangParser.ExpressionStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#equation.
    def visitEquation(self, ctx:reviLangParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#relop.
    def visitRelop(self, ctx:reviLangParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#param.
    def visitParam(self, ctx:reviLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#params.
    def visitParams(self, ctx:reviLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#functionCall.
    def visitFunctionCall(self, ctx:reviLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#atom.
    def visitAtom(self, ctx:reviLangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reviLangParser#type.
    def visitType(self, ctx:reviLangParser.TypeContext):
        return self.visitChildren(ctx)



del reviLangParser