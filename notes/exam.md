# Potential Exam Questions / Topics


1. Programming Languages and Compilers in general
    - What is a _programming language_? Why do we have high-level languages?
    - What is a _Translator_? What is a _Compiler_? What is an _Assembler_?
    - What are the typical _phases_ in compilation "pipeline"?
2. Lexical Analysis
    - What are _regular expressions (RegEx)_? Can you provide a regular expression for a common token in a programming language (e.g. whitespace, identifiers, floating point numbers etc.)?
    - How are regular expressions _operationalized_ to create lexers? With other word: what is the relationship of RegEx and _(non-)deterministic finite automata (NFA/DFA)_ in the context of lexing?
    - What are _limitations_ of RegEx/DFA-based recognizers? Do you have an example of syntax elements that cannot be recognized by such a lexer?
3. Syntactical Analysis 
    - What is a _context-free grammar (CFG)_? Can you provide an example, e.g. some grammar rules for your favourite programming language?
    - What type of rules are usually challenging for _LL-type_ parsers? What other _issues_ you may take into account when designing language rules? How did the parser generator that you were using resolve those? (Tipps: Think of arithmetic expressions!)
    - What are _limitations of CFG-based parsers_? What syntax elements cannot be recognized by such a parser?
4. Syntax-Directed Translation and Type Checking
    - What _design pattern_ is a perfect fit for the implementation of _syntax-directed tranlsators_? Can you quickly sketch this pattern?
    - What _additional data structure_ is needed when implementing a translator (e.g. an interpreter)? How is it commonly implemented?
    - What is a _type-checker_? What does it do? Why is it needed? Where can a type-checker be located in the compilation pipeline?
5. (Intermediate) Code Generation
    - What is an _intermediate representation (IR)_? Why is it needed?
    - What are the different aspects that have to be taken into account when creating a _"native binary"_? (Tipps: Think of _triples_!)
    - How are typical programming language _control structures_ (e.g. loops) _implemented_ in IR/Assembly language?
6. Program Runtime and Storage Organization
    - What is the typical _organization of a binary program_ when it is loaded into memory?
    - What _types of memory allocations_ exists? When do you use which?
    - When using _heap-based dynamic memory allocation_, two potential issues arise: _dangling references_ and _garbage collection (GC)_? Can you quickly explain them?
7. Optimization
    - What is the _purpose and general idea of optimization_? Can you explain one common optimization "pass" (for instance: inlining, memory to register assignment, peephole optimizations, dead code elimination, various loop optimizations)
    - What is a _Control-Flow Graph (CFG)_? How does it look like? Why is it important for optimization?
    - What is _Vectorization_? What facilitates it? How can it used to speed up computations?


