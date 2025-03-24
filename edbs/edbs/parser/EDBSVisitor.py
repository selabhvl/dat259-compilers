# Generated from /Users/past-madm/Projects/teaching/dat259/dat259-compilers/edbs/EDBS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from edbs.parser.EDBSParser import EDBSParser
else:
    from edbs.parser.EDBSParser import EDBSParser

# This class defines a complete generic visitor for a parse tree produced by EDBSParser.

class EDBSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EDBSParser#program.
    def visitProgram(self, ctx:EDBSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#module_def.
    def visitModule_def(self, ctx:EDBSParser.Module_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#input_params.
    def visitInput_params(self, ctx:EDBSParser.Input_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#output_params.
    def visitOutput_params(self, ctx:EDBSParser.Output_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#module_body.
    def visitModule_body(self, ctx:EDBSParser.Module_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#param_list.
    def visitParam_list(self, ctx:EDBSParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#main_statement.
    def visitMain_statement(self, ctx:EDBSParser.Main_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#while.
    def visitWhile(self, ctx:EDBSParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#read.
    def visitRead(self, ctx:EDBSParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#readfile.
    def visitReadfile(self, ctx:EDBSParser.ReadfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#write.
    def visitWrite(self, ctx:EDBSParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#calc.
    def visitCalc(self, ctx:EDBSParser.CalcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#mutate.
    def visitMutate(self, ctx:EDBSParser.MutateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#return.
    def visitReturn(self, ctx:EDBSParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#write_arg.
    def visitWrite_arg(self, ctx:EDBSParser.Write_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#add.
    def visitAdd(self, ctx:EDBSParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#sub.
    def visitSub(self, ctx:EDBSParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#mul.
    def visitMul(self, ctx:EDBSParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#var.
    def visitVar(self, ctx:EDBSParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#concat.
    def visitConcat(self, ctx:EDBSParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#nested.
    def visitNested(self, ctx:EDBSParser.NestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#substr.
    def visitSubstr(self, ctx:EDBSParser.SubstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#call.
    def visitCall(self, ctx:EDBSParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#div.
    def visitDiv(self, ctx:EDBSParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#strlit.
    def visitStrlit(self, ctx:EDBSParser.StrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#split.
    def visitSplit(self, ctx:EDBSParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#nolit.
    def visitNolit(self, ctx:EDBSParser.NolitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#listop.
    def visitListop(self, ctx:EDBSParser.ListopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#repeat.
    def visitRepeat(self, ctx:EDBSParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#expo.
    def visitExpo(self, ctx:EDBSParser.ExpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#actual_param_list.
    def visitActual_param_list(self, ctx:EDBSParser.Actual_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#actual_param.
    def visitActual_param(self, ctx:EDBSParser.Actual_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#list_command.
    def visitList_command(self, ctx:EDBSParser.List_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#str_literal.
    def visitStr_literal(self, ctx:EDBSParser.Str_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#comp.
    def visitComp(self, ctx:EDBSParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#not.
    def visitNot(self, ctx:EDBSParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#or.
    def visitOr(self, ctx:EDBSParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#and.
    def visitAnd(self, ctx:EDBSParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDBSParser#comparison.
    def visitComparison(self, ctx:EDBSParser.ComparisonContext):
        return self.visitChildren(ctx)



del EDBSParser