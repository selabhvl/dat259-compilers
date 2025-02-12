import sys
from antlr4 import *
from edbs.EDBSParser import EDBSParser
from edbs.EDBSLexer import EDBSLexer
from edbs.EDBSVisitor import EDBSVisitor


class SymbolTable:

    def __init__(self):
        self.storage = {}

    def add_var(self, name: str, value: float):
        self.storage[name] = value

    def get_var(self, name: str):
        if name not in self.storage:
            raise KeyError(f"Variable {name} not found!!")
        return self.storage[name]

class InterpreterVisitor(EDBSVisitor):

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table


    def visitWrite_arg(self, ctx:EDBSParser.Write_argContext):
        if ctx.IDENTIFIER() is not None:
            name = str(ctx.IDENTIFIER())
            value = self.symbol_table.get_var(name)
            print(str(value), end=" ")
        elif ctx.STRING():
            string_token = ctx.STRING()
            print(str(string_token)[1:-1], end=" ")

    def visitWrite_stmt(self, ctx:EDBSParser.Write_stmtContext):
        for c in ctx.children:
            self.visit(c)
        print()

    def visitRead_assgn(self, ctx:EDBSParser.Read_assgnContext):
        prompt = str(ctx.STRING())[1:-1]
        value = float(input(f"{prompt}: "))
        name = str(ctx.IDENTIFIER())
        self.symbol_table.add_var(name, value)

    def visitCalc_stmt(self, ctx:EDBSParser.Calc_stmtContext):
        name = str(ctx.IDENTIFIER())
        value = self.visit(ctx.expression())
        self.symbol_table.add_var(name, value)

    def visitLit(self, ctx:EDBSParser.LitContext):
        value =  float(str(ctx.NUMBER()).replace(",", '.'))
        return value

    def visitVar(self, ctx:EDBSParser.VarContext):
        name = str(ctx.IDENTIFIER())
        value = self.symbol_table.get_var(name)
        return value

    def visitAdd(self, ctx:EDBSParser.AddContext):
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(2))

    def visitDiv(self, ctx:EDBSParser.DivContext):
        return self.visit(ctx.getChild(0)) / self.visit(ctx.getChild(2))

    def visitMul(self, ctx:EDBSParser.MulContext):
        return self.visit(ctx.getChild(0)) * self.visit(ctx.getChild(2))

    def visitSub(self, ctx:EDBSParser.SubContext):
        return self.visit(ctx.getChild(0)) - self.visit(ctx.getChild(2))

    def visitExpo(self, ctx:EDBSParser.ExpoContext):
        return self.visit(ctx.getChild(0)) ** self.visit(ctx.getChild(2))

    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visit(ctx.expression())


def main():

    input_stream = FileStream("./examples/uttrykk.edbs", encoding="utf-8")
    lexer = EDBSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EDBSParser(token_stream)
    tree = parser.program()
    table = SymbolTable()
    visitor = InterpreterVisitor(table)
    visitor.visit(tree)

if __name__ == '__main__':
    main()
