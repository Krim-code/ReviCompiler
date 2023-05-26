import re
from llvmlite.ir import *
from llvmlite import ir, binding
from llvmlite import binding as llvm


def constant_fold(ir_text):
    # Создаем объект Module, который будет хранить набор функций и глобальные переменные
    module = Module()

    # Добавляем функцию в модуль
    func = Function(module, FunctionType(IntType(32), [IntType(32), IntType(32)]), "mymul")
    # Определяем блок и вставляем его в функцию
    block = func.append_basic_block("entry")
    # Создаем IRBuilder с указанием вставлять инструкции в блок
    builder = IRBuilder(block)

    # Загружаем LLVM IR из переданной строки
    module.parse(ir_text)

    # Определяем шаблон для поиска бинарных операций с константами-операндами
    pattern = r"(\s*%[\w.]+) = (\w+) i32 (\d+), (\d+)"

    # Ищем все соответствия шаблону в загруженном модуле
    for match in re.finditer(pattern, str(module)):
        # Определяем оператор и константы из найденной бинарной операции
        operator = match.group(2)
        const1 = int(match.group(3))
        const2 = int(match.group(4))

        # Вычисляем результат операции
        if operator == 'add':
            result = const1 + const2
        elif operator == 'sub':
            result = const1 - const2
        elif operator == 'mul':
            result = const1 * const2
        elif operator == 'sdiv':
            result = const1 // const2
        else:
            continue

        # Заменяем инструкцию на инструкцию присваивания с результатом операции
        build_instruction = builder.alloca(IntType(32))
        builder.store(Constant(IntType(32), result), build_instruction)

        find_instruction = builder.del_inst(named_values[match.group(1)].ref)
        find_instruction.replace_all_uses_with(build_instruction)

    # Компилируем нашу функцию и возвращаем LLVM IR
    return str(module)


def optimize_llvm_file(input_filename, output_filename):
    # Load the input file and parse the LLVM IR code
    with open(input_filename, 'r') as f:
        llvm_code = f.read()
    llvm_module = llvm.parse_assembly(llvm_code)
    llvm_module.verify()

    # Create a target machine
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_all_asmprinters()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine(codemodel="small")

    # Optimize the module using constant folding
    llvm_module = constant_fold(str(llvm_module))

    # pass_manager_builder = llvm.create_pass_manager_builder()
    #
    # module_pass_manager = llvm.create_module_pass_manager()
    # module_pass_manager.add_basic_alias_analysis_pass()
    #
    # pass_manager_builder.populate(module_pass_manager)
    #
    # module_pass_manager.run(llvm_module)

    # Write the optimized LLVM IR to an output file
    with open(output_filename, 'w') as f:
        f.write(str(llvm_module))


# Example usage:
optimize_llvm_file('revi.str', 'revi_temp2.s')
