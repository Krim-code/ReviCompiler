from llvmlite import ir
from gen.reviLangParser import reviLangParser
from codegen.AST import MainAST


class CoolFunc:

    @staticmethod
    def get_type(my_type: reviLangParser.TypeContext):
        value = my_type.getText()

        if value == "int":
            return ir.IntType(32)
        elif value == "double":
            return ir.DoubleType()
        else:
            raise Exception("Unknown type: " + value)

    @staticmethod
    def check_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
