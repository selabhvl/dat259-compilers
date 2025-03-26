import sys

from edbs.parser.EDBSParser import  EDBSParser
from edbs.parser.EDBSVisitor import EDBSVisitor
from edbs.utils import parse, CollectActualParams
from edbs.symbols import SymbolTable, Module, EDBSException, UnsupportedFeature
from pathlib import Path


class EDBSInterpreter(EDBSVisitor):

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def visitModule_def(self, ctx:EDBSParser.Module_defContext):
        name = str(ctx.IDENTIFIER())
        params = self.visit(ctx.input_params())
        result = self.visit(ctx.output_params())
        m = Module(params, result, ctx.module_body(), ctx.start.line, ctx.start.column )
        m.body = ctx.module_body()
        self.symbol_table.modules[name] = m

    def visitOutput_params(self, ctx:EDBSParser.Output_paramsContext):
        return str(ctx.IDENTIFIER())

    def visitInput_params(self, ctx:EDBSParser.Input_paramsContext):
        return self.visit(ctx.param_list())

    def visitParam_list(self, ctx:EDBSParser.Param_listContext):
        idx = 0
        current = ctx.IDENTIFIER(idx)
        result = []
        while current is not None:
            result.append(str(current))
            idx += 1
            current = ctx.IDENTIFIER(idx)
        return result

    def visitWrite_arg(self, ctx:EDBSParser.Write_argContext):
        if ctx.IDENTIFIER() is not None:
            name = str(ctx.IDENTIFIER())
            value = self.symbol_table.get_var(name, ctx.start.line, ctx.start.column).value
            if isinstance(value, float):
                value = str(round(value, 2)).replace(".", ",")
            if value.endswith(",0"):
                value = value[:-2]
            print(str(value), end=" ")
        elif ctx.STRING():
            string_token = ctx.STRING()
            print(str(string_token)[1:-1], end=" ")

    def visitWrite(self, ctx:EDBSParser.WriteContext):
        for c in ctx.children:
            self.visit(c)
        print()

    def visitRead(self, ctx:EDBSParser.ReadContext):
        prompt = str(ctx.STRING())[1:-1]
        value = float(input(f"{prompt}: ").replace(".", "").replace(",", "."))
        name = str(ctx.IDENTIFIER())
        self.symbol_table.add_var(name, ctx.start.line, ctx.start.column, value)

    def visitCalc(self, ctx:EDBSParser.CalcContext):
        name = str(ctx.IDENTIFIER())
        value = self.visit(ctx.expression())
        self.symbol_table.add_var(name, line=ctx.start.line, col=ctx.start.column, value=value)

    def visitMutate(self, ctx:EDBSParser.MutateContext):
        name = str(ctx.IDENTIFIER())
        if not self.symbol_table.is_defined(name):
            self.symbol_table.add_var(name, ctx.start.line, ctx.start.column, value=0.0)
        value = self.visit(ctx.expression())
        self.symbol_table.mutate_var(name, ctx.start.line, ctx.start.column, value=value)

    def visitWhile(self, ctx:EDBSParser.WhileContext):
        is_satisfied =  self.visit(ctx.bool_expr())
        self.symbol_table = SymbolTable(self.symbol_table)
        while is_satisfied:
            for c in ctx.children:
                self.visit(c)
            is_satisfied = self.visit(ctx.bool_expr())
        self.symbol_table = self.symbol_table.next

    def visitStrlit(self, ctx:EDBSParser.StrlitContext):
        return self.visit(ctx.str_literal())

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        if ctx.STRING() is not None:
            return str(ctx.STRING())[1:-1]
        elif ctx.NEWLINE_CHAR():
            return '\n'
        elif ctx.WHITESPACE_CHAR():
            return ' '
        elif ctx.NULL_CHAR():
            return None

    def visitNolit(self, ctx:EDBSParser.NolitContext):
        value = float(str(ctx.NUMBER()).replace(",", '.'))
        return value

    def visitVar(self, ctx:EDBSParser.VarContext):
        name = str(ctx.IDENTIFIER())
        var_obj = self.symbol_table.get_var(name, ctx.start.line, ctx.start.column)
        value = var_obj.get_val()
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

    def visitListop(self, ctx:EDBSParser.ListopContext):
        raise UnsupportedFeature("operasjoner på hugselister") # TODO: hugseliste

    def visitCall(self, ctx:EDBSParser.CallContext):
        name = str(ctx.IDENTIFIER())
        module = self.symbol_table.get_module(name, ctx.start.line, ctx.start.column)

        # update module symbol table with actual param values
        collect_actuals = CollectActualParams(self.symbol_table)
        collect_actuals.visit(ctx.actual_param_list())
        for p, v in zip(module.formal_param_names, collect_actuals.values):
            module.symbols.get_var(p, ctx.start.line, ctx.start.column).value = v

        # call module with fresh interpreter
        module_interpreter = EDBSInterpreter(module.symbols)
        module_interpreter.visit(module.body)

        # get result back
        result = module.symbols.get_var(module.result_param_name, ctx.start.line, ctx.start.column).value
        return result

    # bool expressions
    def visitComp(self, ctx:EDBSParser.CompContext):
        return self.visit(ctx.comparison())

    def visitComparison(self, ctx:EDBSParser.ComparisonContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(ctx.getChildCount() - 1))
        if ctx.COMP_EQL() is not None:
            return lhs == rhs
        elif ctx.COMP_LT() is not None:
            return lhs < rhs
        elif ctx.COMP_LEQ() is not None:
            return lhs <= rhs
        elif ctx.COMP_GT() is not None:
            return lhs > rhs
        elif ctx.COMP_GEQ() is not None:
            return lhs >= rhs

    def visitAnd(self, ctx:EDBSParser.AndContext):
        return self.visit(ctx.getChild(0)) and self.visit(ctx.getChild(2))

    def visitOr(self, ctx:EDBSParser.OrContext):
        return self.visit(ctx.getChild(0)) or self.visitComp(ctx.getChild(2))

    def visitNot(self, ctx:EDBSParser.NotContext):
        return not self.visit(ctx.bool_expr())


def interpret(file: Path):
    ast = parse(file)
    symbols = SymbolTable()
    interpreter = EDBSInterpreter(symbols)
    try:
        interpreter.visit(ast)
    except EDBSException as e:
        print(e.msg)
        sys.exit(69)

def main():
    if len(sys.argv) >= 2:
        progname = sys.argv[1]
        progfile = Path.cwd() / progname
        interpret(progfile)
    else:
        print("Betjeningsfeil! Bruk: edbi <FILNAMN>")
        sys.exit(1)

if __name__ == "__main__":
    main()

