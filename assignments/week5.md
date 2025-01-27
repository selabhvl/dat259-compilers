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

1. Install ANTLR, see [Instructions](../notes/antlr-00-setup-notes.md)
2. Create a `<YourLanguageName>Tokens.g4` file and then write your `lexer grammar` rules in it (UPPERCASE names!), see [Notes](../notes/antlr-01-lexer-notes.md) for further references.
3. For testing your lexer rules, you can use the `TestRig`, i.e.:
    - after each iteration you compile the Lexer class `javac *.java` (make sure that the antlr jar is on your classpath),
    - then run the `TestRig` in token mode:
    ```bash
    antdbg «YourLanguagName»Tokens tokens -tokens «your language file»
    ```
    the last parameter ("your language file") is optional. If it is not provided the TestRig reads from standard input, i.e.
    you can write your tokens directly in there (terminated by `CTRL-Z` in POSIX and `CTRL-D` in Windows.)


