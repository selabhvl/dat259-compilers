import sys
from antlr4 import *
from edbs.EDBSParser import EDBSParser
from edbs.EDBSLexer import EDBSLexer
from edbs.EDBSVisitor import EDBSVisitor


class InterpreterVisitor(EDBSVisitor):


    def visitWrite_stmt(self, ctx: EDBSParser.Write_stmtContext):
        string_token = ctx.STRING()
        print(str(string_token)[1:-1])
    


def main():
    input_stream = FileStream("./examples/hello.edbs", encoding="utf-8")
    lexer = EDBSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EDBSParser(token_stream)
    tree = parser.program()
    visitor = InterpreterVisitor()

    visitor.visit(tree)

if __name__ == '__main__':
    main()
