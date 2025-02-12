grammar EDBS;
import EDBSTokens;

program :  statement* FINISH_KEYWORD NEWLINE?;

statement : ( write_stmt | calc_stmt | read_assgn) PERIOD NEWLINE;

read_assgn: READ_KEYWORD IDENTIFIER COLON STRING;

write_stmt  : WRITE_KEYWORD write_arg+ ;

write_arg : STRING | IDENTIFIER;

calc_stmt : CALC_KEYWORD IDENTIFIER COLON expression;

expression:  expression OP_EXP expression # expo
        | expression OP_MUL expression # mul
        | expression OP_DIV expression # div
         | expression OP_ADD expression # add
         | expression OP_SUB expression # sub
         | '(' expression ')' # nested
         | IDENTIFIER # var
         |  NUMBER # lit
        ;