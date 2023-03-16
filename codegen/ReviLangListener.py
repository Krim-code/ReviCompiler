from random import randint

import llvmlite.binding as llvm
from antlr4 import ParseTreeWalker
from llvmlite import ir
from llvmlite.ir import Argument
from codegen.AST import MainAST
from codegen.AST import FunctionAST
from stuf.cool_functions import CoolFunc
from gen.reviLangLexer import reviLangLexer
from gen.reviLangListener import reviLangListener
from gen.reviLangParser import reviLangParser

print_function = None


class CustomReviLangListener(reviLangListener):
    stack = []

    def __init__(self):
        self.module = ir.Module()
        self.AST = MainAST()

    def load_library(self):
        pass

    def enterFunction(self, ctx: reviLangParser.FunctionContext):
        listener = FunctionListener(self.module, self.AST)
        walker = ParseTreeWalker()
        walker.walk(listener, ctx)


class FunctionListener(reviLangListener):
    def __init__(self, module, main_ast):
        self.module = module
        self.MainAST = main_ast
        self.functions = None
        self.AST = None
        self.builder = None

    def enterFunctionHead(self, ctx: reviLangParser.FunctionHeadContext):
        return_type = CoolFunc.get_type(ctx.type_())
        args_type = [CoolFunc.get_type(arg.type_()) for arg in ctx.arguments().arg()]
        func_name = ctx.ID().symbol.text
        func_type = ir.FunctionType(return_type, tuple(args_type))

        self.create_function(func_name, func_type)
        args = [state.ID().getText() for state in ctx.arguments().arg()]
        for i, arg in enumerate(self.functions.args):
            self.AST.add_variable(args[i], arg)

    def create_function(self, func_name, func_type):
        self.functions = ir.Function(self.module, func_type, func_name)
        block = self.functions.append_basic_block("entry")
        self.builder = ir.IRBuilder(block)
        self.AST = FunctionAST(func_name, self.MainAST, self.functions)

    def enterFunctionBody(self, ctx: reviLangParser.FunctionBodyContext):
        listener = FunctionBodyListener(self.builder, self.AST, self.module)
        walker = ParseTreeWalker()
        walker.walk(listener, ctx)


class FunctionBodyListener(reviLangListener):
    def __init__(self, builder: ir.IRBuilder, AST: FunctionAST, module: ir.Module):
        self.builder = builder
        self.AST = AST
        self.module = module

    def enterFunctionBody(self, ctx: reviLangParser.FunctionBodyContext):
        for stmt in ctx.children:
            listener = StatementListener(self.builder, self.AST, self.module)
            walker = ParseTreeWalker()
            walker.walk(listener, stmt)


class StatementListener(reviLangListener):
    def __init__(self, builder: ir.IRBuilder, AST: FunctionAST, module: ir.Module):
        self.builder = builder
        self.AST = AST
        self.module = module
        self.condition = None
        self.print_function = None

    def enterReturnStatement(self, ctx: reviLangParser.ReturnStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx)

        if self.condition is not None:
            with self.builder.if_then(self.condition):
                self.builder.ret(listener.stack.pop())
        else:
            self.builder.ret(listener.stack.pop())

    def enterAssignmentStatement(self, ctx: reviLangParser.AssignmentStatementContext):
        type_variable = CoolFunc.get_type(ctx.type_())
        name = ctx.ID().getText()
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx)
        value = listener.stack.pop()

        pointer = self.builder.alloca(type_variable, 1, name)
        self.builder.store(value, pointer)
        self.AST.add_variable(name, pointer)

    def enterMoveValueVariable(self, ctx: reviLangParser.MoveValueVariableContext):
        name = ctx.ID().getText()
        if self.condition is not None:
            with self.builder.if_then(self.condition):
                walker = ParseTreeWalker()
                listener = ExpressionListener(self.builder, self.AST)
                walker.walk(listener, ctx)
                value = listener.stack.pop()
                pointer = self.AST.get_variable(name)
                self.builder.store(value, pointer)
                self.AST.add_variable(name, pointer)
        else:
            walker = ParseTreeWalker()
            listener = ExpressionListener(self.builder, self.AST)
            walker.walk(listener, ctx)
            value = listener.stack.pop()
            pointer = self.AST.get_variable(name)
            self.builder.store(value, pointer)
            self.AST.add_variable(name, pointer)

    def enterIfStatement(self, ctx: reviLangParser.IfStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx.equation().expression(0))
        left = listener.stack.pop()


        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx.equation().expression(1))
        right = listener.stack.pop()


        operator = ctx.equation().op.getText()

        self.condition = self.builder.icmp_signed(cmpop=operator, lhs=left, rhs=right)

    def exitIfStatement(self, ctx: reviLangParser.IfStatementContext):
        self.cAst = self.AST
        # self.AST = None

    def enterWhileStatement(self, ctx: reviLangParser.WhileStatementContext):
        self.w_body_block = self.builder.append_basic_block("w_body")
        self.w_after_block = self.builder.append_basic_block("w_after")

        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx.equation().expression(0))
        left = listener.stack.pop()
        print(left)

        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx.equation().expression(1))
        right = listener.stack.pop()
        print(right)

        operator = ctx.equation().op.getText()

        cond_head = self.builder.icmp_signed(cmpop=operator, lhs=left, rhs=right)
        self.builder.cbranch(cond_head, self.w_body_block, self.w_after_block)
        self.builder.position_at_start(self.w_body_block)

    def exitWhileStatement(self, ctx: reviLangParser.WhileStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx.equation().expression(0))
        left = listener.stack.pop()


        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.AST)
        walker.walk(listener, ctx.equation().expression(1))
        right = listener.stack.pop()

        operator = ctx.equation().op.getText()
        cond_body = self.builder.icmp_signed(cmpop=operator, lhs=left, rhs=right)
        self.builder.cbranch(cond_body, self.w_body_block, self.w_after_block)
        self.builder.position_at_start(self.w_after_block)

    def create_print_function(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")
        return printf

    def enterPrintStatement(self, ctx: reviLangParser.PrintStatementContext):
        check = None
        var = ctx.expression().getText()
        if str(var).isnumeric() or CoolFunc.check_float(str(var)):
            walker = ParseTreeWalker()
            listener = ExpressionListener(self.builder, self.AST)
            walker.walk(listener, ctx)
            value = listener.stack.pop()
            pointer = self.builder.alloca(value.type, 1, f"temp{randint(0, 1000000)}")
            self.builder.store(value, pointer)
            value = pointer
        elif str(var)[0] == '"':
            arg = f'{str(var)[1:-1]}\0'
            c_str_val = ir.Constant(ir.ArrayType(ir.IntType(8), len(arg)),
                                    bytearray(arg.encode("utf-8")))
            c_str = self.builder.alloca(c_str_val.type)
            self.builder.store(c_str_val, c_str)
            value = c_str
            check = True
        else:
            try:
                value = self.AST.get_variable(str(var))
                print(value)
            except:
                raise Exception("Variable not found")

        global print_function
        if print_function is None:
            print_function = self.create_print_function()

        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        if isinstance(value.type.pointee, ir.DoubleType):
            fmt = "%f \n\0"
        if check:
            fmt = "%s \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf-8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr" + str(randint(0, 100000)))
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        if self.condition is not None:
            with self.builder.if_then(self.condition):
                fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
                if check:
                    self.builder.call(print_function, [fmt_arg, value])
                else:
                    self.builder.call(print_function, [fmt_arg, self.builder.load(value)])
        else:
            fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
            if check:
                self.builder.call(print_function, [fmt_arg, value])
            else:
                self.builder.call(print_function, [fmt_arg, self.builder.load(value)])


