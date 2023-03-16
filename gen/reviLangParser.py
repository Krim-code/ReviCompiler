# Generated from C:/Users/Redmi/Documents/Programming/Python/ReviCompiler/grammar\reviLang.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,3,4,66,8,4,1,4,1,4,5,4,
        70,8,4,10,4,12,4,73,9,4,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,87,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,106,8,9,10,9,12,9,109,9,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        137,8,13,10,13,12,13,140,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,5,14,152,8,14,10,14,12,14,155,9,14,1,14,1,14,3,14,
        159,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,170,8,
        14,10,14,12,14,173,9,14,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,
        1,18,3,18,184,8,18,1,18,1,18,5,18,188,8,18,10,18,12,18,191,9,18,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,3,20,201,8,20,1,21,1,21,
        1,21,0,1,28,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,0,4,1,0,15,16,1,0,12,14,2,0,21,22,26,27,1,0,7,8,206,
        0,47,1,0,0,0,2,50,1,0,0,0,4,55,1,0,0,0,6,61,1,0,0,0,8,65,1,0,0,0,
        10,77,1,0,0,0,12,86,1,0,0,0,14,88,1,0,0,0,16,94,1,0,0,0,18,98,1,
        0,0,0,20,112,1,0,0,0,22,119,1,0,0,0,24,124,1,0,0,0,26,130,1,0,0,
        0,28,158,1,0,0,0,30,174,1,0,0,0,32,178,1,0,0,0,34,180,1,0,0,0,36,
        183,1,0,0,0,38,192,1,0,0,0,40,200,1,0,0,0,42,202,1,0,0,0,44,46,3,
        2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,
        1,1,0,0,0,49,47,1,0,0,0,50,51,3,4,2,0,51,52,5,23,0,0,52,53,3,10,
        5,0,53,54,5,24,0,0,54,3,1,0,0,0,55,56,3,42,21,0,56,57,5,11,0,0,57,
        58,5,17,0,0,58,59,3,8,4,0,59,60,5,18,0,0,60,5,1,0,0,0,61,62,3,42,
        21,0,62,63,5,11,0,0,63,7,1,0,0,0,64,66,3,6,3,0,65,64,1,0,0,0,65,
        66,1,0,0,0,66,71,1,0,0,0,67,68,5,1,0,0,68,70,3,6,3,0,69,67,1,0,0,
        0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,9,1,0,0,0,73,71,1,
        0,0,0,74,76,3,12,6,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,
        78,1,0,0,0,78,11,1,0,0,0,79,77,1,0,0,0,80,87,3,14,7,0,81,87,3,16,
        8,0,82,87,3,26,13,0,83,87,3,18,9,0,84,87,3,24,12,0,85,87,3,22,11,
        0,86,80,1,0,0,0,86,81,1,0,0,0,86,82,1,0,0,0,86,83,1,0,0,0,86,84,
        1,0,0,0,86,85,1,0,0,0,87,13,1,0,0,0,88,89,3,42,21,0,89,90,5,11,0,
        0,90,91,5,20,0,0,91,92,3,28,14,0,92,93,5,25,0,0,93,15,1,0,0,0,94,
        95,5,2,0,0,95,96,3,28,14,0,96,97,5,25,0,0,97,17,1,0,0,0,98,99,5,
        9,0,0,99,100,5,17,0,0,100,101,3,30,15,0,101,102,5,18,0,0,102,107,
        5,23,0,0,103,106,3,12,6,0,104,106,3,28,14,0,105,103,1,0,0,0,105,
        104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        110,1,0,0,0,109,107,1,0,0,0,110,111,5,24,0,0,111,19,1,0,0,0,112,
        113,5,3,0,0,113,114,3,42,21,0,114,115,5,4,0,0,115,116,5,17,0,0,116,
        117,3,28,14,0,117,118,5,18,0,0,118,21,1,0,0,0,119,120,5,11,0,0,120,
        121,5,20,0,0,121,122,3,28,14,0,122,123,5,25,0,0,123,23,1,0,0,0,124,
        125,5,5,0,0,125,126,5,17,0,0,126,127,3,28,14,0,127,128,5,18,0,0,
        128,129,5,25,0,0,129,25,1,0,0,0,130,131,5,6,0,0,131,132,5,17,0,0,
        132,133,3,30,15,0,133,134,5,18,0,0,134,138,5,23,0,0,135,137,3,12,
        6,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,
        0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,142,5,24,0,0,142,27,1,0,
        0,0,143,144,6,14,-1,0,144,159,3,20,10,0,145,159,3,38,19,0,146,147,
        5,17,0,0,147,148,3,28,14,0,148,149,5,18,0,0,149,159,1,0,0,0,150,
        152,7,0,0,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,
        154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,159,3,40,20,0,157,
        159,5,10,0,0,158,143,1,0,0,0,158,145,1,0,0,0,158,146,1,0,0,0,158,
        153,1,0,0,0,158,157,1,0,0,0,159,171,1,0,0,0,160,161,10,6,0,0,161,
        162,5,19,0,0,162,170,3,28,14,7,163,164,10,5,0,0,164,165,7,1,0,0,
        165,170,3,28,14,6,166,167,10,4,0,0,167,168,7,0,0,0,168,170,3,28,
        14,5,169,160,1,0,0,0,169,163,1,0,0,0,169,166,1,0,0,0,170,173,1,0,
        0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,29,1,0,0,0,173,171,1,0,0,
        0,174,175,3,28,14,0,175,176,3,32,16,0,176,177,3,28,14,0,177,31,1,
        0,0,0,178,179,7,2,0,0,179,33,1,0,0,0,180,181,3,28,14,0,181,35,1,
        0,0,0,182,184,3,34,17,0,183,182,1,0,0,0,183,184,1,0,0,0,184,189,
        1,0,0,0,185,186,5,1,0,0,186,188,3,34,17,0,187,185,1,0,0,0,188,191,
        1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,37,1,0,0,0,191,189,1,
        0,0,0,192,193,5,11,0,0,193,194,5,17,0,0,194,195,3,36,18,0,195,196,
        5,18,0,0,196,39,1,0,0,0,197,201,5,28,0,0,198,201,5,29,0,0,199,201,
        5,11,0,0,200,197,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,41,
        1,0,0,0,202,203,7,3,0,0,203,43,1,0,0,0,15,47,65,71,77,86,105,107,
        138,153,158,169,171,183,189,200
    ]

