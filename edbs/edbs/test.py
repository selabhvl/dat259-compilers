from llvmlite import ir
import llvmlite.binding as llvm

import subprocess
from pathlib import Path

llvm.initialize()
llvm.initialize_native_target()
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()

# Create some useful types
double = ir.DoubleType()
ptr = ir.PointerType()
i8 = ir.IntType(8)
i32 = ir.IntType(32)
main_type = ir.FunctionType(i32, (i32, ptr))
printf_type = ir.FunctionType(i32, (ptr,), var_arg=True)

# Create an empty module...
base_name = Path(__file__)
file_name = base_name.with_suffix(".ll")

module = ir.Module(name=base_name.name)
module.triple = target_machine.triple
module.data_layout = str(target_machine.target_data)

text = "Hello World\n\0"
textb = text.encode()
str1 = ir.ArrayType(i8, len(textb))
const = ir.GlobalVariable(module, str1, "hello")
const.initializer = ir.Constant(str1, bytearray(textb))

printf = ir.Function(module, printf_type, name='printf')
func = ir.Function(module, main_type, name="main")

# Now implement the function
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
builder.call(printf, (const,))
builder.ret(ir.Constant(i32, 0))

print(module)

#with open(file_name, "w") as output_file:
#    output_file.write(str(module))

#subprocess.run(['clang', file_name, '-w', '-o', base_name.stem ])