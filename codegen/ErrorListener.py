import sys

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import RecognitionException


class MyErrorListener(ErrorListener):
    def __init__(self):
        self.check = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
        print("Syntax error at line", line, "column", column, ":", message)
        self.check = True
        # raise CustomRecognitionException("Token recognition error", recognizer, offendingSymbol, line, column, e)


class CustomRecognitionException(RecognitionException):
    def __init__(self, message, recognizer, offendingSymbol, line, column, e):
        super().__init__(message, recognizer, offendingSymbol, e)
        self.line = line
        self.column = column
        print(e.getMessage(), "at line", e.line, "column", e.column)

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     print("Ambiguity at index", startIndex)
    #     sys.exit("aa! errors!")
    #
    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     print("Attempting full context at index", startIndex)
    #     sys.exit("aa! errors!")
    #
    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     print("Context sensitivity at index", startIndex)
    #     sys.exit("aa! errors!")