class ExpressionListener(reviLangListener):
    stack = []

    def __init__(self, builder: ir.IRBuilder, AST: FunctionAST):
        self.builder = builder
        self.AST = AST

    def exitExpressionFunctionCall(self, ctx: reviLangParser.ExpressionFunctionCallContext):
        main_ast = self.AST.main_ast
        call_function_name = main_ast.get_function(ctx.functionCall().ID().getText())
        call_function = call_function_name.function

        params = []

        for param in ctx.functionCall().params().param():
            params.append(self.stack.pop())
        params.reverse()

        self.stack.append(self.builder.call(call_function, params))

    def exitExpressionAdd(self, ctx: reviLangParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if isinstance(left.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
            add_function = self.builder.fadd
            sub_function = self.builder.fsub

            double_type = ir.DoubleType()
            left = self.builder.sitofp(left, double_type)
            right = self.builder.sitofp(right, double_type)

        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
            add_function = self.builder.add
            sub_function = self.builder.sub
        else:
            raise Exception("Don't know how to understand types")

        if ctx.op.text == "+":
            self.stack.append(add_function(right, left))
        elif ctx.op.text == "-":
            self.stack.append(sub_function(right, left))

    def exitConvert_type(self, ctx:reviLangParser.Convert_typeContext):
        type_convert = CoolFunc.get_type(ctx.type_())
        print(type_convert)
        expr = self.stack.pop()
        if isinstance(type_convert, ir.DoubleType):
            convert_function = self.builder.sitofp(expr,type_convert)
        elif isinstance(type_convert, ir.IntType):
            print("fff")
            convert_function = self.builder.fptosi(expr,type_convert)
        else:
            raise print("I don't recognize this type")
        self.stack.append(convert_function)

    def exitExpressionMul(self, ctx: reviLangParser.ExpressionMulContext):
        left = self.stack.pop()
        right = self.stack.pop()
        mul_function = self.builder.mul
        div_function = self.builder.udiv
        rem_function = self.builder.urem


        double_type = ir.DoubleType()
        if isinstance(left.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
            mul_function = self.builder.fmul
            rem_function = self.builder.frem
            div_function = self.builder.fdiv
            left = self.builder.sitofp(left, double_type)
            right = self.builder.sitofp(right, double_type)
        if ctx.op.text == "*":
            self.stack.append(mul_function(right, left))
        elif ctx.op.text == "/":
            # left = self.builder.sitofp(left, double_type)
            # right = self.builder.sitofp(right, double_type)
            self.stack.append(div_function(right, left))
        elif ctx.op.text == "%":
            self.stack.append(rem_function(right, left))

    def enterAtom(self, ctx: reviLangParser.AtomContext):
        type_atom = ctx.op.type
        value_atom = ctx.getText()
        if type_atom == reviLangLexer.INT:
            result = ir.Constant(ir.IntType(32), int(value_atom))
        elif type_atom == reviLangLexer.DECIMAL:
            result = ir.Constant(ir.DoubleType(), float(value_atom))
        elif type_atom == reviLangLexer.ID:
            pointer = self.AST.get_variable(value_atom)
            if isinstance(pointer, Argument):
                result = pointer
            else:
                result = self.builder.load(pointer, value_atom)
        else:
            raise Exception("Unknown atom type")

        self.stack.append(result)
