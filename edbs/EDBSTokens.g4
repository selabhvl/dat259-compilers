lexer grammar EDBSTokens;

// TODO: the following is able to parse the hello world example
// BUT: a few keywords and concepts (numbers, operators) are missing
// see the other files beneath /examples
PERIOD : '.';
WRITE_KEYWORD : 'SKRIV';
FINISH_KEYWORD : 'FERDIG';
STRING : '«' (~[»])* '»';
COMMENT : 'OBS!' (~[\r\n])* NEWLINE;
NEWLINE : '\r'? '\n';
WHITESPACE : [ \r\n\t]+ -> skip;

