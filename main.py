import os
import sys
import time

import llvmlite.binding as llvm
from antlr4 import *
from gen.reviLangLexer import reviLangLexer
from gen.reviLangParser import reviLangParser
from codegen.ReviLangListener import CustomReviLangListener
from codegen.Optimization import Optimization
from codegen.ErrorListener import MyErrorListener


class Compiler:
    def __init__(self, input_file):
        self.input_file = FileStream(input_file)
        print(input_file)
        self.lexer = reviLangLexer(self.input_file)
        self.stream = CommonTokenStream(self.lexer)

        self.parser = reviLangParser(self.stream)
        self.parser.removeErrorListeners()
        self.errorListener = MyErrorListener()
        self.parser.addErrorListener(self.errorListener)

        self.tree = self.parser.program()

        if not self.errorListener.check:
            printer = CustomReviLangListener()
            walker = ParseTreeWalker()
            walker.walk(printer, self.tree)

            self.compile(printer)

    def compile(self, gen_module):
        module_ref = llvm.parse_assembly(str(gen_module.module))
        module_ref.verify()

        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine(codemodel="small")

        gen_module.module.triple = llvm.get_default_triple()
        gen_module.module.data_layout = target_machine.target_data

        print(module_ref)
        check = input("you want to optimize this code [Y/N]: ").lower()
        if check == "y":
            print("---Optimization is enable----")
            Optimization.__int__(self, module_ref)
            print(module_ref)
        elif check == "n":
            print("---Optimization is disable----")
        obj = target_machine.emit_object(module_ref)
        open('revi.o', 'wb').write(obj)
        print("=" * 25, "execute", "=" * 25)
        os.system(f"clang revi.o -o revi.exe")

        start_time = time.time()
        os.system("revi")
        end_time = time.time()

        print("=" * 27, "end", "=" * 27)
        print('Program Revi - Execution time:', (end_time - start_time) * 1000, 'milliseconds')

        os.system(f"clang revi_c_.c -o revi_c_.exe")

        start_time = time.time()
        os.system("revi_c_")
        end_time = time.time()

        print('Program C - Execution time:', (end_time - start_time) * 1000, 'milliseconds')
        # del compiler files
        [os.remove(trash) for trash in ["revi.o", "revi.exe"]]


if __name__ == '__main__':
    Compiler = Compiler("./tests/test.revi")
