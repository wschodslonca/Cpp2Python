from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarListener import GrammarListener

class Translator:
    # Class that converts .cpp to .py
    def __init__(self):

        self.input_file = None
        self.result_file = "output.py"
        self.lines = []
        self.translated_code = ""

    def import_code_file(self):
        self.input_file = open("nwd.cpp", "rt")
        self.lines = self.input_file.readlines()

    def write_to_output(self):
        output = open(self.result_file, "w")
        output.write(self.translated_code)
        output.close()

    def cpp2py(self):
        for line in self.lines:
            print(line)


def main():
    translator = Translator()
    translator.import_code_file()
    translator.cpp2py()
    translator.write_to_output()


if __name__ == '__main__':
    main()

