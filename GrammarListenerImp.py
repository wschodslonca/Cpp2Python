from antlr4 import *
import sys
from GrammarListener import GrammarListener
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser

class GrammarListenerImp(GrammarListener):

    def __init__(self):
        self.c = ""

    def enterProgram(self, ctx: GrammarParser.ProgramContext):
        super().enterProgram(ctx)

    def exitProgram(self, ctx: GrammarParser.ProgramContext):
        self.c +="if __name__ == '__main__':\n  main()"

    def enterMainFunc(self, ctx: GrammarParser.MainFuncContext):
        super().enterMainFunc(ctx)

    def exitMainFunc(self, ctx: GrammarParser.MainFuncContext):
        super().exitMainFunc(ctx)

    def enterBlock(self, ctx: GrammarParser.BlockContext):
        super().enterBlock(ctx)

    def exitBlock(self, ctx: GrammarParser.BlockContext):
        super().exitBlock(ctx)

    def enterBlockElement(self, ctx: GrammarParser.BlockElementContext):
        super().enterBlockElement(ctx)

    def exitBlockElement(self, ctx: GrammarParser.BlockElementContext):
        super().exitBlockElement(ctx)

    def enterExp(self, ctx: GrammarParser.ExpContext):
        super().enterExp(ctx)

    def exitExp(self, ctx: GrammarParser.ExpContext):
        super().exitExp(ctx)

    def enterExpOp(self, ctx: GrammarParser.ExpOpContext):
        super().enterExpOp(ctx)

    def exitExpOp(self, ctx: GrammarParser.ExpOpContext):
        super().exitExpOp(ctx)

    def enterSingleExp(self, ctx: GrammarParser.SingleExpContext):
        super().enterSingleExp(ctx)

    def exitSingleExp(self, ctx: GrammarParser.SingleExpContext):
        super().exitSingleExp(ctx)

    def enterBracketsExp(self, ctx: GrammarParser.BracketsExpContext):
        super().enterBracketsExp(ctx)

    def exitBracketsExp(self, ctx: GrammarParser.BracketsExpContext):
        super().exitBracketsExp(ctx)

    def enterStatement(self, ctx: GrammarParser.StatementContext):
        super().enterStatement(ctx)

    def exitStatement(self, ctx: GrammarParser.StatementContext):
        super().exitStatement(ctx)

    def enterIfSt(self, ctx: GrammarParser.IfStContext):
        super().enterIfSt(ctx)

    def exitIfSt(self, ctx: GrammarParser.IfStContext):
        super().exitIfSt(ctx)

    def enterWhileSt(self, ctx: GrammarParser.WhileStContext):
        super().enterWhileSt(ctx)

    def exitWhileSt(self, ctx: GrammarParser.WhileStContext):
        super().exitWhileSt(ctx)

    def enterForSt(self, ctx: GrammarParser.ForStContext):
        super().enterForSt(ctx)

    def exitForSt(self, ctx: GrammarParser.ForStContext):
        super().exitForSt(ctx)

    def enterReturnSt(self, ctx: GrammarParser.ReturnStContext):
        super().enterReturnSt(ctx)

    def exitReturnSt(self, ctx: GrammarParser.ReturnStContext):
        super().exitReturnSt(ctx)

    def enterIdentifierType(self, ctx: GrammarParser.IdentifierTypeContext):
        super().enterIdentifierType(ctx)

    def exitIdentifierType(self, ctx: GrammarParser.IdentifierTypeContext):
        super().exitIdentifierType(ctx)

    def enterFuncType(self, ctx: GrammarParser.FuncTypeContext):
        super().enterFuncType(ctx)

    def exitFuncType(self, ctx: GrammarParser.FuncTypeContext):
        super().exitFuncType(ctx)

    def enterFuncDec(self, ctx: GrammarParser.FuncDecContext):
        super().enterFuncDec(ctx)

    def exitFuncDec(self, ctx: GrammarParser.FuncDecContext):
        super().exitFuncDec(ctx)

    def enterFunc(self, ctx: GrammarParser.FuncContext):
        super().enterFunc(ctx)

    def exitFunc(self, ctx: GrammarParser.FuncContext):
        super().exitFunc(ctx)

    def enterAssignment(self, ctx: GrammarParser.AssignmentContext):
        super().enterAssignment(ctx)

    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        super().exitAssignment(ctx)

    def enterDeclaration(self, ctx: GrammarParser.DeclarationContext):
        super().enterDeclaration(ctx)

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        super().exitDeclaration(ctx)

    def enterVarDec(self, ctx: GrammarParser.VarDecContext):
        super().enterVarDec(ctx)

    def exitVarDec(self, ctx: GrammarParser.VarDecContext):
        super().exitVarDec(ctx)

    def enterVarAssignment(self, ctx: GrammarParser.VarAssignmentContext):
        super().enterVarAssignment(ctx)

    def exitVarAssignment(self, ctx: GrammarParser.VarAssignmentContext):
        super().exitVarAssignment(ctx)

    def enterVarOp(self, ctx: GrammarParser.VarOpContext):
        super().enterVarOp(ctx)

    def exitVarOp(self, ctx: GrammarParser.VarOpContext):
        super().exitVarOp(ctx)

    def enterVarOpVar(self, ctx: GrammarParser.VarOpVarContext):
        super().enterVarOpVar(ctx)

    def exitVarOpVar(self, ctx: GrammarParser.VarOpVarContext):
        super().exitVarOpVar(ctx)

    def enterArrayDec(self, ctx: GrammarParser.ArrayDecContext):
        super().enterArrayDec(ctx)

    def exitArrayDec(self, ctx: GrammarParser.ArrayDecContext):
        super().exitArrayDec(ctx)

    def enterArrayInit(self, ctx: GrammarParser.ArrayInitContext):
        super().enterArrayInit(ctx)

    def exitArrayInit(self, ctx: GrammarParser.ArrayInitContext):
        super().exitArrayInit(ctx)

    def enterArrayAssignment(self, ctx: GrammarParser.ArrayAssignmentContext):
        super().enterArrayAssignment(ctx)

    def exitArrayAssignment(self, ctx: GrammarParser.ArrayAssignmentContext):
        super().exitArrayAssignment(ctx)

    def enterParams(self, ctx: GrammarParser.ParamsContext):
        super().enterParams(ctx)

    def exitParams(self, ctx: GrammarParser.ParamsContext):
        super().exitParams(ctx)



