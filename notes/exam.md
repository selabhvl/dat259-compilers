# Potential Exam Questions / Topics


1. Programming Languages and Compilers in general
    - What is a _programming language_? Why do we have high-level languages?
    - What is a _Translator_? What is a _Compiler_? What is an _Assembler_?
    - What are the typical _phases_ in compilation "pipeline"?
2. Lexical Analysis
    - What are _regular expressions_? Can you provide a regular expression for a common token in a programming language (e.g. whitespace, identifiers, floating point numbers etc.)?
    - How are regular expressions _operationalized_ to create lexers (i.e. the principal idea)?
    - What are _limitations_ of lexers based on regex/DFA-based recognizers? Do you have an example of syntax elements that cannot be recognized by a lexer?
3. Syntactical Analysis 
    - What is a _context-free grammar (CFG)_? Can you provide an example, e.g. some grammar rules for your favourite programming language?
    - What type of rules are usually challenging for LL-type parsers? What other _issues_ you may take into account when designing language rules? How did the parser generator that you were using resolve those? (Tipps: Think of arithmetic expressions!)
    - What are limitations of CFG-based parsers? What syntax elements cannot be recognized by a parser?
4. Syntax-Directed Translation and Type Checking
    - What _design pattern_ is a perfect fit for the implementation of syntax-directed tranlsators? Can you quickly sketch this pattern?
    - What additional data structure is needed when implementing a translator (e.g. an interpreter)?
    - What is a type-checker? What does it do? Why is it needed? Where can a type-checker be located in the compilation pipeline?
5. (Intermediate) Code Generation
    - What is an _intermediate representation (IR)_? Why is it needed?
    - What are the different aspects that have to be taken into account when creating a "native binary"? (Tipps: Think of _triples_!)
    - How are typical programming language control structures (e.g. loops) implemented in IR/Assembly language?
6. Program Runtime and Storage Organization
    - What is the typical organization of a binary program when it is loaded into memory?
    - What types of memory allocations exists? When do you use which?
    - When using heap-based dynamic memory allocation, two potential issues arise: dangling references and garbage collection? Can you quickly explain them?
7. Optimization
    - Control-Flow Graphs, Loop Optimization?
    - Peephole optimization?
    - Vector instructions?


