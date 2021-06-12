from GrammarListener import GrammarListener
from GrammarParser import *


class GrammarListenerImp(GrammarListener):

    def __init__(self):
        self.c = ""
        self.indParam = 0

    def parseSingleExpIns(self, ctx):
        if ctx.incOp():
            if ctx.incOp().PP():
                return ctx.ID().getText() + ' += 1'
            else:
                return ctx.ID().getText() + ' -= 1'
        elif ctx.NOT():
            return 'not ' + ctx.ID().getText()
        else:
            return ctx.getText()

    def parseBoolsIns(self, ctx):
        if ctx.TRUE():
            return "True"
        else:
            return "False"

    def parseExpIns(self, ctx):
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
            if ctx.singleExp():
                text += self.parseSingleExpIns(ctx.singleExp())
            elif ctx.bools():
                text += self.parseBoolsIns(ctx.bools())
            else:
                # func/number/id/...
                text += ctx.getText()
        return text

    def parseExp(self, ctx):
        self.add(self.parseExpIns(ctx))

    def parseExpOp(self, ctx):
        if ctx.AND():
            return " and "
        elif ctx.OR():
            return " or "
        else:
            return ' ' + ctx.getText() + ' '

    def parseFuncDec(self, ctx):
        self.endl()
        self.ind()
        self.add("def " + ctx.ID().getText() + "(")
        params = ctx.params()
        if len(params.ID()) > 0:
            self.add(params.ID()[0].getText())
            for i in params.ID()[1:]:
                self.add(", " + i.getText())
        self.add(")")
        self.parseBlock(ctx.block())
        self.blank()

    def parseVarDec(self, ctx):
        self.add(ctx.ID().getText())
        if ctx.ASSIGN():
            self.add(" = ")
            self.parseExp(ctx.exp())
        else:
            self.add(" = None")

    def parseStatement(self, ctx):
        if ctx.whileSt():
            self.parseWhileSt(ctx.whileSt())
        elif ctx.ifSt():
            self.parseIfSt(ctx.ifSt())
        elif ctx.returnSt():
            self.parseReturnSt(ctx.returnSt())
        elif ctx.forSt():
            self.parseForSt(ctx.forSt())
        # break/continue
        else:
            self.add(ctx.getText()[:-1])

    def parseReturnSt(self, ctx):
        self.add(ctx.RETURN().getText() + " ")
        self.parseExp(ctx.exp())

    def parseArrayInit(self, ctx):
        self.parseExp(ctx.exp()[0])
        for i in ctx.exp()[1:]:
            self.add(', ')
            self.parseExp(i)

    def parseArrayDec(self, ctx):
        self.add(ctx.ID().getText() + ' = [')
        if ctx.arrayInit():
            self.parseArrayInit(ctx.arrayInit())
        else:
            if ctx.PINT():
                self.add('0 for _ in range(' + ctx.PINT().getText() + ')')
            else:
                pass
        self.add(']')

    def parseDeclaration(self, ctx):
        if ctx.varDec():
            self.parseVarDec(ctx.varDec())
        elif ctx.arrayDec():
            self.parseArrayDec(ctx.arrayDec())
        # todo
        else:
            pass

    def parseVarOp(self, ctx):
        self.add(" " + ctx.getText() + " ")

    def parseVarOpVar(self, ctx):
        self.add(ctx.ID()[0].getText())
        self.parseVarOp(ctx.varOp())
        self.add(ctx.ID()[1].getText())

    def parseVarAssignment(self, ctx):
        self.add(ctx.ID().getText() + ' ' + ctx.ASSIGN().getText() + ' ')
        self.parseExp(ctx.exp())

    def parseSingleExp(self, ctx):
        print("check")
        self.add(self.parseSingleExpIns(ctx))

    def parseArrayAssignment(self, ctx):
        self.add(ctx.ID().getText() + "[" + ctx.PINT().getText() + "] = ")
        self.parseExp(ctx.exp())

    def parseAssignment(self, ctx):
        if ctx.varOpVar():
            self.parseVarOpVar(ctx.varOpVar())
        elif ctx.varAssignment():
            self.parseVarAssignment(ctx.varAssignment())
        elif ctx.arrayAssignment():
            self.parseArrayAssignment(ctx.arrayAssignment())
        # todo
        else:
            pass

    def parseExpOrEndl(self, ctx):
        if ctx.exp():
            self.parseExp(ctx.exp())
        elif ctx.ENDL():
            self.add("'\\n'")
        else:
            print("error in parseCoutExp(temp)")

    def parseCoutExp(self, ctx):
        self.add("print(")
        self.parseExpOrEndl(ctx.expOrEndl()[0])
        if len(ctx.expOrEndl()) > 1:
            for i in ctx.expOrEndl()[1:]:
                self.add(', ')
                self.parseExpOrEndl(i)
        self.add(", sep='', end='')")

    def parseCinExp(self, ctx):
        self.add(ctx.ID().getText() + " = input()")

    def parseCommToken(self, ctx):
        self.add('#' + ctx.getText()[2:])

    # todo
    def parseBlockElement(self, ctx):
        self.endl()
        self.ind()
        if ctx.exp():
            self.parseExp(ctx.exp())
        if ctx.statement():
            self.parseStatement(ctx.statement())
        elif ctx.declaration():
            self.parseDeclaration(ctx.declaration())
        elif ctx.assignment():
            self.parseAssignment(ctx.assignment())
        elif ctx.coutExp():
            self.parseCoutExp(ctx.coutExp())
        elif ctx.cinExp():
            self.parseCinExp(ctx.cinExp())
        elif ctx.COMM():
            self.parseCommToken(ctx)
        else:
            pass

    def parseBlock(self, ctx):
        self.add(":")
        self.incInd()
        if len(ctx.blockElement()) > 0:
            for i in ctx.blockElement():
                self.parseBlockElement(i)
        self.decInd()

    def parseBracketExp(self, ctx):
        self.parseExp(ctx.exp())

    def parseWhileSt(self, ctx):
        self.add(ctx.WHILE().getText() + " ")
        self.parseBracketExp(ctx.bracketsExp())
        self.parseBlock(ctx.block())

    def parseIfSt(self, ctx):
        self.add(ctx.IF().getText() + " ")
        self.parseBracketExp(ctx.bracketsExp()[0])
        self.parseBlock(ctx.block()[0])
        i = 1
        if len(ctx.ELSE_IF()) > 0:
            for i in range(1, len(ctx.ELSE_IF()) + 1):
                self.endl()
                self.ind()
                self.add(ctx.ELSE_IF()[i - 1].getText())
                self.parseBracketExp(ctx.bracketsExp()[i])
                self.parseBlock(ctx.block()[i])
        if ctx.ELSE():
            self.endl()
            self.ind()
            self.add(ctx.ELSE().getText())
            self.parseBlock(ctx.block(i))

    def parseMainFunc(self, ctx):
        self.endl()
        self.add("def main()")
        self.parseBlock(ctx.block())
        self.blank()

    def add(self, text):
        self.c += text

    def ind(self):
        inds = ""
        for i in range(self.indParam):
            inds += "    "
        self.add(inds)

    def incInd(self):
        self.indParam += 1

    def decInd(self):
        self.indParam -= 1

    def endl(self):
        self.add('\n')

    def blank(self):
        self.add('\n\n')

    def parseForParamOne(self, ctx):
        if ctx.varDec():
            self.parseVarDec(ctx.varDec())
            self.endl()
            self.ind()
        elif ctx.varAssignment():
            self.parseVarAssignment(ctx.varAssignment())
            self.endl()
            self.ind()
        elif ctx.exp():
            self.parseExp(ctx.exp())
            self.endl()
            self.ind()
        else:
            pass

    def parseForParamTwo(self, ctx):
        if ctx.exp():
            self.parseExp(ctx.exp())
        else:
            self.add("True")

    def parseForParamThree(self, ctx):
        if ctx.exp():
            self.parseExp(ctx.exp())

    def parseForSt(self, ctx):
        self.parseForParamOne(ctx.forParamOne())
        self.add("while ")
        self.parseForParamTwo(ctx.forParamTwo())
        self.parseBlock(ctx.block())
        self.endl()
        self.ind()
        self.add("    ")
        self.parseForParamThree(ctx.forParamThree())

    def enterProgram(self, ctx: GrammarParser.ProgramContext):
        for i in ctx.programElement():
            if i.funcDec():
                self.parseFuncDec(i.funcDec())
            elif i.varDec():
                self.endl()
                self.parseVarDec(i.varDec())
                self.blank()
        self.parseMainFunc(ctx.mainFunc())

    def exitProgram(self, ctx: GrammarParser.ProgramContext):
        self.endl()
        self.add("if __name__ == '__main__':\n    main()\n")
