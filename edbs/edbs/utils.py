from pathlib import Path
from antlr4 import FileStream, CommonTokenStream
from edbs.parser.EDBSParser import EDBSParser
from edbs.parser.EDBSLexer import EDBSLexer
from edbs.parser.EDBSVisitor import EDBSVisitor


class CollectActualParams(EDBSVisitor):

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.values = []
        self.types = []

    def visitActual_param_list(self, ctx:EDBSParser.Actual_param_listContext):
        for p in ctx.getChildren():
            self.visit(p)


    def visitActual_param(self, ctx:EDBSParser.Actual_paramContext):
        if ctx.IDENTIFIER() is not None:
            var_name = str(ctx.IDENTIFIER())
            var = self.symbol_table.get_var(var_name, ctx.start.line, ctx.start.column)
            self.values.append(var.value)
            self.types.append(var.admissible_types)
        elif ctx.NUMBER():
            self.values.append(float(str(ctx.NUMBER()).replace(".","").replace(",",".")))
            self.types.append({'tal'})
        else:
            self.values.append(self.visit(ctx.str_literal()))
            self.types.append({'streng'})

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        if ctx.STRING() is not None:
            return str(ctx.STRING())[1:-1]
        elif ctx.NEWLINE_CHAR():
            return '\n'
        elif ctx.WHITESPACE_CHAR():
            return ' '
        elif ctx.NULL_CHAR():
            return None


def parse(file: Path) -> EDBSParser.ProgramContext:
    input_stream = FileStream(file, encoding="utf-8")
    lexer = EDBSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EDBSParser(token_stream)
    return parser.program()