class reviLangParser ( Parser ):

    grammarFileName = "reviLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'return'", "'<<'", "'>>'", "'print'", 
                     "'if'", "'int'", "'double'", "'while'", "<INVALID>", 
                     "<INVALID>", "'*'", "'%'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'^'", "'='", "'=='", "'!='", "'{'", "'}'", 
                     "';'", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WHILE", "STRING", "ID", "TIMES", "REM", 
                      "DIV", "PLUS", "MINUS", "LPAREN", "RPAREN", "POW", 
                      "EQ", "EQ_EQ", "NOT_EQ", "LBRACE", "RBRACE", "END_STATE", 
                      "GT", "LT", "INT", "DECIMAL", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_functionHead = 2
    RULE_arg = 3
    RULE_arguments = 4
    RULE_functionBody = 5
    RULE_statement = 6
    RULE_assignmentStatement = 7
    RULE_returnStatement = 8
    RULE_whileStatement = 9
    RULE_convert_type = 10
    RULE_moveValueVariable = 11
    RULE_printStatement = 12
    RULE_ifStatement = 13
    RULE_expression = 14
    RULE_equation = 15
    RULE_relop = 16
    RULE_param = 17
    RULE_params = 18
    RULE_functionCall = 19
    RULE_atom = 20
    RULE_type = 21

    ruleNames =  [ "program", "function", "functionHead", "arg", "arguments", 
                   "functionBody", "statement", "assignmentStatement", "returnStatement", 
                   "whileStatement", "convert_type", "moveValueVariable", 
                   "printStatement", "ifStatement", "expression", "equation", 
                   "relop", "param", "params", "functionCall", "atom", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    WHILE=9
    STRING=10
    ID=11
    TIMES=12
    REM=13
    DIV=14
    PLUS=15
    MINUS=16
    LPAREN=17
    RPAREN=18
    POW=19
    EQ=20
    EQ_EQ=21
    NOT_EQ=22
    LBRACE=23
    RBRACE=24
    END_STATE=25
    GT=26
    LT=27
    INT=28
    DECIMAL=29
    WS=30
    COMMENT=31
    LINE_COMMENT=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.FunctionContext)
            else:
                return self.getTypedRuleContext(reviLangParser.FunctionContext,i)


        def getRuleIndex(self):
            return reviLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = reviLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 44
                self.function()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionHead(self):
            return self.getTypedRuleContext(reviLangParser.FunctionHeadContext,0)


        def LBRACE(self):
            return self.getToken(reviLangParser.LBRACE, 0)

        def functionBody(self):
            return self.getTypedRuleContext(reviLangParser.FunctionBodyContext,0)


        def RBRACE(self):
            return self.getToken(reviLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = reviLangParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.functionHead()
            self.state = 51
            self.match(reviLangParser.LBRACE)
            self.state = 52
            self.functionBody()
            self.state = 53
            self.match(reviLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionHeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(reviLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(reviLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(reviLangParser.ArgumentsContext,0)


        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_functionHead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionHead" ):
                listener.enterFunctionHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionHead" ):
                listener.exitFunctionHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionHead" ):
                return visitor.visitFunctionHead(self)
            else:
                return visitor.visitChildren(self)




    def functionHead(self):

        localctx = reviLangParser.FunctionHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionHead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.type_()
            self.state = 56
            self.match(reviLangParser.ID)
            self.state = 57
            self.match(reviLangParser.LPAREN)
            self.state = 58
            self.arguments()
            self.state = 59
            self.match(reviLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(reviLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(reviLangParser.ID, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = reviLangParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.type_()
            self.state = 62
            self.match(reviLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ArgContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ArgContext,i)


        def getRuleIndex(self):
            return reviLangParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = reviLangParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 64
                self.arg()


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 67
                self.match(reviLangParser.T__0)
                self.state = 68
                self.arg()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(reviLangParser.StatementContext,i)


        def getRuleIndex(self):
            return reviLangParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = reviLangParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3044) != 0:
                self.state = 74
                self.statement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(reviLangParser.AssignmentStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(reviLangParser.ReturnStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(reviLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(reviLangParser.WhileStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(reviLangParser.PrintStatementContext,0)


        def moveValueVariable(self):
            return self.getTypedRuleContext(reviLangParser.MoveValueVariableContext,0)


        def getRuleIndex(self):
            return reviLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = reviLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.assignmentStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.returnStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.ifStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.whileStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.printStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.moveValueVariable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(reviLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(reviLangParser.ID, 0)

        def EQ(self):
            return self.getToken(reviLangParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)


        def END_STATE(self):
            return self.getToken(reviLangParser.END_STATE, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = reviLangParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.type_()
            self.state = 89
            self.match(reviLangParser.ID)
            self.state = 90
            self.match(reviLangParser.EQ)
            self.state = 91
            self.expression(0)
            self.state = 92
            self.match(reviLangParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)


        def END_STATE(self):
            return self.getToken(reviLangParser.END_STATE, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = reviLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(reviLangParser.T__1)
            self.state = 95
            self.expression(0)
            self.state = 96
            self.match(reviLangParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(reviLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)

        def equation(self):
            return self.getTypedRuleContext(reviLangParser.EquationContext,0)


        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(reviLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(reviLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(reviLangParser.StatementContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return reviLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = reviLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(reviLangParser.WHILE)
            self.state = 99
            self.match(reviLangParser.LPAREN)
            self.state = 100
            self.equation()
            self.state = 101
            self.match(reviLangParser.RPAREN)
            self.state = 102
            self.match(reviLangParser.LBRACE)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 805539820) != 0:
                self.state = 105
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 104
                    self.expression(0)
                    pass


                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(reviLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Convert_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(reviLangParser.TypeContext,0)


        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_convert_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConvert_type" ):
                listener.enterConvert_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConvert_type" ):
                listener.exitConvert_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConvert_type" ):
                return visitor.visitConvert_type(self)
            else:
                return visitor.visitChildren(self)




    def convert_type(self):

        localctx = reviLangParser.Convert_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_convert_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(reviLangParser.T__2)
            self.state = 113
            self.type_()
            self.state = 114
            self.match(reviLangParser.T__3)
            self.state = 115
            self.match(reviLangParser.LPAREN)
            self.state = 116
            self.expression(0)
            self.state = 117
            self.match(reviLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveValueVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(reviLangParser.ID, 0)

        def EQ(self):
            return self.getToken(reviLangParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)


        def END_STATE(self):
            return self.getToken(reviLangParser.END_STATE, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_moveValueVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveValueVariable" ):
                listener.enterMoveValueVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveValueVariable" ):
                listener.exitMoveValueVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveValueVariable" ):
                return visitor.visitMoveValueVariable(self)
            else:
                return visitor.visitChildren(self)




    def moveValueVariable(self):

        localctx = reviLangParser.MoveValueVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_moveValueVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(reviLangParser.ID)
            self.state = 120
            self.match(reviLangParser.EQ)
            self.state = 121
            self.expression(0)
            self.state = 122
            self.match(reviLangParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def END_STATE(self):
            return self.getToken(reviLangParser.END_STATE, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = reviLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(reviLangParser.T__4)
            self.state = 125
            self.match(reviLangParser.LPAREN)
            self.state = 126
            self.expression(0)
            self.state = 127
            self.match(reviLangParser.RPAREN)
            self.state = 128
            self.match(reviLangParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)

        def equation(self):
            return self.getTypedRuleContext(reviLangParser.EquationContext,0)


        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(reviLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(reviLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(reviLangParser.StatementContext,i)


        def getRuleIndex(self):
            return reviLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = reviLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(reviLangParser.T__5)
            self.state = 131
            self.match(reviLangParser.LPAREN)
            self.state = 132
            self.equation()
            self.state = 133
            self.match(reviLangParser.RPAREN)
            self.state = 134
            self.match(reviLangParser.LBRACE)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3044) != 0:
                self.state = 135
                self.statement()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(reviLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return reviLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionAddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(reviLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(reviLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAdd" ):
                listener.enterExpressionAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAdd" ):
                listener.exitExpressionAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAdd" ):
                return visitor.visitExpressionAdd(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionMulContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ExpressionContext,i)

        def TIMES(self):
            return self.getToken(reviLangParser.TIMES, 0)
        def DIV(self):
            return self.getToken(reviLangParser.DIV, 0)
        def REM(self):
            return self.getToken(reviLangParser.REM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionMul" ):
                listener.enterExpressionMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionMul" ):
                listener.exitExpressionMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionMul" ):
                return visitor.visitExpressionMul(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionNumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(reviLangParser.AtomContext,0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(reviLangParser.PLUS)
            else:
                return self.getToken(reviLangParser.PLUS, i)
        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(reviLangParser.MINUS)
            else:
                return self.getToken(reviLangParser.MINUS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionNumber" ):
                listener.enterExpressionNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionNumber" ):
                listener.exitExpressionNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionNumber" ):
                return visitor.visitExpressionNumber(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionFunctionCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(reviLangParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionFunctionCall" ):
                listener.enterExpressionFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionFunctionCall" ):
                listener.exitExpressionFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionFunctionCall" ):
                return visitor.visitExpressionFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionNestedContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionNested" ):
                listener.enterExpressionNested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionNested" ):
                listener.exitExpressionNested(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionNested" ):
                return visitor.visitExpressionNested(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionToTypeContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def convert_type(self):
            return self.getTypedRuleContext(reviLangParser.Convert_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionToType" ):
                listener.enterExpressionToType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionToType" ):
                listener.exitExpressionToType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionToType" ):
                return visitor.visitExpressionToType(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionPowContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ExpressionContext,i)

        def POW(self):
            return self.getToken(reviLangParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionPow" ):
                listener.enterExpressionPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionPow" ):
                listener.exitExpressionPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionPow" ):
                return visitor.visitExpressionPow(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStringContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a reviLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(reviLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionString" ):
                listener.enterExpressionString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionString" ):
                listener.exitExpressionString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionString" ):
                return visitor.visitExpressionString(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = reviLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = reviLangParser.ExpressionToTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 144
                self.convert_type()
                pass

            elif la_ == 2:
                localctx = reviLangParser.ExpressionFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = reviLangParser.ExpressionNestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(reviLangParser.LPAREN)
                self.state = 147
                self.expression(0)
                self.state = 148
                self.match(reviLangParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = reviLangParser.ExpressionNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 150
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 156
                self.atom()
                pass

            elif la_ == 5:
                localctx = reviLangParser.ExpressionStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(reviLangParser.STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 169
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = reviLangParser.ExpressionPowContext(self, reviLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 161
                        localctx.op = self.match(reviLangParser.POW)
                        self.state = 162
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = reviLangParser.ExpressionMulContext(self, reviLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 164
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 165
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = reviLangParser.ExpressionAddContext(self, reviLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 167
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.expression(5)
                        pass

             
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # RelopContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(reviLangParser.RelopContext,0)


        def getRuleIndex(self):
            return reviLangParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = reviLangParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expression(0)
            self.state = 175
            localctx.op = self.relop()
            self.state = 176
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_EQ(self):
            return self.getToken(reviLangParser.EQ_EQ, 0)

        def GT(self):
            return self.getToken(reviLangParser.GT, 0)

        def LT(self):
            return self.getToken(reviLangParser.LT, 0)

        def NOT_EQ(self):
            return self.getToken(reviLangParser.NOT_EQ, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = reviLangParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 207618048) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(reviLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return reviLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = reviLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reviLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(reviLangParser.ParamContext,i)


        def getRuleIndex(self):
            return reviLangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = reviLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 805538824) != 0:
                self.state = 182
                self.param()


            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 185
                self.match(reviLangParser.T__0)
                self.state = 186
                self.param()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(reviLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(reviLangParser.LPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(reviLangParser.ParamsContext,0)


        def RPAREN(self):
            return self.getToken(reviLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = reviLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(reviLangParser.ID)
            self.state = 193
            self.match(reviLangParser.LPAREN)
            self.state = 194
            self.params()
            self.state = 195
            self.match(reviLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def INT(self):
            return self.getToken(reviLangParser.INT, 0)

        def DECIMAL(self):
            return self.getToken(reviLangParser.DECIMAL, 0)

        def ID(self):
            return self.getToken(reviLangParser.ID, 0)

        def getRuleIndex(self):
            return reviLangParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = reviLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atom)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                localctx.op = self.match(reviLangParser.INT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                localctx.op = self.match(reviLangParser.DECIMAL)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                localctx.op = self.match(reviLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return reviLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = reviLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




