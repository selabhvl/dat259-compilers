# LLVM Code generation


The official bindings for LLVM exist only for the `C++` programming language.
If one wants to use Python for implementing the compiler, a viable option 
is to use [`llvmlite`](https://llvmlite.pydata.org/en/latest/index.html).
The latter has some drawback, for instance that it only supports a limited subset of the LLVM IR bindings,
that is based on an outdated version of LLVM (i.e. version 15).
However, it allows us to generate all the instrcutions that are required for our purposes.

llvmlite is a subproject of the numba project and is officially supported by Anaconda.
Hence, installation requires `conda`.


## Generating "Hello World"

The following Python code uses llvmlite to generate a hello world:

```Python
from llvmlite import ir
import llvmlite.binding as llvm
import subprocess
from pathlib import Path

llvm.initialize()
llvm.initialize_native_target()

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
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
module.triple = target_machine.triple
module.data_layout = str(target_machine.target_data)

# and declare a function named "fpadd" inside it
str1 = ir.ArrayType(i8, 7)
const = ir.GlobalVariable(module, str1, "hello")
const.initializer = ir.Constant(str1, bytearray(b'Hello\n\0'))
printf = ir.Function(module, printf_type, name='printf')
func = ir.Function(module, main_type, name="main")

# Now implement the function
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
builder.call(printf, (const,))
builder.ret(ir.Constant(i32, 0))


with open(file_name, "w") as output_file:
    output_file.write(str(module))

subprocess.run(['clang', file_name, '-w', '-o', base_name.stem ])
```
