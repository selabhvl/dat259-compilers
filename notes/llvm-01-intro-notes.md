# LLVM First Steps

This and the following lectures will focus on understanding and LLVM and how it can be used for generating _native programs_.
Instructions are only provided for Mac OS X and Linux since we fill only focus on the UNIX system interface.
If you are using Windows, please consider using WSL!

## Installation

platform specific...

Probably, the easisest way to get started with LLVM is by using `clang` and observing how simple C programs get translated to machine code via LLVM.


## Producing Native Binaries

Start by writing the classic _hello world_ in C:

```c 
#include <stdio.h>

int main(int argc, char *argv[]) 
{
    printf("Hello, World!\n");
    return 0;
}
```
Let us name this file `hello.c`. 

Upon calling 
```bash 
clang -o hello hello.c
```
(The `-o` parameter is optional, and is used define the name of the resulting binary. If it is left unspecified, the generic name `a.out` will be used).

you will get a _native_ binary called `hello`. 

This file can be run directly from you shell by pasing the filename as the first parameter:
```bash 
./hello
```
which will write the following to standard out (as expected):
```
Hello, World!
```

So far, this is nothing special, as you could (and maybe you already did this earlier in your life if you have been learning C before?) 
have done the exact same thing with the GNU C compiler `gcc`.

Thus, let us now explore the different phases of producing a binary explicitly (`clang` is hiding those from us)

### Step 1: Intermediate Representation

The first step, coming from a high-level language (like `C`) is to produce an _intermediate representation (IR)_.
By convention, the file ending for the LLVM IR is `.ll`.
We can force `clang` to output the corresponding IR for the Hello World program.


```bash
clang -emit-llvm -S -o hello.ll hello.c 
```
(the `emit-llvm` is the important option here and tells clang to produce IR instead of a binary. It is also important to provide the `-S` option here to disable _linking_, which is required when only  outputting IR).


**Exercise:** Open the `hello.ll` file in a text editor! Can you make sense of its contents?

### Step 2: Bitcode

The LLVM IR is a human-readable format for the low-level instructions that LLVM can translate into optimized machine code.
This format can be translated into a more (space-)efficient binary format called _bitcode_ (`.bc`).
We can translate IR into bitcode using the `llvm-as` tool:

```bash
llvm-as -o hello.bc hello.ll
```

### Step 3: Compilation

The "core" of the LLVM infrastructure is the _compiler_ (`llc`) that translates the intermediate representation into native assembler.
Try calling:

```
llc hello.bc
```
Normally, this should produce an assembly file (`hello.s`).
If not, i.e. when you are getting a binary at once, you can explicitly ask for assembly by providing the `-filetype=asm` option.

**Exercise**: Open the `hello.s` file in a text editor! Can you make sense of its contents?


### Step 4: Assembling

**Note:** This and the following step are _system dependent_ (i.e. the paths and paremeters may differ). 
You will always be able to execute both in one pass by directly calling `clang` with the assembly file as argument.
`clang` will then call the system assembler and linker with the correct parameters.
However, for pedagocial reasons I would like to invite you to step through the following steps manually 
to explore what happens behind the scenes. 
If you find out that the following commands are not working, feel free to create pull request to cover as much operation system constellations as possible.


In the next phase, the assembly file containing the native instructions needs to be translated to _machine code_ (i.e. the binary representation of the system instructions). 
This is done via the system assembler (which is called `as` on POSIX systems).
```bash
as -o hello.o hello
```

The output of the assembly phase is an _object file_ (`.o`), which contains _relocatable machine code_.
This means that the instructions refer to named locations of (system) library functions.
The latter are not resolved yet, therefore linking is required.

### Step 5: Linking 

To create a native binary, which contains the _absolute machine code_, linking is required, which 
resolves the symbolic names in the object file.
Generally, the C standard library is used as an intermediary for contacting the operating system (reading/writing from standard in/out, files, etc.).
On POSIX systems, the system linker is called `ld`.
The latter requires the location of the system library as an argument:

#### Mac OS X

On Mac OS X, the system C library needs to be installed with the "Xcode Terminal Development Tools", which are located at `/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/` per default.

Linking should work via:
```bash 
ld -o hello -syslibroot /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/ -lSystem hello.o
```

#### Linux 

On Linux, the system library must be dynamically linked including the C standard library (which should be located at `/usr/lib/crt1.o`):

```bash
ld -o hello -dynamic-linker /lib/ld-linux.so.2 /usr/lib/crt1.o /usr/lib/crti.o output.o -lc /usr/lib/crtn.o
```

Finally, you can try whether the produced binary corresponds to one produced by `clang` in one step, by executing it.


## LLVM IR Language


The most important resource from now on is the [LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html).
You should always have it opened in a tab of your web browser while writing or generating LLVM IR code :wink:

Let us revisit the result from the first step ("producing intermediate representation"): Open `hello.ll` in a text editor!
Could you make sense of it previously?

First of all, it is important to note that the generated code is a bit more complicated thant it needs to be (because it 
it contains a lot of metadata and optimization flags).

You can basically delete... 
- ...the `source_filename` instruction,
- ...everything associated with `!`s (exclamation marks), since this is only metadata,
- ...everything associated with `#`s (hash tags), since these are mostly optimization attributes,
- ...all comments (line comments starting with `;`) except for the one containing `ModuleID = `,
- ...all alignment instructions (`align N`),
- ...optimization keywords such as (`private`, `unnammed_addr`, `noundef`, `nounwind`, ...)


Moreover, the `alloca`/`store`-instruction pairs define local scope variables that are written but never read (i.e. unused variables) and therefore they can be deleted as well.
The resulting simplified "Hello World" in LLVM IR looks something like this:


```llvm 
; ModuleID = 'hello.c'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128-Fn32" ; this may be different on your system
target triple = "arm64-apple-macosx15.0.0" ; also this may be different on you system

@.str = constant [13 x i8] c"Hello World\0A\00"

define i32 @main(i32 %0, ptr %1) {
  %6 = call i32 @puts(ptr @.str)
  ret i32 0
}

declare i32 @puts(ptr)
```

This simplified "Hello World" is hopefully much easier to understand now.
As you may see, LLVM IR is basically a simplified form of assembler (reduced instruction set (RISC)) that features some high-level convenience features such as _function calls_ and _data types_. 

As introductory resources, I recommend [this video](https://www.youtube.com/watch?v=m8G_S5LwlTo) and the associated [slide set](https://llvm.org/devmtg/2019-04/slides/Tutorial-Bridgers-LLVM_IR_tutorial.pdf).

After this introduction, you are invited to implement some introductory programming exercises in LLVM IR. 
To make things even easier, we can (ab)use C's return code mechanism to test numerical functions directly.
For instance, a `main` program that constantly returns `42`:

```llvm 
; ModuleID = 'theanswer'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128-Fn32" ; this may be different on your system
target triple = "arm64-apple-macosx15.0.0" ; also this may be different on you system

define i32 @main(i32 %0, ptr %1) {
  ret i32 42

```

can diretly be interpreted by LLVM using `lli` and then getting the return code of the last executed process via `$?`

```bash
lli theanswer.ll;echo $?
```

Some suggestions, for programming exercises:

- `max` (returns the biggest of two input numbers)
- `fac` (calculates the factorial of one onput number, recursive variant)
- `fac` (same as above but in an iterative manner, i.e. using a loop)
- `fib` (calculate fibonacci, both iterative and recursive vartant)
- [Collatz Sequence](https://en.wikipedia.org/wiki/Collatz_conjecture)
