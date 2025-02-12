# Antlr Parsing

It is time to move on! 
Lexer rules based on the language of _regular expressions_ are a powerful tool to define arbitrary tokens.
However, they have limitations, e.g. the language of _balanced parentheses_ (i.e. "as many opening parentheses as closing parentheses") cannot be expressed with regular expressions or equivalently: cannot be recognized by a finite automaton (check the [Pumping Lemma](https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages) if you want to know why).

Hence, we need a more powerful tool: It is called _context-free grammars (CFG)_. 
They look pretty much similar to regular expressions first. 
The _new_ thing is that it is allowed to have rules that called themselved recursively.

When it comes to antlr, not that much changes. The most fundamental:

- You have to write `grammar X;` instead of `lexer grammar X;` in your language file `X.g4`
- Rules must now start with a **lowercase** letter: `rule : ...`.

The rest stays pretty much the same: You still define rules using sequence and choice (as well as `?`, `*`, and `+`)
but rules may call themselves directly or indirectly.

You can also import existing lexer rules using an import:
```
import XTokens;
```

## Parsing Expressions 

In general, parsing infix expressions with different operators and different precendences is tricky!
For instance, the following rule:
```
expression : expression '+' expression | expression '*' expression | '(' expresssion ')' | INT;
```
would be ambiguous if one would not specifcy _precedence_ (i.e. binding power of operators).
Also, this example contains _left recursion_, which normally is a problem for efficient top-down parsers.
However, there has been a lot of theoretical work in this domain and antlr comes with a powerful implementation
that solves these problems _automagically_.

You just need to know:

- Antlr defines _precendence_ based on the order of sub-rules in the choice (`|`), i.e. the first alternative has highest precedence,
- Antlr normally _associates_ from left to right, if your operator should associate the other way (e.g. "function composition" or "exponentiation") you must add `<assoc=right>` before the rule,
- Antlr handles direct left-recursion out-of-the-box but it cannot deal with _indirect left-recursion_.

## Tool support 

I heavily encourage to check out the Antlr plugin for the JetBrains IDEs, it makes developing and debugging grammar rules very easy! :wink:
