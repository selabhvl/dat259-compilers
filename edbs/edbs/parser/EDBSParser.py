# Generated from /Users/past-madm/Projects/teaching/dat259/dat259-compilers/edbs/EDBS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,244,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,5,0,40,8,
        0,10,0,12,0,43,9,0,1,0,1,0,3,0,47,8,0,1,1,1,1,1,1,1,1,3,1,53,8,1,
        1,1,1,1,3,1,57,8,1,1,1,1,1,3,1,61,8,1,1,1,1,1,1,1,3,1,66,8,1,1,1,
        1,1,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,4,
        4,84,8,4,11,4,12,4,85,1,5,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,1,
        6,1,6,1,6,1,6,1,7,1,7,3,7,102,8,7,1,7,1,7,1,7,3,7,107,8,7,1,7,5,
        7,110,8,7,10,7,12,7,113,9,7,1,7,3,7,116,8,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,3,7,129,8,7,1,7,1,7,4,7,133,8,7,11,7,12,
        7,134,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,147,8,7,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,164,8,
        9,1,9,1,9,3,9,168,8,9,1,9,1,9,3,9,172,8,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,201,8,9,10,9,12,9,204,9,9,1,10,1,10,1,
        10,5,10,209,8,10,10,10,12,10,212,9,10,1,11,1,11,1,11,3,11,217,8,
        11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,3,14,227,8,14,1,14,1,
        14,1,14,1,14,1,14,1,14,5,14,235,8,14,10,14,12,14,238,9,14,1,15,1,
        15,1,15,1,15,1,15,0,2,18,28,16,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,0,4,1,0,51,52,1,0,42,45,2,0,47,49,52,52,1,0,28,32,271,0,
        35,1,0,0,0,2,48,1,0,0,0,4,74,1,0,0,0,6,78,1,0,0,0,8,83,1,0,0,0,10,
        87,1,0,0,0,12,95,1,0,0,0,14,146,1,0,0,0,16,148,1,0,0,0,18,171,1,
        0,0,0,20,205,1,0,0,0,22,216,1,0,0,0,24,218,1,0,0,0,26,220,1,0,0,
        0,28,226,1,0,0,0,30,239,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,41,1,0,0,0,37,35,1,0,0,0,
        38,40,3,12,6,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,
        0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,46,5,3,0,0,45,47,5,54,0,0,46,
        45,1,0,0,0,46,47,1,0,0,0,47,1,1,0,0,0,48,49,5,14,0,0,49,50,5,51,
        0,0,50,52,5,15,0,0,51,53,5,54,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,
        54,1,0,0,0,54,56,3,4,2,0,55,57,5,54,0,0,56,55,1,0,0,0,56,57,1,0,
        0,0,57,58,1,0,0,0,58,60,3,6,3,0,59,61,5,54,0,0,60,59,1,0,0,0,60,
        61,1,0,0,0,61,62,1,0,0,0,62,63,5,18,0,0,63,65,5,5,0,0,64,66,5,54,
        0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,3,8,4,0,68,69,
        5,19,0,0,69,70,5,20,0,0,70,72,5,4,0,0,71,73,5,54,0,0,72,71,1,0,0,
        0,72,73,1,0,0,0,73,3,1,0,0,0,74,75,5,16,0,0,75,76,5,5,0,0,76,77,
        3,10,5,0,77,5,1,0,0,0,78,79,5,17,0,0,79,80,5,5,0,0,80,81,5,51,0,
        0,81,7,1,0,0,0,82,84,3,12,6,0,83,82,1,0,0,0,84,85,1,0,0,0,85,83,
        1,0,0,0,85,86,1,0,0,0,86,9,1,0,0,0,87,92,5,51,0,0,88,89,5,6,0,0,
        89,91,5,51,0,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,
        0,0,0,93,11,1,0,0,0,94,92,1,0,0,0,95,96,3,14,7,0,96,97,5,4,0,0,97,
        98,5,54,0,0,98,13,1,0,0,0,99,101,5,11,0,0,100,102,5,54,0,0,101,100,
        1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,111,3,14,7,0,104,106,
        5,6,0,0,105,107,5,54,0,0,106,105,1,0,0,0,106,107,1,0,0,0,107,108,
        1,0,0,0,108,110,3,14,7,0,109,104,1,0,0,0,110,113,1,0,0,0,111,109,
        1,0,0,0,111,112,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,114,116,
        5,54,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,
        5,12,0,0,118,119,3,28,14,0,119,147,1,0,0,0,120,121,5,9,0,0,121,122,
        5,51,0,0,122,123,5,5,0,0,123,147,5,52,0,0,124,125,5,9,0,0,125,126,
        5,22,0,0,126,128,5,51,0,0,127,129,5,52,0,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,147,1,0,0,0,130,132,5,8,0,0,131,133,3,16,8,0,132,131,
        1,0,0,0,133,134,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,147,
        1,0,0,0,136,137,5,10,0,0,137,138,5,51,0,0,138,139,5,5,0,0,139,147,
        3,18,9,0,140,141,5,13,0,0,141,142,5,51,0,0,142,143,5,5,0,0,143,147,
        3,18,9,0,144,145,5,19,0,0,145,147,5,24,0,0,146,99,1,0,0,0,146,120,
        1,0,0,0,146,124,1,0,0,0,146,130,1,0,0,0,146,136,1,0,0,0,146,140,
        1,0,0,0,146,144,1,0,0,0,147,15,1,0,0,0,148,149,7,0,0,0,149,17,1,
        0,0,0,150,151,6,9,-1,0,151,152,5,1,0,0,152,153,3,18,9,0,153,154,
        5,2,0,0,154,172,1,0,0,0,155,156,5,21,0,0,156,157,5,51,0,0,157,158,
        5,15,0,0,158,172,3,20,10,0,159,160,3,24,12,0,160,163,5,51,0,0,161,
        162,5,46,0,0,162,164,3,18,9,0,163,161,1,0,0,0,163,164,1,0,0,0,164,
        172,1,0,0,0,165,167,5,51,0,0,166,168,5,7,0,0,167,166,1,0,0,0,167,
        168,1,0,0,0,168,172,1,0,0,0,169,172,3,26,13,0,170,172,5,50,0,0,171,
        150,1,0,0,0,171,155,1,0,0,0,171,159,1,0,0,0,171,165,1,0,0,0,171,
        169,1,0,0,0,171,170,1,0,0,0,172,202,1,0,0,0,173,174,10,15,0,0,174,
        175,5,37,0,0,175,201,3,18,9,16,176,177,10,14,0,0,177,178,5,35,0,
        0,178,201,3,18,9,15,179,180,10,13,0,0,180,181,5,39,0,0,181,201,3,
        18,9,14,182,183,10,12,0,0,183,184,5,36,0,0,184,201,3,18,9,13,185,
        186,10,11,0,0,186,187,5,40,0,0,187,201,3,18,9,12,188,189,10,10,0,
        0,189,190,5,33,0,0,190,201,3,18,9,11,191,192,10,9,0,0,192,193,5,
        38,0,0,193,201,3,18,9,10,194,195,10,8,0,0,195,196,5,34,0,0,196,201,
        3,18,9,9,197,198,10,7,0,0,198,199,5,41,0,0,199,201,3,18,9,8,200,
        173,1,0,0,0,200,176,1,0,0,0,200,179,1,0,0,0,200,182,1,0,0,0,200,
        185,1,0,0,0,200,188,1,0,0,0,200,191,1,0,0,0,200,194,1,0,0,0,200,
        197,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,
        19,1,0,0,0,204,202,1,0,0,0,205,210,3,22,11,0,206,207,5,6,0,0,207,
        209,3,22,11,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,
        211,1,0,0,0,211,21,1,0,0,0,212,210,1,0,0,0,213,217,5,50,0,0,214,
        217,3,26,13,0,215,217,5,51,0,0,216,213,1,0,0,0,216,214,1,0,0,0,216,
        215,1,0,0,0,217,23,1,0,0,0,218,219,7,1,0,0,219,25,1,0,0,0,220,221,
        7,2,0,0,221,27,1,0,0,0,222,223,6,14,-1,0,223,224,5,25,0,0,224,227,
        3,28,14,4,225,227,3,30,15,0,226,222,1,0,0,0,226,225,1,0,0,0,227,
        236,1,0,0,0,228,229,10,3,0,0,229,230,5,26,0,0,230,235,3,28,14,4,
        231,232,10,2,0,0,232,233,5,27,0,0,233,235,3,28,14,3,234,228,1,0,
        0,0,234,231,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,
        0,0,237,29,1,0,0,0,238,236,1,0,0,0,239,240,3,18,9,0,240,241,7,3,
        0,0,241,242,3,18,9,0,242,31,1,0,0,0,27,35,41,46,52,56,60,65,72,85,
        92,101,106,111,115,128,134,146,163,167,171,200,202,210,216,226,234,
        236
    ]

