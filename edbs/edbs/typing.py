import sys

from edbs.parser.EDBSParser import  EDBSParser
from edbs.parser.EDBSVisitor import EDBSVisitor
from edbs.symbols import SymbolTable, EDBSException, Module
from pathlib import Path
from edbs.utils import parse, CollectActualParams

class EDBSTypeChecker(EDBSVisitor):

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table
        self.nested_scopes = []
        # TODO: quick and dirty! This has to be a stack to make it properly!
        self.current_pushdown = set()

    def visitMutate(self, ctx:EDBSParser.MutateContext):
        name = str(ctx.IDENTIFIER())
        admissable_types = self.visit(ctx.expression())
        self.symbol_table.mutate_var(name, line=ctx.start.line, col=ctx.start.column, typing=admissable_types)

    def visitCalc(self, ctx:EDBSParser.CalcContext):
        name = str(ctx.IDENTIFIER())
        admissable_types = self.visit(ctx.expression())
        self.symbol_table.add_var(name,  line=ctx.start.line, col=ctx.start.column).admissible_types = admissable_types

    def visitRead(self, ctx:EDBSParser.ReadContext):
        name = str(ctx.IDENTIFIER())
        self.symbol_table.add_var(name,  line=ctx.start.line, col=ctx.start.column).is_constant = False

    # type judgement for all arithmetic operations: tal, tal -> tal
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
        var = self.symbol_table.get_var(name, line=ctx.start.line, col=ctx.start.column)
        return var.narrow_and_type(self.current_pushdown,  line=ctx.start.line, col=ctx.start.column)

    def visitNolit(self, ctx:EDBSParser.NolitContext):
        return {'tal'}

    def visitStrlit(self, ctx:EDBSParser.StrlitContext):
        return {'streng'}

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        return  {'streng'}

    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visit(ctx.expression())

    # type judgement: tal, tal -> sannheit
    def visitComparison(self, ctx:EDBSParser.ComparisonContext):
        # type inference goes down
        self.current_pushdown = {'tal'}
        self.visit(ctx.getChild(0)) # lhs
        self.visit(ctx.getChild(ctx.getChildCount() - 1)) # rhs
        # bool is not a type that can be used in expressions, therefore no return



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

    def visitCall(self, ctx: EDBSParser.CallContext):
        name = str(ctx.IDENTIFIER())
        module = self.symbol_table.get_module(name,  line=ctx.start.line, col=ctx.start.column)

        # update module symbol table with actual param types
        collect_actuals = CollectActualParams(self.symbol_table)
        collect_actuals.visit(ctx.actual_param_list())
        for p, t in zip(module.formal_param_names, collect_actuals.types):
            module.symbols.get_var(p,  line=ctx.start.line, col=ctx.start.column).admissible_types = t

        # TODO: after the call it is possible to backpropagate the type information to the variables

        # call module with fresh interpreter
        module_typer = EDBSTypeChecker(module.symbols)
        module_typer.visit(module.body)

        # get result back
        result = module.symbols.get_var(module.result_param_name, col=ctx.start.column, line=ctx.start.line).admissible_types
        return result

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

    def visitWhile(self, ctx:EDBSParser.WhileContext):
        nested = SymbolTable(self.symbol_table)
        backup = self.symbol_table
        self.symbol_table = nested
        for c in ctx.children:
            self.visit(c)
        self.symbol_table = backup
        self.nested_scopes.append(nested)

    def visitOutput_params(self, ctx: EDBSParser.Output_paramsContext):
        return str(ctx.IDENTIFIER())

    def visitInput_params(self, ctx: EDBSParser.Input_paramsContext):
        return self.visit(ctx.param_list())

    def visitParam_list(self, ctx: EDBSParser.Param_listContext):
        idx = 0
        current = ctx.IDENTIFIER(idx)
        result = []
        while current is not None:
            result.append(str(current))
            idx += 1
            current = ctx.IDENTIFIER(idx)
        return result

    def visitModule_def(self, ctx:EDBSParser.Module_defContext):
        name = str(ctx.IDENTIFIER())
        params = self.visit(ctx.input_params())
        result = self.visit(ctx.output_params())
        m = Module(formal_params=params, result=result, body=ctx.module_body(),  line=ctx.start.line, col=ctx.start.column)
        self.symbol_table.modules[name] = m

    def summarize_types(self):
        print(f"{self.symbol_table.modules.keys().__len__()} Moduler")
        for k,v in self.symbol_table.modules.items():
            print(f"# Modul: {k}")
            print(f"{v.symbols}")
        print("# Hovudprogram")
        print(f"{self.symbol_table}")




def type_check(file: Path, print_info: bool = False):
    print(f"Leser EDBS fil '{file.resolve()}'...", end="")
    ast = parse(file)
    print("OK")
    symbols = SymbolTable()
    checker = EDBSTypeChecker(symbols)
    try:
        print(f"Sjekker EDBS fil '{file.resolve()}'...", end="")
        checker.visit(ast)
        print("OK")
        if print_info:
            checker.summarize_types()
    except EDBSException as e:
        print(e.msg)
        sys.exit(69)


def main():
    if len(sys.argv) >= 2:
        progname = sys.argv[1]
        progfile = Path.cwd() / progname
        type_check(progfile, True)
    else:
        print("Betjeningsfeil! Bruk: edbc <FILNAMN>")
        sys.exit(1)

if __name__ == "__main__":
    main()
