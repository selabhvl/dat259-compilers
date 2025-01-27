# Lexing with ANTLR

The lexer is defined via the definition of _lexer rules_. 
Their definition is similar to _parser rules_ (coming later).
The difference is that lexer rules **start with an UPPERCASE** letter (it is common that the whole rule then is written all uppercase letters).
A complete reference about lexer rules can be found in chapter 15.5 in the [ANTLR Book](https://pragprog.com/titles/tpantlr2/the-definitive-antlr-4-reference/).


## Lexer Rule 

The general syntax is:
```
«RuleName» : «regular expression» 
```

The regular expressions follow the general syntax you learned in the lecture (with some convenience features like in UNIX regex).
- Match a single character `c` with: `'c'` (you can use the all unicode characters; if you know the unicode-code point you can use `\uXXXX` where `XXXX` is unicode code point; the character `.` represents a _wildcard_ (any character), `\` works as an _escape_, i.e. to match a literal period, one needs to write `'\.'`)),
- Match a sequence of reg-exes _r1_, ... _rn_: `«r1» «r2» « ... » «r2»` (whitespaces are optional, and if your sub-regexes _r1_ to _rn_ are all single characters you can alternatively write `'hello'` instead of `'h' 'e' 'l' 'l' 'o'`).
- Match a choice between regexes _r1_, ..., _rn_ with `«r1» | «r2» | « ... » | «r2»` (notice the vertical bars; also if all sub-regexes _r1_ to _rn_ are all single characters you can define a character set: `[abc]` is a shorthand for `'a' | 'b'| 'c'`).
- Match an optional, arbitrary, or at-least-once occurence of a sub-regex _r_ via `?`, `*`, or `+`. Notice that you might have add parantheses `(` `)` where necessary.
- alternatively, you can also call another lexer rule `R` (if you already defined the regex in another rule). Recursion is allowed (but no _left-recursion_). The called rules can be proper rules or _fragment rules_.

Another useful convenience feature w.r.t. to character classes. When you have a big choice of valid characters and their byte representations are located next to each other, e.g.
all ASCII lowercase letters, you can write `'a' .. 'z'` or alternatively (`[a-z]`) to match them (code $97$ until $122$).
Character classes can also be negated with `~`, i.e. `~[ \r\t\n]` would match _every non-whitespace character_!


### Advanced concepts

#### Fragment rules 

By adding the keyword `fragment` in front of a rule definition, the respective rule becomes a _fragment rule_. 
Fragment rules do not create tokens put are meant solely to be used as parts of other lexer rules, i.e.
for better modularization.

#### Conflicting Rule 

If you have overlapping rules like e.g.:
```
INT: '-'? [1-9][0-9]*;
FLOAT: '-'? [1-9][0-9]*('.'[0-9]+)?;
```
then conflicts are resolved by favorising the rule that is defined first.
If you would swap the order of the two rules above, every number would be matched as a `FLOAT` even when they
do not have a fractional part.

#### Non-greedy sub-rules 

Per default the `r*` operator tries to match the pattern `r` _greedy_ (i.e. as far as possible). 
To make a rule non-greedy, one may add a `?`:
A use case might be for matching a _string literal_ (i.e. matching anything between a pair of `"` `"`).
```
STRING : '"' .*? '"' ;
```
Without the question mark `.*` would match any character (including the final delimitting `"`).


#### Lexer commands

Following the regex definition in a rule one may add a arrow-character-sequence (`->`) to perform a command.
Possible commands are:
- `skip`: Do not output any token. Generally used for dropping whitespace.
- `type(T)`: Can be used to create _token supertypes_.
- `channel(C)`: Can be used to write tokens to different channels.
- `pushMode(M)`/`popMode`: Used for different lexical parsing modes.


