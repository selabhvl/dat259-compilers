from typing import Literal

from antlr4 import *
from edbs.EDBSParser import EDBSParser
from edbs.EDBSLexer import EDBSLexer
from edbs.EDBSVisitor import EDBSVisitor

EDBS_TYP = Literal["streng", "tal", "hugseliste"]

class ExitCall(Exception):
    pass

class UndefinedVarRef(Exception):
    def __init__(self, name: str):
        self.name = name

class UndefinedModuleRef(Exception):
    def __init__(self, name: str):
        self.name = name

class VarAlreadyDefined(Exception):
    def __init__(self, name: str):
        self.name = name

class UnsoundTypes(Exception):
    def __init__(self, name: str, expected: set[EDBS_TYP], actual: set[EDBS_TYP]):
        self.name = name
        self.expected = expected
        self.actual = actual


class Module:

    def __init__(self, formal_params, result, body):
        self.formal_params = formal_params
        self.result = result
        self.body = body


class SymbolTable:

    def __init__(self, next = None):
        self.storage = {}
        self.types = {}
        self.modules = {}
        self.next = next

    def add_var(self, name: str, value: float):
        if name in self.storage:
            raise VarAlreadyDefined(name)
        self.storage[name] = value

    def get_var(self, name: str):
        if name not in self.storage:
            if self.next is not None:
                return self.next.get_var(name)
            else:
                UndefinedVarRef(name)
        return self.storage[name]

    def mutate_var(self, name: str, value):
        if self.next is not None:
            self.next.mutate_var(name, value)
        else:
            self.storage[name] = value

    def is_defined(self, name: str):
        result = name in self.storage
        if not result and self.next is not None:
            return self.next.is_defined(name)
        return result

    def register_var_name(self, name: str):
        self.types[name] = {"streng", "tal", "hugseliste"}


class CollectActualParams(EDBSVisitor):

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.values = []

    def visitActual_param_list(self, ctx:EDBSParser.Actual_param_listContext):
        for p in ctx.getChildren():
            self.visit(p)


    def visitActual_param(self, ctx:EDBSParser.Actual_paramContext):
        if ctx.IDENTIFIER() is not None:
            self.values.append(self.symbol_table.get_var(str(ctx.IDENTIFIER())))
        elif ctx.NUMBER():
            self.values.append(float(str(ctx.NUMBER()).replace(".","").replace(",",".")))
        else:
            self.values.append(self.visit(ctx.str_literal()))

    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        if ctx.STRING() is not None:
            return str(ctx.STRING())[1:-1]
        elif ctx.NEWLINE_CHAR():
            return '\n'
        elif ctx.WHITESPACE_CHAR():
            return ' '
        elif ctx.NULL_CHAR():
            return None


class InterpreterVisitor(EDBSVisitor):

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table


    def visitModule_def(self, ctx:EDBSParser.Module_defContext):
        name = str(ctx.IDENTIFIER())
        params = self.visit(ctx.input_params())
        result = self.visit(ctx.output_params())
        ctx.output_params()
        m = Module(params, result, ctx.module_body())
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
            value = self.symbol_table.get_var(name)
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
        self.symbol_table.add_var(name, value)

    def visitCalc(self, ctx:EDBSParser.CalcContext):
        name = str(ctx.IDENTIFIER())
        value = self.visit(ctx.expression())
        self.symbol_table.add_var(name, value)

    def visitMutate(self, ctx:EDBSParser.MutateContext):
        name = str(ctx.IDENTIFIER())
        if not self.symbol_table.is_defined(name):
            self.symbol_table.add_var(name,0.0)
        value = self.visit(ctx.expression())
        self.symbol_table.mutate_var(name, value)

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

    def visitListop(self, ctx:EDBSParser.ListopContext):
        return None # TODO: hugseliste

    def visitCall(self, ctx:EDBSParser.CallContext):
        name = str(ctx.IDENTIFIER())
        collect_actuals = CollectActualParams(self.symbol_table)
        collect_actuals.visit(ctx.actual_param_list())
        module = self.symbol_table.modules[name]
        global_scope = self.symbol_table
        self.symbol_table = SymbolTable()
        for p, v in zip(module.formal_params, collect_actuals.values):
            self.symbol_table.add_var(p, v)
        try:
            self.visit(module.body)
        except ExitCall:
            pass # TODO: error handling
        result = self.symbol_table.get_var(module.result)
        self.symbol_table = global_scope
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


def main():

    input_stream = FileStream("../examples/types.edbs", encoding="utf-8")
    lexer = EDBSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EDBSParser(token_stream)
    tree = parser.program()
    table = SymbolTable()
    #visitor = InterpreterVisitor(table)
    #visitor.visit(tree)
    type_check = TypeChecker(table)
    try:
        type_check.visit(tree)
        type_check.summarize_types()
    except UnsoundTypes as e:
        print(f"FEIL! Stedfortreter {e.name} har feil type! Det forventes å være {e.expected} mend den er {e.actual}")
    except VarAlreadyDefined as e:
        print(f"FEIL! Stedfortreter {e.name} finnast alt!")
    except UndefinedVarRef as e:
        print(f"FEIL! Stedfortreter {e.name} finnast ikkje")

if __name__ == '__main__':
    main()
