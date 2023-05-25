from llvmlite import ir
from llvmlite import binding as llvm_binding


class OptimizationSecondTry:
    def __init__(self, module, parser):
        llvm_binding.initialize_all_targets()
        llvm_binding.initialize_all_asmprinters()

    def optimize_unusable_variables(self, module):
        llvm_binding.initialize_all_targets()
        llvm_binding.initialize_all_asmprinters()

        pass_manager = llvm_binding.create_module_pass_manager()
        pass_manager.add_dead_code_elimination_pass()
        pass_manager.initialize()

        for func in module.functions:
            pass_manager.run(func)

    def optimize_constants(module):
        llvm_binding.initialize_all_targets()
        llvm_binding.initialize_all_asmprinters()

        pass_manager = llvm_binding.create_module_pass_manager()
        pass_manager.add_constant_propagation_pass()
        pass_manager.initialize()

        for func in module.functions:
            pass_manager.run(func)

    def optimize_variable_assignments(module):
        llvm_binding.initialize_all_targets()
        llvm_binding.initialize_all_asmprinters()
        llvm_binding.initialize_all_passes()

        pass_manager = llvm_binding.create_module_pass_manager()
        pass_manager.add_memory_to_register_promotion_pass()
        pass_manager.initialize()

        pass_manager.run(module)
