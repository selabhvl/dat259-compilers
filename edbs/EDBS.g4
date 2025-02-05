grammar EDBS;
import EDBSTokens;

program :  statement* FINISH_KEYWORD NEWLINE?;

statement : ( write_stmt | calc_stmt ) PERIOD NEWLINE;

write_stmt  : WRITE_KEYWORD STRING;

calc_stmt : CALC_KEYWORD IDENTIFIER COLON expression;

expression:   expression OP_MUL expression
         | expression OP_ADD expression
         |  NUMBER;