class EDBSParser ( Parser ):

    grammarFileName = "EDBS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'FERDIG.'", "'.'", "':'", 
                     "','", "'''", "'SKRIV'", "'LES'", "'REKN'", "'GJENTAR'", 
                     "'MEDAN'", "'OPPDATER'", "'DEFINER EIT MODUL'", "'MED'", 
                     "'INN'", "'UT'", "'SOM'", "'AVSLUT'", "'MODUL'", "'KALL'", 
                     "'FIL'", "'i'", "'!'", "'IKKJE'", "'OG'", "'ELLER'", 
                     "'='", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'^'", "'++'", "'**'", "'//'", "'--'", 
                     "'neste'", "'finn'", "'f\\u00F8rre'", "'tilbakestill'", 
                     "'til'", "'<tom>'", "'<linjeskift>'", "'<tomrom>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "FINISH_KEYWORD", 
                      "PERIOD", "COLON", "COMMA", "PRIMED", "WRITE_KEYWORD", 
                      "READ_KEYWORD", "CALC_KEYWORD", "REPEAT_KEYWORD", 
                      "CONDITION_KEYWORD", "UPDATE_KEYWORD", "DEFINE_MOULE_KEYWORD", 
                      "MODULE_PARAM_KEYWORD", "INPUT_PARAM_KEYWORD", "OUTPUT_PARAM_KEYWORD", 
                      "MODULE_BODY_KEYWORD", "EXIT_KEYWORD", "MODULE_KEYWORD", 
                      "CALL_MODULE_KEYWORD", "FILE_KEYWORD", "IN_KEYWORD", 
                      "EXCLAMATION", "BOP_NOT", "BOP_AND", "BOP_OR", "COMP_EQL", 
                      "COMP_LT", "COMP_LEQ", "COMP_GT", "COMP_GEQ", "OP_ADD", 
                      "OP_SUB", "OP_MUL", "OP_DIV", "OP_EXP", "SOP_CONCAT", 
                      "SOP_REPEAT", "SOP_SPLIT", "SOP_SUBSTR", "LOP_NEXT", 
                      "LOP_FIND", "LOP_BACK", "LOP_RESET", "LOP_RESET_IDX", 
                      "NULL_CHAR", "NEWLINE_CHAR", "WHITESPACE_CHAR", "NUMBER", 
                      "IDENTIFIER", "STRING", "COMMENT", "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_module_def = 1
    RULE_input_params = 2
    RULE_output_params = 3
    RULE_module_body = 4
    RULE_param_list = 5
    RULE_main_statement = 6
    RULE_stmt = 7
    RULE_write_arg = 8
    RULE_expression = 9
    RULE_actual_param_list = 10
    RULE_actual_param = 11
    RULE_list_command = 12
    RULE_str_literal = 13
    RULE_bool_expr = 14
    RULE_comparison = 15

    ruleNames =  [ "program", "module_def", "input_params", "output_params", 
                   "module_body", "param_list", "main_statement", "stmt", 
                   "write_arg", "expression", "actual_param_list", "actual_param", 
                   "list_command", "str_literal", "bool_expr", "comparison" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    FINISH_KEYWORD=3
    PERIOD=4
    COLON=5
    COMMA=6
    PRIMED=7
    WRITE_KEYWORD=8
    READ_KEYWORD=9
    CALC_KEYWORD=10
    REPEAT_KEYWORD=11
    CONDITION_KEYWORD=12
    UPDATE_KEYWORD=13
    DEFINE_MOULE_KEYWORD=14
    MODULE_PARAM_KEYWORD=15
    INPUT_PARAM_KEYWORD=16
    OUTPUT_PARAM_KEYWORD=17
    MODULE_BODY_KEYWORD=18
    EXIT_KEYWORD=19
    MODULE_KEYWORD=20
    CALL_MODULE_KEYWORD=21
    FILE_KEYWORD=22
    IN_KEYWORD=23
    EXCLAMATION=24
    BOP_NOT=25
    BOP_AND=26
    BOP_OR=27
    COMP_EQL=28
    COMP_LT=29
    COMP_LEQ=30
    COMP_GT=31
    COMP_GEQ=32
    OP_ADD=33
    OP_SUB=34
    OP_MUL=35
    OP_DIV=36
    OP_EXP=37
    SOP_CONCAT=38
    SOP_REPEAT=39
    SOP_SPLIT=40
    SOP_SUBSTR=41
    LOP_NEXT=42
    LOP_FIND=43
    LOP_BACK=44
    LOP_RESET=45
    LOP_RESET_IDX=46
    NULL_CHAR=47
    NEWLINE_CHAR=48
    WHITESPACE_CHAR=49
    NUMBER=50
    IDENTIFIER=51
    STRING=52
    COMMENT=53
    NEWLINE=54
    WHITESPACE=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINISH_KEYWORD(self):
            return self.getToken(EDBSParser.FINISH_KEYWORD, 0)

        def module_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Module_defContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Module_defContext,i)


        def main_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Main_statementContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Main_statementContext,i)


        def NEWLINE(self):
            return self.getToken(EDBSParser.NEWLINE, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EDBSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 32
                self.module_def()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536320) != 0):
                self.state = 38
                self.main_statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(EDBSParser.FINISH_KEYWORD)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 45
                self.match(EDBSParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE_MOULE_KEYWORD(self):
            return self.getToken(EDBSParser.DEFINE_MOULE_KEYWORD, 0)

        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)

        def MODULE_PARAM_KEYWORD(self):
            return self.getToken(EDBSParser.MODULE_PARAM_KEYWORD, 0)

        def input_params(self):
            return self.getTypedRuleContext(EDBSParser.Input_paramsContext,0)


        def output_params(self):
            return self.getTypedRuleContext(EDBSParser.Output_paramsContext,0)


        def MODULE_BODY_KEYWORD(self):
            return self.getToken(EDBSParser.MODULE_BODY_KEYWORD, 0)

        def COLON(self):
            return self.getToken(EDBSParser.COLON, 0)

        def module_body(self):
            return self.getTypedRuleContext(EDBSParser.Module_bodyContext,0)


        def EXIT_KEYWORD(self):
            return self.getToken(EDBSParser.EXIT_KEYWORD, 0)

        def MODULE_KEYWORD(self):
            return self.getToken(EDBSParser.MODULE_KEYWORD, 0)

        def PERIOD(self):
            return self.getToken(EDBSParser.PERIOD, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(EDBSParser.NEWLINE)
            else:
                return self.getToken(EDBSParser.NEWLINE, i)

        def getRuleIndex(self):
            return EDBSParser.RULE_module_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_def" ):
                return visitor.visitModule_def(self)
            else:
                return visitor.visitChildren(self)




    def module_def(self):

        localctx = EDBSParser.Module_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_module_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(EDBSParser.DEFINE_MOULE_KEYWORD)
            self.state = 49
            self.match(EDBSParser.IDENTIFIER)
            self.state = 50
            self.match(EDBSParser.MODULE_PARAM_KEYWORD)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 51
                self.match(EDBSParser.NEWLINE)


            self.state = 54
            self.input_params()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 55
                self.match(EDBSParser.NEWLINE)


            self.state = 58
            self.output_params()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 59
                self.match(EDBSParser.NEWLINE)


            self.state = 62
            self.match(EDBSParser.MODULE_BODY_KEYWORD)
            self.state = 63
            self.match(EDBSParser.COLON)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 64
                self.match(EDBSParser.NEWLINE)


            self.state = 67
            self.module_body()
            self.state = 68
            self.match(EDBSParser.EXIT_KEYWORD)
            self.state = 69
            self.match(EDBSParser.MODULE_KEYWORD)
            self.state = 70
            self.match(EDBSParser.PERIOD)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 71
                self.match(EDBSParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT_PARAM_KEYWORD(self):
            return self.getToken(EDBSParser.INPUT_PARAM_KEYWORD, 0)

        def COLON(self):
            return self.getToken(EDBSParser.COLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(EDBSParser.Param_listContext,0)


        def getRuleIndex(self):
            return EDBSParser.RULE_input_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_params" ):
                return visitor.visitInput_params(self)
            else:
                return visitor.visitChildren(self)




    def input_params(self):

        localctx = EDBSParser.Input_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_input_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EDBSParser.INPUT_PARAM_KEYWORD)
            self.state = 75
            self.match(EDBSParser.COLON)
            self.state = 76
            self.param_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT_PARAM_KEYWORD(self):
            return self.getToken(EDBSParser.OUTPUT_PARAM_KEYWORD, 0)

        def COLON(self):
            return self.getToken(EDBSParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_output_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_params" ):
                return visitor.visitOutput_params(self)
            else:
                return visitor.visitChildren(self)




    def output_params(self):

        localctx = EDBSParser.Output_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_output_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(EDBSParser.OUTPUT_PARAM_KEYWORD)
            self.state = 79
            self.match(EDBSParser.COLON)
            self.state = 80
            self.match(EDBSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Main_statementContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Main_statementContext,i)


        def getRuleIndex(self):
            return EDBSParser.RULE_module_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_body" ):
                return visitor.visitModule_body(self)
            else:
                return visitor.visitChildren(self)




    def module_body(self):

        localctx = EDBSParser.Module_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_module_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 82
                    self.main_statement()

                else:
                    raise NoViableAltException(self)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(EDBSParser.IDENTIFIER)
            else:
                return self.getToken(EDBSParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EDBSParser.COMMA)
            else:
                return self.getToken(EDBSParser.COMMA, i)

        def getRuleIndex(self):
            return EDBSParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = EDBSParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(EDBSParser.IDENTIFIER)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 88
                self.match(EDBSParser.COMMA)
                self.state = 89
                self.match(EDBSParser.IDENTIFIER)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(EDBSParser.StmtContext,0)


        def PERIOD(self):
            return self.getToken(EDBSParser.PERIOD, 0)

        def NEWLINE(self):
            return self.getToken(EDBSParser.NEWLINE, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_main_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_statement" ):
                return visitor.visitMain_statement(self)
            else:
                return visitor.visitChildren(self)




    def main_statement(self):

        localctx = EDBSParser.Main_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_main_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.stmt()
            self.state = 96
            self.match(EDBSParser.PERIOD)
            self.state = 97
            self.match(EDBSParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EDBSParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadfileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ_KEYWORD(self):
            return self.getToken(EDBSParser.READ_KEYWORD, 0)
        def FILE_KEYWORD(self):
            return self.getToken(EDBSParser.FILE_KEYWORD, 0)
        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def STRING(self):
            return self.getToken(EDBSParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadfile" ):
                return visitor.visitReadfile(self)
            else:
                return visitor.visitChildren(self)


    class MutateContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UPDATE_KEYWORD(self):
            return self.getToken(EDBSParser.UPDATE_KEYWORD, 0)
        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def COLON(self):
            return self.getToken(EDBSParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EDBSParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutate" ):
                return visitor.visitMutate(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ_KEYWORD(self):
            return self.getToken(EDBSParser.READ_KEYWORD, 0)
        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def COLON(self):
            return self.getToken(EDBSParser.COLON, 0)
        def STRING(self):
            return self.getToken(EDBSParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class CalcContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CALC_KEYWORD(self):
            return self.getToken(EDBSParser.CALC_KEYWORD, 0)
        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def COLON(self):
            return self.getToken(EDBSParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EDBSParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc" ):
                return visitor.visitCalc(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REPEAT_KEYWORD(self):
            return self.getToken(EDBSParser.REPEAT_KEYWORD, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.StmtContext)
            else:
                return self.getTypedRuleContext(EDBSParser.StmtContext,i)

        def CONDITION_KEYWORD(self):
            return self.getToken(EDBSParser.CONDITION_KEYWORD, 0)
        def bool_expr(self):
            return self.getTypedRuleContext(EDBSParser.Bool_exprContext,0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(EDBSParser.NEWLINE)
            else:
                return self.getToken(EDBSParser.NEWLINE, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EDBSParser.COMMA)
            else:
                return self.getToken(EDBSParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE_KEYWORD(self):
            return self.getToken(EDBSParser.WRITE_KEYWORD, 0)
        def write_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Write_argContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Write_argContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXIT_KEYWORD(self):
            return self.getToken(EDBSParser.EXIT_KEYWORD, 0)
        def EXCLAMATION(self):
            return self.getToken(EDBSParser.EXCLAMATION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = EDBSParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = EDBSParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(EDBSParser.REPEAT_KEYWORD)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==54:
                    self.state = 100
                    self.match(EDBSParser.NEWLINE)


                self.state = 103
                self.stmt()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 104
                    self.match(EDBSParser.COMMA)
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==54:
                        self.state = 105
                        self.match(EDBSParser.NEWLINE)


                    self.state = 108
                    self.stmt()
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==54:
                    self.state = 114
                    self.match(EDBSParser.NEWLINE)


                self.state = 117
                self.match(EDBSParser.CONDITION_KEYWORD)
                self.state = 118
                self.bool_expr(0)
                pass

            elif la_ == 2:
                localctx = EDBSParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(EDBSParser.READ_KEYWORD)
                self.state = 121
                self.match(EDBSParser.IDENTIFIER)
                self.state = 122
                self.match(EDBSParser.COLON)
                self.state = 123
                self.match(EDBSParser.STRING)
                pass

            elif la_ == 3:
                localctx = EDBSParser.ReadfileContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(EDBSParser.READ_KEYWORD)
                self.state = 125
                self.match(EDBSParser.FILE_KEYWORD)
                self.state = 126
                self.match(EDBSParser.IDENTIFIER)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 127
                    self.match(EDBSParser.STRING)


                pass

            elif la_ == 4:
                localctx = EDBSParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.match(EDBSParser.WRITE_KEYWORD)
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 131
                    self.write_arg()
                    self.state = 134 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==51 or _la==52):
                        break

                pass

            elif la_ == 5:
                localctx = EDBSParser.CalcContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.match(EDBSParser.CALC_KEYWORD)
                self.state = 137
                self.match(EDBSParser.IDENTIFIER)
                self.state = 138
                self.match(EDBSParser.COLON)
                self.state = 139
                self.expression(0)
                pass

            elif la_ == 6:
                localctx = EDBSParser.MutateContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.match(EDBSParser.UPDATE_KEYWORD)
                self.state = 141
                self.match(EDBSParser.IDENTIFIER)
                self.state = 142
                self.match(EDBSParser.COLON)
                self.state = 143
                self.expression(0)
                pass

            elif la_ == 7:
                localctx = EDBSParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.match(EDBSParser.EXIT_KEYWORD)
                self.state = 145
                self.match(EDBSParser.EXCLAMATION)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EDBSParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_write_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_arg" ):
                return visitor.visitWrite_arg(self)
            else:
                return visitor.visitChildren(self)




    def write_arg(self):

        localctx = EDBSParser.Write_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_write_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==51 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EDBSParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def OP_ADD(self):
            return self.getToken(EDBSParser.OP_ADD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def OP_SUB(self):
            return self.getToken(EDBSParser.OP_SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def OP_MUL(self):
            return self.getToken(EDBSParser.OP_MUL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def PRIMED(self):
            return self.getToken(EDBSParser.PRIMED, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ConcatContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def SOP_CONCAT(self):
            return self.getToken(EDBSParser.SOP_CONCAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)


    class NestedContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EDBSParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested" ):
                return visitor.visitNested(self)
            else:
                return visitor.visitChildren(self)


    class SubstrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def SOP_SUBSTR(self):
            return self.getToken(EDBSParser.SOP_SUBSTR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstr" ):
                return visitor.visitSubstr(self)
            else:
                return visitor.visitChildren(self)


    class CallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CALL_MODULE_KEYWORD(self):
            return self.getToken(EDBSParser.CALL_MODULE_KEYWORD, 0)
        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def MODULE_PARAM_KEYWORD(self):
            return self.getToken(EDBSParser.MODULE_PARAM_KEYWORD, 0)
        def actual_param_list(self):
            return self.getTypedRuleContext(EDBSParser.Actual_param_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class DivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def OP_DIV(self):
            return self.getToken(EDBSParser.OP_DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class StrlitContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def str_literal(self):
            return self.getTypedRuleContext(EDBSParser.Str_literalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrlit" ):
                return visitor.visitStrlit(self)
            else:
                return visitor.visitChildren(self)


    class SplitContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def SOP_SPLIT(self):
            return self.getToken(EDBSParser.SOP_SPLIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplit" ):
                return visitor.visitSplit(self)
            else:
                return visitor.visitChildren(self)


    class NolitContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(EDBSParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNolit" ):
                return visitor.visitNolit(self)
            else:
                return visitor.visitChildren(self)


    class ListopContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_command(self):
            return self.getTypedRuleContext(EDBSParser.List_commandContext,0)

        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)
        def LOP_RESET_IDX(self):
            return self.getToken(EDBSParser.LOP_RESET_IDX, 0)
        def expression(self):
            return self.getTypedRuleContext(EDBSParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListop" ):
                return visitor.visitListop(self)
            else:
                return visitor.visitChildren(self)


    class RepeatContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def SOP_REPEAT(self):
            return self.getToken(EDBSParser.SOP_REPEAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)


    class ExpoContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)

        def OP_EXP(self):
            return self.getToken(EDBSParser.OP_EXP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpo" ):
                return visitor.visitExpo(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EDBSParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = EDBSParser.NestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 151
                self.match(EDBSParser.T__0)
                self.state = 152
                self.expression(0)
                self.state = 153
                self.match(EDBSParser.T__1)
                pass
            elif token in [21]:
                localctx = EDBSParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(EDBSParser.CALL_MODULE_KEYWORD)
                self.state = 156
                self.match(EDBSParser.IDENTIFIER)
                self.state = 157
                self.match(EDBSParser.MODULE_PARAM_KEYWORD)
                self.state = 158
                self.actual_param_list()
                pass
            elif token in [42, 43, 44, 45]:
                localctx = EDBSParser.ListopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.list_command()
                self.state = 160
                self.match(EDBSParser.IDENTIFIER)
                self.state = 163
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 161
                    self.match(EDBSParser.LOP_RESET_IDX)
                    self.state = 162
                    self.expression(0)


                pass
            elif token in [51]:
                localctx = EDBSParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 165
                self.match(EDBSParser.IDENTIFIER)
                self.state = 167
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 166
                    self.match(EDBSParser.PRIMED)


                pass
            elif token in [47, 48, 49, 52]:
                localctx = EDBSParser.StrlitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 169
                self.str_literal()
                pass
            elif token in [50]:
                localctx = EDBSParser.NolitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.match(EDBSParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 200
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = EDBSParser.ExpoContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 174
                        self.match(EDBSParser.OP_EXP)
                        self.state = 175
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = EDBSParser.MulContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 177
                        self.match(EDBSParser.OP_MUL)
                        self.state = 178
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = EDBSParser.RepeatContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 180
                        self.match(EDBSParser.SOP_REPEAT)
                        self.state = 181
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = EDBSParser.DivContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 183
                        self.match(EDBSParser.OP_DIV)
                        self.state = 184
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = EDBSParser.SplitContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 186
                        self.match(EDBSParser.SOP_SPLIT)
                        self.state = 187
                        self.expression(12)
                        pass

                    elif la_ == 6:
                        localctx = EDBSParser.AddContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 189
                        self.match(EDBSParser.OP_ADD)
                        self.state = 190
                        self.expression(11)
                        pass

                    elif la_ == 7:
                        localctx = EDBSParser.ConcatContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 192
                        self.match(EDBSParser.SOP_CONCAT)
                        self.state = 193
                        self.expression(10)
                        pass

                    elif la_ == 8:
                        localctx = EDBSParser.SubContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 195
                        self.match(EDBSParser.OP_SUB)
                        self.state = 196
                        self.expression(9)
                        pass

                    elif la_ == 9:
                        localctx = EDBSParser.SubstrContext(self, EDBSParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 197
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 198
                        self.match(EDBSParser.SOP_SUBSTR)
                        self.state = 199
                        self.expression(8)
                        pass

             
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Actual_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actual_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Actual_paramContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Actual_paramContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EDBSParser.COMMA)
            else:
                return self.getToken(EDBSParser.COMMA, i)

        def getRuleIndex(self):
            return EDBSParser.RULE_actual_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_param_list" ):
                return visitor.visitActual_param_list(self)
            else:
                return visitor.visitChildren(self)




    def actual_param_list(self):

        localctx = EDBSParser.Actual_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_actual_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.actual_param()
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self.match(EDBSParser.COMMA)
                    self.state = 207
                    self.actual_param() 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Actual_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(EDBSParser.NUMBER, 0)

        def str_literal(self):
            return self.getTypedRuleContext(EDBSParser.Str_literalContext,0)


        def IDENTIFIER(self):
            return self.getToken(EDBSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_actual_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_param" ):
                return visitor.visitActual_param(self)
            else:
                return visitor.visitChildren(self)




    def actual_param(self):

        localctx = EDBSParser.Actual_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_actual_param)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(EDBSParser.NUMBER)
                pass
            elif token in [47, 48, 49, 52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.str_literal()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.match(EDBSParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOP_NEXT(self):
            return self.getToken(EDBSParser.LOP_NEXT, 0)

        def LOP_BACK(self):
            return self.getToken(EDBSParser.LOP_BACK, 0)

        def LOP_RESET(self):
            return self.getToken(EDBSParser.LOP_RESET, 0)

        def LOP_FIND(self):
            return self.getToken(EDBSParser.LOP_FIND, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_list_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_command" ):
                return visitor.visitList_command(self)
            else:
                return visitor.visitChildren(self)




    def list_command(self):

        localctx = EDBSParser.List_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65970697666560) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_CHAR(self):
            return self.getToken(EDBSParser.NULL_CHAR, 0)

        def NEWLINE_CHAR(self):
            return self.getToken(EDBSParser.NEWLINE_CHAR, 0)

        def WHITESPACE_CHAR(self):
            return self.getToken(EDBSParser.WHITESPACE_CHAR, 0)

        def STRING(self):
            return self.getToken(EDBSParser.STRING, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_str_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_literal" ):
                return visitor.visitStr_literal(self)
            else:
                return visitor.visitChildren(self)




    def str_literal(self):

        localctx = EDBSParser.Str_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_str_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5488762045857792) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EDBSParser.RULE_bool_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompContext(Bool_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.Bool_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparison(self):
            return self.getTypedRuleContext(EDBSParser.ComparisonContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(Bool_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.Bool_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOP_NOT(self):
            return self.getToken(EDBSParser.BOP_NOT, 0)
        def bool_expr(self):
            return self.getTypedRuleContext(EDBSParser.Bool_exprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(Bool_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.Bool_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Bool_exprContext,i)

        def BOP_OR(self):
            return self.getToken(EDBSParser.BOP_OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(Bool_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EDBSParser.Bool_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(EDBSParser.Bool_exprContext,i)

        def BOP_AND(self):
            return self.getToken(EDBSParser.BOP_AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)



    def bool_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EDBSParser.Bool_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_bool_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = EDBSParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 223
                self.match(EDBSParser.BOP_NOT)
                self.state = 224
                self.bool_expr(4)
                pass
            elif token in [1, 21, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52]:
                localctx = EDBSParser.CompContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 225
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 234
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = EDBSParser.AndContext(self, EDBSParser.Bool_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 228
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 229
                        self.match(EDBSParser.BOP_AND)
                        self.state = 230
                        self.bool_expr(4)
                        pass

                    elif la_ == 2:
                        localctx = EDBSParser.OrContext(self, EDBSParser.Bool_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 231
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 232
                        self.match(EDBSParser.BOP_OR)
                        self.state = 233
                        self.bool_expr(3)
                        pass

             
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EDBSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EDBSParser.ExpressionContext,i)


        def COMP_EQL(self):
            return self.getToken(EDBSParser.COMP_EQL, 0)

        def COMP_LT(self):
            return self.getToken(EDBSParser.COMP_LT, 0)

        def COMP_LEQ(self):
            return self.getToken(EDBSParser.COMP_LEQ, 0)

        def COMP_GT(self):
            return self.getToken(EDBSParser.COMP_GT, 0)

        def COMP_GEQ(self):
            return self.getToken(EDBSParser.COMP_GEQ, 0)

        def getRuleIndex(self):
            return EDBSParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = EDBSParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.expression(0)
            self.state = 240
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 241
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        self._predicates[14] = self.bool_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

    def bool_expr_sempred(self, localctx:Bool_exprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




