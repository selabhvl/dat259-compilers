lexer grammar EDBSTokens;


FINISH_KEYWORD : 'FERDIG.';
PERIOD : '.';
COLON : ':';
COMMA : ',';
PRIMED: '\'';
WRITE_KEYWORD : 'SKRIV';
READ_KEYWORD: 'LES';
CALC_KEYWORD : 'REKN';
REPEAT_KEYWORD :  'GJENTAR';
CONDITION_KEYWORD : 'MEDAN';
UPDATE_KEYWORD : 'OPPDATER';
DEFINE_MOULE_KEYWORD : 'DEFINER EIT MODUL';
MODULE_PARAM_KEYWORD : 'MED';
INPUT_PARAM_KEYWORD : 'INN';
OUTPUT_PARAM_KEYWORD: 'UT';
MODULE_BODY_KEYWORD: 'SOM';
EXIT_MODULE_KEYWORD: 'AVSLUT MODUL';
CALL_MODULE_KEYWORD: 'KALL';
FILE_KEYWORD: 'FIL';
IN_KEYWORD: 'i';

BOP_NOT : 'IKKJE';
BOP_AND : 'OG';
BOP_OR : 'ELLER';


COMP_EQL : '=';
COMP_LT : '<';
COMP_LEQ : '<=';
COMP_GT: '>';
COMP_GEQ: '>=';

OP_ADD : '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV : '/';
OP_EXP : '^';

SOP_CONCAT : '++';
SOP_REPEAT : '**';
SOP_SPLIT : '//';
SOP_SUBSTR : '--';

LOP_NEXT : 'neste';
LOP_FIND : 'finn';
LOP_BACK : 'førre';
LOP_RESET : 'tilbakestill';
LOP_RESET_IDX : 'til';

NULL_CHAR : '<tom>';
NEWLINE_CHAR : '<linjeskift>';
WHITESPACE_CHAR : '<tomrom>';

fragment CHAR : [a-zA-ZåæøÅÆØ];
fragment CHAR_PLUS : CHAR | '-';
fragment DIGIT: [0-9];

NUMBER : '-'? DIGIT+ (',' DIGIT+)?;
IDENTIFIER: CHAR CHAR_PLUS*;
STRING : '«' (~[»])* '»';
COMMENT : 'OBS!' (~[\r\n])* NEWLINE -> skip;
NEWLINE : '\r'? '\n' [ \r\n\t]*;
WHITESPACE : [ \r\n\t]+ -> skip;

