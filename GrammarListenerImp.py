from antlr4 import *
import sys
from GrammarListener import GrammarListener
from GrammarLexer import GrammarLexer
from GrammarParser import *

class GrammarListenerImp(GrammarListener):

    def __init__(self):
        self.c = ""
        self.indParam = 0


    def parseExpIns(self,ctx):
        text = ""
        if len(ctx.exp()) == 2:
            text += self.parseExpIns(ctx.exp()[0])
            text += self.parseExpOp(ctx.expOp())
            text += self.parseExpIns(ctx.exp()[1])
        elif len(ctx.exp()) == 1:
            text += ctx.LEFT_BRACKET().getText()
            text += self.parseExpIns(ctx.exp()[0])
            text += ctx.RIGHT_BRACKET().getText()
        else:
            # temp
            text += ctx.getText()
        return text

    def parseExp(self, ctx):
        self.add(self.parseExpIns(ctx))

    def parseExpOp(self, ctx):
        #if isinstance(ctx,GrammarParser.AND):
        if ctx.getText()=="&&":
            return " and "
        #elif isinstance(ctx,GrammarParser.OR):
        elif ctx.getText() == "||":
            return " or "
        else:
            return ctx.getText()

    def parseFuncDec(self,ctx):
        self.ind()
        self.add("def " + ctx.ID().getText() + "(")
        params = ctx.params()
        if len(params.ID()) > 0:
            self.add(params.ID()[0].getText())
            for i in params.ID()[1:]:
                self.add(", " + i.getText())
        self.add(")")
        self.parseBlock(ctx.block())


    #todo
    def parseVarDec(self,ctx):
        self.add(ctx.ID().getText())
        if ctx.ASSIGN():
            self.add(" = ")
            self.parseExp(ctx.exp())
        else:
            self.add(" = None")

    #todo
    def parseStatement(self,ctx):
        self.ind()
        if ctx.whileSt():
            self.parseWhileSt(ctx.whileSt())
        elif ctx.ifSt():
            self.parseIfSt(ctx.ifSt())
        elif ctx.returnSt():
            self.parseReturnSt(ctx.returnSt())
        else:
            pass

    def parseReturnSt(self,ctx):
        self.add(ctx.RETURN().getText()+" ")
        self.parseExp(ctx.exp())
        self.add("\n")

    #todo
    def parseDeclaration(self,ctx):
        self.ind()
        if ctx.varDec():
            self.parseVarDec(ctx.varDec())
        #todo
        else:
            pass
        self.add("\n")

    def parseVarOp(self,ctx):
        self.add(ctx.getText())

    #todo
    def parseVarOpVar(self,ctx):
        self.add(ctx.ID()[0].getText())
        self.add(ctx.varOp().getText())
        self.add(ctx.ID()[1].getText())

    #todo
    def parseAssignment(self,ctx):
        self.ind()
        if ctx.varOpVar():
            self.parseVarOpVar(ctx.varOpVar())
        #todo
        else:
            pass
        self.add("\n")

    #todo
    def parseBlockElement(self,ctx):
        if ctx.statement():
            self.parseStatement(ctx.statement())
        elif ctx.declaration():
            self.parseDeclaration(ctx.declaration())
        elif ctx.assignment():
            self.parseAssignment(ctx.assignment())
        else:
            self.parseExp(ctx.exp())


    def parseBlock(self,ctx):
        self.add(":\n")
        self.incInd()
        if len(ctx.blockElement())>0:
            for i in ctx.blockElement():
                self.parseBlockElement(i)
        self.decInd()

    def parseBracketExp(self, ctx):
        self.parseExp(ctx.exp())

    def parseWhileSt(self,ctx):
        self.add(ctx.WHILE().getText()+" ")
        self.parseBracketExp(ctx.bracketsExp())
        self.parseBlock(ctx.block())

    def parseIfSt(self,ctx):
        self.add(ctx.IF().getText()+" ")
        self.parseBracketExp(ctx.bracketsExp()[0])
        self.parseBlock(ctx.block()[0])
        i = 1
        if len(ctx.ELSE_IF())>0:
            for i in range(1,len(ctx.ELSE_IF())+1):
                self.ind()
                self.add(ctx.ELSE_IF()[i-1].getText())
                self.parseBracketExp(ctx.bracketsExp()[i])
                self.parseBlock(ctx.block()[i])
        if ctx.ELSE():
            self.ind()
            self.add(ctx.ELSE().getText())
            self.parseBlock(ctx.block(i))

    def parseMainFunc(self,ctx):
        self.add("def main()")
        self.parseBlock(ctx.block())

    def add(self,text):
        self.c += text

    def ind(self):
        inds = ""
        for i in range(self.indParam):
            inds+="  "
        self.add(inds)

    def incInd(self):
        self.indParam += 1

    def decInd(self):
        self.indParam -= 1

    def enterProgram(self, ctx: GrammarParser.ProgramContext):
        if len(ctx.funcDec())>0:
            for i in ctx.funcDec():
                self.parseFuncDec(i)
        if len(ctx.varDec())>0:
            for i in ctx.varDec():
                self.parseVarDec(i)
        self.parseMainFunc(ctx.mainFunc())


    def exitProgram(self, ctx: GrammarParser.ProgramContext):
        self.add("if __name__ == '__main__':\n  main()")

    def enterMainFunc(self, ctx: GrammarParser.MainFuncContext):
        pass

    def exitMainFunc(self, ctx: GrammarParser.MainFuncContext):
        pass

    def enterBlock(self, ctx: GrammarParser.BlockContext):
        pass

    def exitBlock(self, ctx: GrammarParser.BlockContext):
        pass

    def enterBlockElement(self, ctx: GrammarParser.BlockElementContext):
        super().enterBlockElement(ctx)

    def exitBlockElement(self, ctx: GrammarParser.BlockElementContext):
        super().exitBlockElement(ctx)

    def enterExp(self, ctx: GrammarParser.ExpContext):
        pass

    def exitExp(self, ctx: GrammarParser.ExpContext):
        pass

    def enterExpOp(self, ctx: GrammarParser.ExpOpContext):
        pass

    def exitExpOp(self, ctx: GrammarParser.ExpOpContext):
        pass

    def enterSingleExp(self, ctx: GrammarParser.SingleExpContext):
        super().enterSingleExp(ctx)

    def exitSingleExp(self, ctx: GrammarParser.SingleExpContext):
        super().exitSingleExp(ctx)

    def enterBracketsExp(self, ctx: GrammarParser.BracketsExpContext):
        pass

    def exitBracketsExp(self, ctx: GrammarParser.BracketsExpContext):
        pass

    def enterStatement(self, ctx: GrammarParser.StatementContext):
        super().enterStatement(ctx)

    def exitStatement(self, ctx: GrammarParser.StatementContext):
        super().exitStatement(ctx)

    def enterIfSt(self, ctx: GrammarParser.IfStContext):
        pass

    def exitIfSt(self, ctx: GrammarParser.IfStContext):
        super().exitIfSt(ctx)

    def enterWhileSt(self, ctx: GrammarParser.WhileStContext):
        pass


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
        pass


    def exitFuncDec(self, ctx: GrammarParser.FuncDecContext):
        pass

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
        pass

    def exitParams(self, ctx: GrammarParser.ParamsContext):
        pass



