# LLVM First Steps

Probably, the easisest way to get started with LLVM is by using `clang` and observing how simple C programs get translated to machine code via LLVM.

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
When calling 
```bash 
clang hello.c -o hello
```

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

So, let us explore the _intermediate representation (IR)_ that LLVM uses. 
You can force `clang` to emit LLVM IR with the following command:

```bash
clang -emit-llvm -S hello.c 
```


## LLVM IR Language

The most important resource is the [LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html).
You should always have it opened in a tab of your web browser while writing or generating LLVM IR code.


