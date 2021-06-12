# Generated from Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#mainFunc.
    def enterMainFunc(self, ctx:GrammarParser.MainFuncContext):
        pass

    # Exit a parse tree produced by GrammarParser#mainFunc.
    def exitMainFunc(self, ctx:GrammarParser.MainFuncContext):
        pass


    # Enter a parse tree produced by GrammarParser#number.
    def enterNumber(self, ctx:GrammarParser.NumberContext):
        pass

    # Exit a parse tree produced by GrammarParser#number.
    def exitNumber(self, ctx:GrammarParser.NumberContext):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#blockElement.
    def enterBlockElement(self, ctx:GrammarParser.BlockElementContext):
        pass

    # Exit a parse tree produced by GrammarParser#blockElement.
    def exitBlockElement(self, ctx:GrammarParser.BlockElementContext):
        pass


    # Enter a parse tree produced by GrammarParser#expOrEndl.
    def enterExpOrEndl(self, ctx:GrammarParser.ExpOrEndlContext):
        pass

    # Exit a parse tree produced by GrammarParser#expOrEndl.
    def exitExpOrEndl(self, ctx:GrammarParser.ExpOrEndlContext):
        pass


    # Enter a parse tree produced by GrammarParser#coutExp.
    def enterCoutExp(self, ctx:GrammarParser.CoutExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#coutExp.
    def exitCoutExp(self, ctx:GrammarParser.CoutExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#cinExp.
    def enterCinExp(self, ctx:GrammarParser.CinExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#cinExp.
    def exitCinExp(self, ctx:GrammarParser.CinExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#bools.
    def enterBools(self, ctx:GrammarParser.BoolsContext):
        pass

    # Exit a parse tree produced by GrammarParser#bools.
    def exitBools(self, ctx:GrammarParser.BoolsContext):
        pass


    # Enter a parse tree produced by GrammarParser#exp.
    def enterExp(self, ctx:GrammarParser.ExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#exp.
    def exitExp(self, ctx:GrammarParser.ExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#expOp.
    def enterExpOp(self, ctx:GrammarParser.ExpOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#expOp.
    def exitExpOp(self, ctx:GrammarParser.ExpOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#incOp.
    def enterIncOp(self, ctx:GrammarParser.IncOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#incOp.
    def exitIncOp(self, ctx:GrammarParser.IncOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#singleExp.
    def enterSingleExp(self, ctx:GrammarParser.SingleExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#singleExp.
    def exitSingleExp(self, ctx:GrammarParser.SingleExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#bracketsExp.
    def enterBracketsExp(self, ctx:GrammarParser.BracketsExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#bracketsExp.
    def exitBracketsExp(self, ctx:GrammarParser.BracketsExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#ifSt.
    def enterIfSt(self, ctx:GrammarParser.IfStContext):
        pass

    # Exit a parse tree produced by GrammarParser#ifSt.
    def exitIfSt(self, ctx:GrammarParser.IfStContext):
        pass


    # Enter a parse tree produced by GrammarParser#whileSt.
    def enterWhileSt(self, ctx:GrammarParser.WhileStContext):
        pass

    # Exit a parse tree produced by GrammarParser#whileSt.
    def exitWhileSt(self, ctx:GrammarParser.WhileStContext):
        pass


    # Enter a parse tree produced by GrammarParser#forParamOne.
    def enterForParamOne(self, ctx:GrammarParser.ForParamOneContext):
        pass

    # Exit a parse tree produced by GrammarParser#forParamOne.
    def exitForParamOne(self, ctx:GrammarParser.ForParamOneContext):
        pass


    # Enter a parse tree produced by GrammarParser#forParamTwo.
    def enterForParamTwo(self, ctx:GrammarParser.ForParamTwoContext):
        pass

    # Exit a parse tree produced by GrammarParser#forParamTwo.
    def exitForParamTwo(self, ctx:GrammarParser.ForParamTwoContext):
        pass


    # Enter a parse tree produced by GrammarParser#forParamThree.
    def enterForParamThree(self, ctx:GrammarParser.ForParamThreeContext):
        pass

    # Exit a parse tree produced by GrammarParser#forParamThree.
    def exitForParamThree(self, ctx:GrammarParser.ForParamThreeContext):
        pass


    # Enter a parse tree produced by GrammarParser#forSt.
    def enterForSt(self, ctx:GrammarParser.ForStContext):
        pass

    # Exit a parse tree produced by GrammarParser#forSt.
    def exitForSt(self, ctx:GrammarParser.ForStContext):
        pass


    # Enter a parse tree produced by GrammarParser#returnSt.
    def enterReturnSt(self, ctx:GrammarParser.ReturnStContext):
        pass

    # Exit a parse tree produced by GrammarParser#returnSt.
    def exitReturnSt(self, ctx:GrammarParser.ReturnStContext):
        pass


    # Enter a parse tree produced by GrammarParser#identifierType.
    def enterIdentifierType(self, ctx:GrammarParser.IdentifierTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#identifierType.
    def exitIdentifierType(self, ctx:GrammarParser.IdentifierTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcType.
    def enterFuncType(self, ctx:GrammarParser.FuncTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcType.
    def exitFuncType(self, ctx:GrammarParser.FuncTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDec.
    def enterFuncDec(self, ctx:GrammarParser.FuncDecContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDec.
    def exitFuncDec(self, ctx:GrammarParser.FuncDecContext):
        pass


    # Enter a parse tree produced by GrammarParser#func.
    def enterFunc(self, ctx:GrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by GrammarParser#func.
    def exitFunc(self, ctx:GrammarParser.FuncContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignment.
    def enterAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignment.
    def exitAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#declaration.
    def enterDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#declaration.
    def exitDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#varDec.
    def enterVarDec(self, ctx:GrammarParser.VarDecContext):
        pass

    # Exit a parse tree produced by GrammarParser#varDec.
    def exitVarDec(self, ctx:GrammarParser.VarDecContext):
        pass


    # Enter a parse tree produced by GrammarParser#varAssignment.
    def enterVarAssignment(self, ctx:GrammarParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#varAssignment.
    def exitVarAssignment(self, ctx:GrammarParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#varOp.
    def enterVarOp(self, ctx:GrammarParser.VarOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#varOp.
    def exitVarOp(self, ctx:GrammarParser.VarOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#varOpVar.
    def enterVarOpVar(self, ctx:GrammarParser.VarOpVarContext):
        pass

    # Exit a parse tree produced by GrammarParser#varOpVar.
    def exitVarOpVar(self, ctx:GrammarParser.VarOpVarContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayDec.
    def enterArrayDec(self, ctx:GrammarParser.ArrayDecContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayDec.
    def exitArrayDec(self, ctx:GrammarParser.ArrayDecContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayInit.
    def enterArrayInit(self, ctx:GrammarParser.ArrayInitContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayInit.
    def exitArrayInit(self, ctx:GrammarParser.ArrayInitContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayAssignment.
    def enterArrayAssignment(self, ctx:GrammarParser.ArrayAssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayAssignment.
    def exitArrayAssignment(self, ctx:GrammarParser.ArrayAssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#params.
    def enterParams(self, ctx:GrammarParser.ParamsContext):
        pass

    # Exit a parse tree produced by GrammarParser#params.
    def exitParams(self, ctx:GrammarParser.ParamsContext):
        pass



del GrammarParser