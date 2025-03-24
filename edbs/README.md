# EDBS++ = Elektronisk DataBehandlings Språk (dobbeltpluss)

A simple programming language for demonstrating basic compiler construction using _antlr_ and _llvm_.
For sake of simplicity, Python is used as the interpretation language.
The proper way would be to use `C++` since this would allow for seamless interoperability with the LLVM API and tooling.
Here, we have to resort to the limited functionality provided via `llvmlite`.

## Setup

`llvmlite` requires `conda`. 
Thus, first make sure to have `conda` installed (e.g. using the [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install) installation).
Afterward, create a new environment with the required dependencies and activate it:
```bash
conda create -n edbs -f environment.yml
conda activate edbs
```

Now, you should be able to run the different tools from within the `/ebds` folder:
```bash
python interpreter.py ../examples/modules.edbs # invokes the interpreter
python typing.py ../examples/types.edbs # invokes the type checker
python compiler.py ../examples/hello.edbs # invokes the compiler
```

