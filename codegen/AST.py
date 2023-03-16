class MainAST:
    function_list = {}

    def add_function(self, name, pointer):
        self.function_list[name] = pointer

    def get_function(self, name):
        return self.function_list[name]


class FunctionAST:
    variable_list = {}

    def __init__(self,name,main_ast:MainAST,function):
        self.main_ast = main_ast
        self.name = name
        self.function = function
        main_ast.add_function(self.name,self)

    def add_variable(self,name,pointer):
        self.variable_list[name] = pointer

    def get_variable(self,name):
        return self.variable_list[name]