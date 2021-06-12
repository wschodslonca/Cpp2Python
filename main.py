from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarListenerImp import GrammarListenerImp
import os
import sys


class Translator:
    # Class that converts .cpp to .py
    def __init__(self,from_file,to_file):
        self.input_path = from_file
        self.input_file = None
        self.result_file = to_file
        self.input_code = ""
        self.translated_code = ""

    def import_code_file(self):
        self.input_file = open(self.input_path, "rt")
        self.input_code = self.input_file.read()

    def write_to_output(self):
        output = open(self.result_file, "w")
        output.write('# from '+self.input_path+' to '+self.result_file+'\n')
        output.write(self.translated_code)
        output.close()

    def cpp2py(self):
        lexer = GrammarLexer(InputStream(self.input_code))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.program()
        walker = ParseTreeWalker()
        listener = GrammarListenerImp()
        walker.walk(listener, tree)
        self.translated_code = listener.c


def main():
    translator = Translator(sys.argv[1],"output.py")
    translator.import_code_file()
    translator.cpp2py()
    translator.write_to_output()
    os.system('output.py')


if __name__ == '__main__':
    main()
