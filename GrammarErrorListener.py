from antlr4.error.ErrorListener import ErrorListener
import sys


class GrammarErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        super().syntaxError(recognizer, offendingSymbol, line, column, msg, e)
        print("syntaxError")
        sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        super().reportAmbiguity(recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs)
        print("reportAmbiguity")
        sys.exit()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        super().reportAttemptingFullContext(recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs)
        print("reportAttemptingFullContext")
        sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        super().reportContextSensitivity(recognizer, dfa, startIndex, stopIndex, prediction, configs)
        print("reportContextSensitivity")
        sys.exit()
