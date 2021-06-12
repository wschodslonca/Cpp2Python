from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarListenerImp import GrammarListenerImp
import os
import sys


class Translator:
    # Class that converts .cpp to .py
    def __init__(self):
        self.workspace_path = "workspace\\"
        self.input_file = None
        self.result_file = None
        self.input_code = ""
        self.translated_code = ""

    def load_file(self):
        if len(sys.argv)>1:
            if sys.argv[1][-4:]=='.cpp':
                self.input_file = sys.argv[1]
                self.result_file = sys.argv[1][0:-4] + '.py'
                return True
            else:
                print('input file is not .cpp type...')
                return False
        else:
            print('missing input file...')
            return False


    def import_code(self):
        input_file = open(self.workspace_path+self.input_file, "rt")
        self.input_code = input_file.read()

    def write_to_output(self):
        output = open(self.workspace_path+self.result_file, "w")
        output.write('# from ' + self.input_file + ' to ' + self.result_file + '\n')
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

    def run_output(self):
        os.system(self.workspace_path+self.result_file)


def main():
        translator = Translator()
        if translator.load_file():
            translator.import_code()
            translator.cpp2py()
            translator.write_to_output()
            translator.run_output()

if __name__ == '__main__':
    main()
