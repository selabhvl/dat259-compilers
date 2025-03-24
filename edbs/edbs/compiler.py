import subprocess

import llvmlite.ir as ir
import llvmlite.binding as llvm

from edbs.parser.EDBSVisitor import EDBSVisitor
from edbs.symbols import SymbolTable
from pathlib import Path


def init_module(source_file: Path):
    module = ir.Module(name=source_file.name)
    target = llvm.Target.from_default_triple()
    machine = target.create_target_machine()
    module.triple = machine.triple
    module.data_layout = str(machine.target_data)
    return module

BYTE_TYPE = ir.IntType(8)
DEFAULT_INT = ir.IntType(32)
PRINTF_TYPE = ir.FunctionType(DEFAULT_INT, (ir.PointerType,), var_arg=True)

class Compiler(EDBSVisitor):

    def __init__(self, source_file: Path, symbols: SymbolTable):
        self.symbols = symbols
        self.source_file = source_file
        self.module = init_module(source_file)
        self.uses_c_printf = None

    def with_printf(self):
        if not self.uses_c_printf:
            fun = ir.Function(self.module, PRINTF_TYPE, name='printf')
            self.uses_c_printf = fun
        return self.uses_c_printf

    def write_llvm_file(self):
        with open(self.source_file.with_suffix(".ll"), "wt") as out:
            out.write(str(self.module))

    def call_llvm_compile(self):
        subprocess.run(['clang', self.source_file.with_suffix(".ll"), '-w', '-o', self.source_file.stem])