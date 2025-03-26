import os
import subprocess

import llvmlite.ir as ir
import llvmlite.binding as llvm

from edbs.parser.EDBSParser import EDBSParser
from edbs.parser.EDBSVisitor import EDBSVisitor
from edbs.symbols import SymbolTable
from pathlib import Path
import  sys
from edbs.utils import  parse


def init_module(source_file: Path):
    llvm.initialize()
    llvm.initialize_native_target()
    module = ir.Module(name=source_file.name)
    target = llvm.Target.from_default_triple()
    machine = target.create_target_machine()
    module.triple = machine.triple
    module.data_layout = str(machine.target_data)
    return module

BYTE_TYPE = ir.IntType(8)
DEFAULT_INT = ir.IntType(32)
PRINTF_TYPE = ir.FunctionType(DEFAULT_INT, (ir.PointerType(),), var_arg=True)
MAIN_TYPE = ir.FunctionType(DEFAULT_INT, (DEFAULT_INT, ir.PointerType()))

class Compiler(EDBSVisitor):



    def __init__(self, source_file: Path, symbols: SymbolTable):
        self.symbols = symbols
        self.source_file = source_file
        self.module = init_module(source_file)
        self.uses_c_printf = None
        self.current_builder = None
        self.constant_counter = 0

    def next_constant(self, prefix: str = "str"):
        next_id = self.constant_counter
        self.constant_counter += 1
        return f"{prefix}{next_id}"


    def visitProgram(self, ctx:EDBSParser.ProgramContext):
        mainf = ir.Function(self.module, MAIN_TYPE, "main")
        main_body = mainf.append_basic_block("entry")
        self.current_builder =  ir.IRBuilder(main_body)

        for stmt in ctx.children:
            self.visit(stmt)
        self.current_builder.ret(ir.Constant(DEFAULT_INT, 0))



    def visitWrite(self, ctx:EDBSParser.WriteContext):
        to_print = []
        for c in ctx.children:
            inner_arg = self.visit(c)
            if isinstance(inner_arg, str):
                to_print.append(inner_arg)

        argument = " ".join(to_print) + "\n\0"
        argumentb = argument.encode()
        array_type = ir.ArrayType(BYTE_TYPE, len(argumentb))
        array_val = ir.Constant(array_type, bytearray(argumentb))

        glob_str = ir.GlobalVariable(self.module, array_type, name=self.next_constant())
        glob_str.global_constant = True
        glob_str.initializer = array_val

        assert self.current_builder is not None
        self.current_builder.call(self.with_printf(), (glob_str,))


    def visitWrite_arg(self, ctx:EDBSParser.Write_argContext):
        if ctx.STRING():
            val = str(ctx.STRING())[1:-1]
            return val
        # TODO var


    def with_printf(self):
        if not self.uses_c_printf:
            fun = ir.Function(self.module, PRINTF_TYPE, name='printf')
            self.uses_c_printf = fun
        return self.uses_c_printf

    def write_llvm_file(self):
        with open(self.source_file.with_suffix(".ll"), "wt") as out:
            out.write(str(self.module))

    def delete_llvm_file(self):
        f = self.source_file.with_suffix(".ll")
        if f.exists():
            os.remove(f)

    def call_llvm_compile(self):
        subprocess.run(['clang', self.source_file.with_suffix(".ll"), '-w', '-o', self.source_file.stem])

    def print_llvm(self):
        return str(self.module)


def main():
    if sys.argv.__len__() >= 2:
        fname = sys.argv[1]
        fpath = Path.cwd() / fname
        ast = parse(fpath)
        symbol_table = SymbolTable()
        compiler = Compiler(fpath, symbol_table)
        compiler.visit(ast)
        if "--debug" in sys.argv:
            print(compiler.print_llvm())
        if "--no-compile" not in sys.argv:
            compiler.write_llvm_file()
            compiler.call_llvm_compile()
    else:
        print("Wrong arguments provided")

if __name__ == "__main__":
    main()

