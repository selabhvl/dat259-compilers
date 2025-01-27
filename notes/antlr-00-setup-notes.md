# Antlr Setup

In the first half of the course we will use the tool [ANTLR](https://www.antlr.org/) quite heavily.

## Install

The installation is basically as simple as downloading the [JAR file](https://www.antlr.org/download/antlr-4.13.2-complete.jar)
and then running it with the Java virtual machine (I think the minimum requirement is version 11).
Assuming that the JVM binary `java` is on your `$PATH`, antlr is run via:

```bash
java -jar /path/where/you/downloaded/antlr-4.13.2-complete.jar «GrammarFile».g4
```

To make usage even more convenient on the command line, I recommend you to set up the following aliases and environment variables (which are inspired by the [book](https://pragprog.com/titles/tpantlr2/the-definitive-antlr-4-reference/)):


```bash
export CLASSPATH=".:/path/where/you/downloaded/antlr-4.13.2-complete.jar:$CLASSPATH"
alias antlr='java -jar /path/where/you/downloaded/antlr-4.13.2-complete.jar'
alias antdbg='java org.antlr.v4.gui.TestRig'
```
**IMPORTANT** It is super important to keep the little `.:` at the front of the `CLASSPATH` variable definition!

> [!NOTE]
> In the above listing and in the wollowing, when providing SHELL commands, I will always assume you are on a POSIX-like shell, e.g.
> bash, zsh, fish or similar. This applies to Mac OS X and Linux users out of the box! If you are a Windows
> user you can get such a POSIX-like environment by installing [Cygwin](https://cygwin.com/) or the [Git Shell for Windows](https://git-scm.com/downloads/win). Probably, you could also re-create the experience in [Windows powershell by defining respective aliases](https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/using-aliases?view=powershell-7.4),
> but here you will have to do the googling yourself :wink:

Afterwards, you are able to generate lexer and parsers from a (lexer) grammer file (ending `.g4`) with:
```bash
antlr «GrammarName».g4
```
and you can debug your language (given that you had compiled the Lexer and Scanner with `javac *.java` before) with:

```bash
antdbg «GrammarName» «Entrypoint Rule» -gui «File in Grammar Syntax»
```


## IDE support 

If you are using a JetBrains IDE like IDEA or PyCharm, I recommend you to also install the [official ANTLRv4 Plugin](https://plugins.jetbrains.com/plugin/7358-antlr-v4) which makes language development even easier!
