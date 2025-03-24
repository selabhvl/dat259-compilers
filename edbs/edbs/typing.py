import sys

from edbs.parser.EDBSParser import  EDBSParser
from edbs.parser.EDBSVisitor import EDBSVisitor
from edbs.symbols import SymbolTable, EDBSException
from pathlib import Path
from edbs.utils import parse

class TypeChecker(EDBSVisitor):

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table
        # TODO: quick and dirty! This has to be a stack to make it properly!
        self.current_pushdown = set()

    def visitMutate(self, ctx:EDBSParser.MutateContext):
        name = str(ctx.IDENTIFIER())
        admissable_types = self.visit(ctx.expression())
        self.symbol_table.types[name] = admissable_types

    def visitCalc(self, ctx:EDBSParser.CalcContext):
        name = str(ctx.IDENTIFIER())
        admissable_types = self.visit(ctx.expression())
        self.symbol_table.types[name] = admissable_types

    def visitRead(self, ctx:EDBSParser.ReadContext):
        name = str(ctx.IDENTIFIER())
        self.symbol_table.register_var_name(name)

    def visitAdd(self, ctx:EDBSParser.AddContext):
        self.current_pushdown = {'tal'} # type inference goes down
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(2))
        return {'tal'} # type check goes up

    def visitDiv(self, ctx:EDBSParser.AddContext):
        self.current_pushdown = {'tal'} # type inference goes down
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(2))
        return {'tal'}  # type check goes up

    def visitMul(self, ctx:EDBSParser.AddContext):
        self.current_pushdown = {'tal'} # type inference goes down
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(2))
        return {'tal'}  # type check goes up

    def visitSub(self, ctx:EDBSParser.AddContext):
        self.current_pushdown = {'tal'} # type inference goes down
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(2))
        return {'tal'}  # type check goes up

    def visitVar(self, ctx:EDBSParser.VarContext):
        name = str(ctx.IDENTIFIER())
        result_types = self.current_pushdown.intersection(self.symbol_table.types[name])
        if len(result_types) == 0:
            raise UnsoundTypes(name, self.current_pushdown, self.symbol_table.types[name])
        else:
            self.symbol_table.types[name] = result_types
            return result_types

    def visitNolit(self, ctx:EDBSParser.NolitContext):
        return {'tal'}

    def visitStrlit(self, ctx:EDBSParser.StrlitContext):
        return {'streng'}

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        return  {'streng'}

    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visit(ctx.expression())

    # type judgement: streng, streng -> hugseliste
    def visitSplit(self, ctx:EDBSParser.SplitContext):
        self.current_pushdown = {'streng'}  # type inference goes down
        self.visit(ctx.getChild(0))
        self.current_pushdown = {'tal'}  # type inference goes down
        self.visit(ctx.getChild(2))
        return {'streng'} # type check goes up

    # type judgement: streng, streng -> hugseliste
    def visitSubstr(self, ctx:EDBSParser.SubstrContext):
        self.current_pushdown = {'streng'}  # type inference goes down
        self.visit(ctx.getChild(0))
        self.current_pushdown = {'tal'}  # type inference goes down
        self.visit(ctx.getChild(2))
        return {'hugseliste'}  # type check goes up

    def visitRepeat(self, ctx:EDBSParser.RepeatContext):
        self.current_pushdown = {'streng'}  # type inference goes down
        self.visit(ctx.getChild(0))
        self.current_pushdown = {'tal'}  # type inference goes down
        self.visit(ctx.getChild(2))
        return {'streng'}  # type check goes up

    def visitConcat(self, ctx:EDBSParser.ConcatContext):
        self.current_pushdown = {'streng'}  # type inference goes down
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(2))
        return {'streng'}  # type check goes up


    def visitCall(self, ctx:EDBSParser.CallContext):
        # TODO: challenge implement type inference med moduler!
        return {'streng', 'tal', 'hugseliste'}


    def visitListop(self, ctx:EDBSParser.ListopContext):
        return self.visit(ctx.list_command())

    def visitList_command(self, ctx:EDBSParser.List_commandContext):
        if ctx.LOP_NEXT():
            return {'tal', 'streng'}
        elif ctx.LOP_BACK():
            return {'tal', 'streng'}
        elif ctx.LOP_RESET():
            return set()
        elif ctx.LOP_FIND():
            return {'tal', 'streng'}

    def summarize_types(self):
        for var_name in self.symbol_table.types.keys():
            types = self.symbol_table.types[var_name]
            if len(types) == 1:
                print(f"{var_name} er {types.__iter__().__next__()}")
            else:
                print(f"Feil: {var_name} er uklart!")

def type_check(file: Path):
    print(f"Leser EDBS fil '{file.resolve()}'...", end="")
    ast = parse(file)
    print("OK")
    symbols = SymbolTable()
    checker = TypeChecker(symbols)
    try:
        print(f"Sjekker EDBS fil '{file.resolve()}'...", end="")
        checker.visit(ast)
        print("OK")
        checker.summarize_types()
    except EDBSException as e:
        print(e.msg)
        sys.exit(69)


def main():
    if len(sys.argv) >= 2:
        progname = sys.argv[1]
        progfile = Path.cwd() / progname
        type_check(progfile)
    else:
        print("Betjeningsfeil! Bruk: edbc <FILNAMN>")
        sys.exit(1)

if __name__ == "__main__":
    main()
