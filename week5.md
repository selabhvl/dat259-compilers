# 2025-01-29 - Lecture 2: Lexical Analysis

## Agenda

- Presentation of _your_ programming language
- Theoretical Background: Lexical Analysis 
    - Alphabets, Languages, Regular Expressions
    - Deterministic Finite Automata (DFA), Non-deterministic Finite Automate (NFA), $\epsilon$-NFA 
- RegEx exercises
- Intro: Antlr

## RegEx in-lecture exercises:

To warm up a bit, here are some exercises to get used into writing regular expressions.
Use https://regex101.com/ to debug your regexes.

1. Write a regex to match all the strings containing the sequence "cat".

Test Input:
```
concatenate
catching
category
caterpillar
```

2. Write a regex to match strings that start with a digit.

Test Input:
```
123abc
456xyz
789def
0abc
```

3. Write a regex to match any string that contains only uppercase letters.

Test input:
```
HELLO
World
Rust
zig
JAVA
```

4. Write a regex to match any string that contains exactly 3 digits.

Test input:
```
69          # no match
123         # match
hello123    # match
4444        # no match
12hei3      # match
12heiho45   # no match
```

5. Write a regex to match any string that contains at least one digit.

Test input:
```
world1        # match
world         # no match
1hallllooooo0 # match
```

6. Extract dates in "YYYY-MM-DD" format from the given text.

Test input:
```
The event is scheduled on 2022-11-15.
The deadline is 2023-05-20.
Birthday: 2021-01-01.
Expected: 2024-12-25.
```

7. Write a regex to match valid email addresses.

Test input:
```
john.doe@example.com
jane_smith123@example.org
alice@great-domain.net
bob@sub.example.co.uk
@google.com     # invalid
hvl@            # invalid 
mail@google     # invalid 
post@.com       # invalid
```

8. Write a regex to match valid IP address (IPv4).

Test input:
```
192.168.1.1
255.255.255.0
127.0.0.1
10.0.0.1
0.0.0.0
388.123.0.1 # invalid
127.0.1     # invalid 
192..1      # invalid
```


## Assignment: Develop a Lexer for your language 

1. Make sure you have JAVA (>= 11) installed (i.e. the JVM binary `java` is on your path)
2. Download the [antlr-complete.jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar) (current version when writing this on 2025-01-22: 4.13.2)
3. Define the following shell-aliases (Windows users have to find out how to do the following bash commands in [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/using-aliases?view=powershell-7.4)):
```bash
alias antlr4='java -jar /path/where/you/downloaded/antlr-4.13.2-complete.jar'
alias grun='CLASSPATH=".:/path/where/you/downloaded/antlr-4.13.2-complete.jar:$CLASSPATH" java org.antlr.v4.gui.TestRig'
```
**NOTE** It is super importatnt to keep the little `.:` at the front of the `CLASSPATH` variable definition!
4. Create a `<YourLanguageName>.g4` file and then write your lexer rules in it (UPPERCASE names!)
5. Add a simple "catch-all" grammar rule on the top at the end (also make sure that you handle whitespace):
```
file : (
    TOKEN1 |
    TOKEN2 |
    ...
    TOKENN ) *;
```
6. Compile the generated java code in the current directory with 
```bash
javac *.java
```
7. Check whether all tokens are recognized in your example file:
```bash
grun <YourLanguageName> file -tokens <example-file>
```


