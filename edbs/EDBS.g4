grammar EDBS;
import EDBSTokens;

program : module_def*  main_statement* FINISH_KEYWORD NEWLINE?;

module_def : DEFINE_MOULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD NEWLINE?
                input_params NEWLINE? output_params
                NEWLINE? MODULE_BODY_KEYWORD COLON NEWLINE?
                module_body
                EXIT_KEYWORD MODULE_KEYWORD PERIOD NEWLINE?;


input_params : INPUT_PARAM_KEYWORD COLON param_list;
output_params :OUTPUT_PARAM_KEYWORD COLON IDENTIFIER;

module_body : main_statement+;

param_list : IDENTIFIER (COMMA IDENTIFIER)*;

main_statement : stmt PERIOD NEWLINE;

stmt : REPEAT_KEYWORD NEWLINE? stmt (COMMA NEWLINE? stmt)* NEWLINE? CONDITION_KEYWORD bool_expr # while
    | READ_KEYWORD IDENTIFIER COLON STRING # read
    | READ_KEYWORD FILE_KEYWORD IDENTIFIER STRING? # readfile
    | WRITE_KEYWORD write_arg+  # write
    | CALC_KEYWORD IDENTIFIER COLON expression # calc
    | UPDATE_KEYWORD IDENTIFIER COLON expression # mutate
    | EXIT_KEYWORD EXCLAMATION # return
    ;

write_arg : STRING | IDENTIFIER;

expression:  expression OP_EXP expression # expo
        | expression OP_MUL expression # mul
        | expression SOP_REPEAT expression # repeat
        | expression OP_DIV expression # div
         | expression SOP_SPLIT expression # split
         | expression OP_ADD expression # add
         | expression SOP_CONCAT expression # concat
         | expression OP_SUB expression # sub
         | expression SOP_SUBSTR expression # substr
         | '(' expression ')' # nested
         | CALL_MODULE_KEYWORD IDENTIFIER MODULE_PARAM_KEYWORD actual_param_list # call
         | list_command IDENTIFIER (LOP_RESET_IDX expression)? # listop
         | IDENTIFIER PRIMED? # var
         | str_literal # strlit
         |  NUMBER # nolit
        ;

actual_param_list: actual_param (COMMA actual_param)*;

actual_param: NUMBER | str_literal | IDENTIFIER;

list_command : LOP_NEXT | LOP_BACK | LOP_RESET | LOP_FIND;

str_literal : NULL_CHAR | NEWLINE_CHAR | WHITESPACE_CHAR | STRING;

bool_expr : BOP_NOT bool_expr # not
        | bool_expr BOP_AND bool_expr # and
        | bool_expr BOP_OR bool_expr # or
        | comparison # comp
        ;

comparison : expression (COMP_EQL | COMP_LT | COMP_LEQ | COMP_GT | COMP_GEQ) expression;