# Generated from C:/Users/Redmi/Documents/Programming/Python/ReviCompiler/grammar\reviLang.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .reviLangParser import reviLangParser
else:
    from reviLangParser import reviLangParser

# This class defines a complete listener for a parse tree produced by reviLangParser.
class reviLangListener(ParseTreeListener):

    # Enter a parse tree produced by reviLangParser#program.
    def enterProgram(self, ctx:reviLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by reviLangParser#program.
    def exitProgram(self, ctx:reviLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by reviLangParser#function.
    def enterFunction(self, ctx:reviLangParser.FunctionContext):
        pass

    # Exit a parse tree produced by reviLangParser#function.
    def exitFunction(self, ctx:reviLangParser.FunctionContext):
        pass


    # Enter a parse tree produced by reviLangParser#functionHead.
    def enterFunctionHead(self, ctx:reviLangParser.FunctionHeadContext):
        pass

    # Exit a parse tree produced by reviLangParser#functionHead.
    def exitFunctionHead(self, ctx:reviLangParser.FunctionHeadContext):
        pass


    # Enter a parse tree produced by reviLangParser#arg.
    def enterArg(self, ctx:reviLangParser.ArgContext):
        pass

    # Exit a parse tree produced by reviLangParser#arg.
    def exitArg(self, ctx:reviLangParser.ArgContext):
        pass


    # Enter a parse tree produced by reviLangParser#arguments.
    def enterArguments(self, ctx:reviLangParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by reviLangParser#arguments.
    def exitArguments(self, ctx:reviLangParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by reviLangParser#functionBody.
    def enterFunctionBody(self, ctx:reviLangParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by reviLangParser#functionBody.
    def exitFunctionBody(self, ctx:reviLangParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by reviLangParser#statement.
    def enterStatement(self, ctx:reviLangParser.StatementContext):
        pass

    # Exit a parse tree produced by reviLangParser#statement.
    def exitStatement(self, ctx:reviLangParser.StatementContext):
        pass


    # Enter a parse tree produced by reviLangParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:reviLangParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by reviLangParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:reviLangParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by reviLangParser#returnStatement.
    def enterReturnStatement(self, ctx:reviLangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by reviLangParser#returnStatement.
    def exitReturnStatement(self, ctx:reviLangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by reviLangParser#whileStatement.
    def enterWhileStatement(self, ctx:reviLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by reviLangParser#whileStatement.
    def exitWhileStatement(self, ctx:reviLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by reviLangParser#convert_type.
    def enterConvert_type(self, ctx:reviLangParser.Convert_typeContext):
        pass

    # Exit a parse tree produced by reviLangParser#convert_type.
    def exitConvert_type(self, ctx:reviLangParser.Convert_typeContext):
        pass


    # Enter a parse tree produced by reviLangParser#moveValueVariable.
    def enterMoveValueVariable(self, ctx:reviLangParser.MoveValueVariableContext):
        pass

    # Exit a parse tree produced by reviLangParser#moveValueVariable.
    def exitMoveValueVariable(self, ctx:reviLangParser.MoveValueVariableContext):
        pass


    # Enter a parse tree produced by reviLangParser#printStatement.
    def enterPrintStatement(self, ctx:reviLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by reviLangParser#printStatement.
    def exitPrintStatement(self, ctx:reviLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by reviLangParser#ifStatement.
    def enterIfStatement(self, ctx:reviLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by reviLangParser#ifStatement.
    def exitIfStatement(self, ctx:reviLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionAdd.
    def enterExpressionAdd(self, ctx:reviLangParser.ExpressionAddContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionAdd.
    def exitExpressionAdd(self, ctx:reviLangParser.ExpressionAddContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionMul.
    def enterExpressionMul(self, ctx:reviLangParser.ExpressionMulContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionMul.
    def exitExpressionMul(self, ctx:reviLangParser.ExpressionMulContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionNumber.
    def enterExpressionNumber(self, ctx:reviLangParser.ExpressionNumberContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionNumber.
    def exitExpressionNumber(self, ctx:reviLangParser.ExpressionNumberContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionFunctionCall.
    def enterExpressionFunctionCall(self, ctx:reviLangParser.ExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionFunctionCall.
    def exitExpressionFunctionCall(self, ctx:reviLangParser.ExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionNested.
    def enterExpressionNested(self, ctx:reviLangParser.ExpressionNestedContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionNested.
    def exitExpressionNested(self, ctx:reviLangParser.ExpressionNestedContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionToType.
    def enterExpressionToType(self, ctx:reviLangParser.ExpressionToTypeContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionToType.
    def exitExpressionToType(self, ctx:reviLangParser.ExpressionToTypeContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionPow.
    def enterExpressionPow(self, ctx:reviLangParser.ExpressionPowContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionPow.
    def exitExpressionPow(self, ctx:reviLangParser.ExpressionPowContext):
        pass


    # Enter a parse tree produced by reviLangParser#expressionString.
    def enterExpressionString(self, ctx:reviLangParser.ExpressionStringContext):
        pass

    # Exit a parse tree produced by reviLangParser#expressionString.
    def exitExpressionString(self, ctx:reviLangParser.ExpressionStringContext):
        pass


    # Enter a parse tree produced by reviLangParser#equation.
    def enterEquation(self, ctx:reviLangParser.EquationContext):
        pass

    # Exit a parse tree produced by reviLangParser#equation.
    def exitEquation(self, ctx:reviLangParser.EquationContext):
        pass


    # Enter a parse tree produced by reviLangParser#relop.
    def enterRelop(self, ctx:reviLangParser.RelopContext):
        pass

    # Exit a parse tree produced by reviLangParser#relop.
    def exitRelop(self, ctx:reviLangParser.RelopContext):
        pass


    # Enter a parse tree produced by reviLangParser#param.
    def enterParam(self, ctx:reviLangParser.ParamContext):
        pass

    # Exit a parse tree produced by reviLangParser#param.
    def exitParam(self, ctx:reviLangParser.ParamContext):
        pass


    # Enter a parse tree produced by reviLangParser#params.
    def enterParams(self, ctx:reviLangParser.ParamsContext):
        pass

    # Exit a parse tree produced by reviLangParser#params.
    def exitParams(self, ctx:reviLangParser.ParamsContext):
        pass


    # Enter a parse tree produced by reviLangParser#functionCall.
    def enterFunctionCall(self, ctx:reviLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by reviLangParser#functionCall.
    def exitFunctionCall(self, ctx:reviLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by reviLangParser#atom.
    def enterAtom(self, ctx:reviLangParser.AtomContext):
        pass

    # Exit a parse tree produced by reviLangParser#atom.
    def exitAtom(self, ctx:reviLangParser.AtomContext):
        pass


    # Enter a parse tree produced by reviLangParser#type.
    def enterType(self, ctx:reviLangParser.TypeContext):
        pass

    # Exit a parse tree produced by reviLangParser#type.
    def exitType(self, ctx:reviLangParser.TypeContext):
        pass



del reviLangParser