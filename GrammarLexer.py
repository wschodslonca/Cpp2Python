# Generated from Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u01c8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\5\'\u00ec\n")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\5\'\u00f3\n\'\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\3")
        buf.write("9\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("=\3=\5=\u016c\n=\3>\3>\3>\3>\3>\3?\3?\3@\3@\3@\7@\u0178")
        buf.write("\n@\f@\16@\u017b\13@\5@\u017d\n@\3A\3A\7A\u0181\nA\fA")
        buf.write("\16A\u0184\13A\3B\3B\3C\3C\5C\u018a\nC\3D\6D\u018d\nD")
        buf.write("\rD\16D\u018e\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\3F\3F\3F\3F\3G\6G\u01ba\nG\rG\16G\u01bb")
        buf.write("\3G\3G\3H\3H\3H\3H\7H\u01c4\nH\fH\16H\u01c7\13H\2\2I\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008b")
        buf.write("G\u008dH\u008fI\3\2\7\3\2\62;\3\2\63;\5\2C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\4\2\f\f\17\17\2\u01d1\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0093")
        buf.write("\3\2\2\2\7\u0095\3\2\2\2\t\u0097\3\2\2\2\13\u0099\3\2")
        buf.write("\2\2\r\u009b\3\2\2\2\17\u009d\3\2\2\2\21\u00a0\3\2\2\2")
        buf.write("\23\u00a2\3\2\2\2\25\u00a4\3\2\2\2\27\u00a6\3\2\2\2\31")
        buf.write("\u00a8\3\2\2\2\33\u00aa\3\2\2\2\35\u00ac\3\2\2\2\37\u00ae")
        buf.write("\3\2\2\2!\u00b0\3\2\2\2#\u00b2\3\2\2\2%\u00b5\3\2\2\2")
        buf.write("\'\u00b8\3\2\2\2)\u00ba\3\2\2\2+\u00bc\3\2\2\2-\u00be")
        buf.write("\3\2\2\2/\u00c0\3\2\2\2\61\u00c2\3\2\2\2\63\u00c4\3\2")
        buf.write("\2\2\65\u00c7\3\2\2\2\67\u00ca\3\2\2\29\u00cc\3\2\2\2")
        buf.write(";\u00cf\3\2\2\2=\u00d2\3\2\2\2?\u00d5\3\2\2\2A\u00d8\3")
        buf.write("\2\2\2C\u00db\3\2\2\2E\u00de\3\2\2\2G\u00e1\3\2\2\2I\u00e4")
        buf.write("\3\2\2\2K\u00e7\3\2\2\2M\u00eb\3\2\2\2O\u00f4\3\2\2\2")
        buf.write("Q\u00f8\3\2\2\2S\u00fe\3\2\2\2U\u0105\3\2\2\2W\u010a\3")
        buf.write("\2\2\2Y\u010f\3\2\2\2[\u0116\3\2\2\2]\u011b\3\2\2\2_\u0120")
        buf.write("\3\2\2\2a\u0123\3\2\2\2c\u0128\3\2\2\2e\u0130\3\2\2\2")
        buf.write("g\u0136\3\2\2\2i\u013a\3\2\2\2k\u0140\3\2\2\2m\u0149\3")
        buf.write("\2\2\2o\u0150\3\2\2\2q\u0155\3\2\2\2s\u015a\3\2\2\2u\u0160")
        buf.write("\3\2\2\2w\u0165\3\2\2\2y\u016b\3\2\2\2{\u016d\3\2\2\2")
        buf.write("}\u0172\3\2\2\2\177\u017c\3\2\2\2\u0081\u017e\3\2\2\2")
        buf.write("\u0083\u0185\3\2\2\2\u0085\u0189\3\2\2\2\u0087\u018c\3")
        buf.write("\2\2\2\u0089\u0190\3\2\2\2\u008b\u01a3\3\2\2\2\u008d\u01b9")
        buf.write("\3\2\2\2\u008f\u01bf\3\2\2\2\u0091\u0092\7\60\2\2\u0092")
        buf.write("\4\3\2\2\2\u0093\u0094\7.\2\2\u0094\6\3\2\2\2\u0095\u0096")
        buf.write("\7=\2\2\u0096\b\3\2\2\2\u0097\u0098\7)\2\2\u0098\n\3\2")
        buf.write("\2\2\u0099\u009a\7$\2\2\u009a\f\3\2\2\2\u009b\u009c\7")
        buf.write("<\2\2\u009c\16\3\2\2\2\u009d\u009e\7<\2\2\u009e\u009f")
        buf.write("\7<\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7%\2\2\u00a1\22\3")
        buf.write("\2\2\2\u00a2\u00a3\7*\2\2\u00a3\24\3\2\2\2\u00a4\u00a5")
        buf.write("\7+\2\2\u00a5\26\3\2\2\2\u00a6\u00a7\7]\2\2\u00a7\30\3")
        buf.write("\2\2\2\u00a8\u00a9\7_\2\2\u00a9\32\3\2\2\2\u00aa\u00ab")
        buf.write("\7}\2\2\u00ab\34\3\2\2\2\u00ac\u00ad\7\177\2\2\u00ad\36")
        buf.write("\3\2\2\2\u00ae\u00af\7>\2\2\u00af \3\2\2\2\u00b0\u00b1")
        buf.write("\7@\2\2\u00b1\"\3\2\2\2\u00b2\u00b3\7>\2\2\u00b3\u00b4")
        buf.write("\7?\2\2\u00b4$\3\2\2\2\u00b5\u00b6\7@\2\2\u00b6\u00b7")
        buf.write("\7?\2\2\u00b7&\3\2\2\2\u00b8\u00b9\7-\2\2\u00b9(\3\2\2")
        buf.write("\2\u00ba\u00bb\7/\2\2\u00bb*\3\2\2\2\u00bc\u00bd\7,\2")
        buf.write("\2\u00bd,\3\2\2\2\u00be\u00bf\7\61\2\2\u00bf.\3\2\2\2")
        buf.write("\u00c0\u00c1\7\'\2\2\u00c1\60\3\2\2\2\u00c2\u00c3\7?\2")
        buf.write("\2\u00c3\62\3\2\2\2\u00c4\u00c5\7(\2\2\u00c5\u00c6\7(")
        buf.write("\2\2\u00c6\64\3\2\2\2\u00c7\u00c8\7~\2\2\u00c8\u00c9\7")
        buf.write("~\2\2\u00c9\66\3\2\2\2\u00ca\u00cb\7#\2\2\u00cb8\3\2\2")
        buf.write("\2\u00cc\u00cd\7#\2\2\u00cd\u00ce\7?\2\2\u00ce:\3\2\2")
        buf.write("\2\u00cf\u00d0\7?\2\2\u00d0\u00d1\7?\2\2\u00d1<\3\2\2")
        buf.write("\2\u00d2\u00d3\7-\2\2\u00d3\u00d4\7-\2\2\u00d4>\3\2\2")
        buf.write("\2\u00d5\u00d6\7/\2\2\u00d6\u00d7\7/\2\2\u00d7@\3\2\2")
        buf.write("\2\u00d8\u00d9\7-\2\2\u00d9\u00da\7?\2\2\u00daB\3\2\2")
        buf.write("\2\u00db\u00dc\7/\2\2\u00dc\u00dd\7?\2\2\u00ddD\3\2\2")
        buf.write("\2\u00de\u00df\7,\2\2\u00df\u00e0\7?\2\2\u00e0F\3\2\2")
        buf.write("\2\u00e1\u00e2\7\61\2\2\u00e2\u00e3\7?\2\2\u00e3H\3\2")
        buf.write("\2\2\u00e4\u00e5\7>\2\2\u00e5\u00e6\7>\2\2\u00e6J\3\2")
        buf.write("\2\2\u00e7\u00e8\7@\2\2\u00e8\u00e9\7@\2\2\u00e9L\3\2")
        buf.write("\2\2\u00ea\u00ec\5)\25\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ec\u00f2\3\2\2\2\u00ed\u00f3\5\177@\2\u00ee")
        buf.write("\u00ef\5\177@\2\u00ef\u00f0\5\3\2\2\u00f0\u00f1\5\177")
        buf.write("@\2\u00f1\u00f3\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f2\u00ee")
        buf.write("\3\2\2\2\u00f3N\3\2\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7v\2\2\u00f7P\3\2\2\2\u00f8\u00f9")
        buf.write("\7h\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7v\2\2\u00fdR\3\2\2\2\u00fe\u00ff")
        buf.write("\7f\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7d\2\2\u0102\u0103\7n\2\2\u0103\u0104\7g\2\2\u0104T\3")
        buf.write("\2\2\2\u0105\u0106\7n\2\2\u0106\u0107\7q\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7i\2\2\u0109V\3\2\2\2\u010a\u010b")
        buf.write("\7e\2\2\u010b\u010c\7j\2\2\u010c\u010d\7c\2\2\u010d\u010e")
        buf.write("\7t\2\2\u010eX\3\2\2\2\u010f\u0110\7u\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111\u0112\7t\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7i\2\2\u0115Z\3\2\2\2\u0116\u0117")
        buf.write("\7d\2\2\u0117\u0118\7q\2\2\u0118\u0119\7q\2\2\u0119\u011a")
        buf.write("\7n\2\2\u011a\\\3\2\2\2\u011b\u011c\7x\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7k\2\2\u011e\u011f\7f\2\2\u011f^\3")
        buf.write("\2\2\2\u0120\u0121\7k\2\2\u0121\u0122\7h\2\2\u0122`\3")
        buf.write("\2\2\2\u0123\u0124\7g\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7u\2\2\u0126\u0127\7g\2\2\u0127b\3\2\2\2\u0128\u0129")
        buf.write("\7g\2\2\u0129\u012a\7n\2\2\u012a\u012b\7u\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7\"\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7h\2\2\u012fd\3\2\2\2\u0130\u0131\7y\2\2\u0131\u0132")
        buf.write("\7j\2\2\u0132\u0133\7k\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135f\3\2\2\2\u0136\u0137\7h\2\2\u0137\u0138")
        buf.write("\7q\2\2\u0138\u0139\7t\2\2\u0139h\3\2\2\2\u013a\u013b")
        buf.write("\7d\2\2\u013b\u013c\7t\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7m\2\2\u013fj\3\2\2\2\u0140\u0141")
        buf.write("\7e\2\2\u0141\u0142\7q\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7w\2\2\u0147\u0148\7g\2\2\u0148l\3\2\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7g\2\2\u014b\u014c\7v\2\2\u014c\u014d")
        buf.write("\7w\2\2\u014d\u014e\7t\2\2\u014e\u014f\7p\2\2\u014fn\3")
        buf.write("\2\2\2\u0150\u0151\7o\2\2\u0151\u0152\7c\2\2\u0152\u0153")
        buf.write("\7k\2\2\u0153\u0154\7p\2\2\u0154p\3\2\2\2\u0155\u0156")
        buf.write("\7v\2\2\u0156\u0157\7t\2\2\u0157\u0158\7w\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159r\3\2\2\2\u015a\u015b\7h\2\2\u015b\u015c")
        buf.write("\7c\2\2\u015c\u015d\7n\2\2\u015d\u015e\7u\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015ft\3\2\2\2\u0160\u0161\7e\2\2\u0161\u0162")
        buf.write("\7q\2\2\u0162\u0163\7w\2\2\u0163\u0164\7v\2\2\u0164v\3")
        buf.write("\2\2\2\u0165\u0166\7e\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168x\3\2\2\2\u0169\u016c\5q9\2\u016a\u016c\5")
        buf.write("s:\2\u016b\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016cz\3")
        buf.write("\2\2\2\u016d\u016e\7g\2\2\u016e\u016f\7p\2\2\u016f\u0170")
        buf.write("\7f\2\2\u0170\u0171\7n\2\2\u0171|\3\2\2\2\u0172\u0173")
        buf.write("\t\2\2\2\u0173~\3\2\2\2\u0174\u017d\7\62\2\2\u0175\u0179")
        buf.write("\t\3\2\2\u0176\u0178\t\2\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u0174\3")
        buf.write("\2\2\2\u017c\u0175\3\2\2\2\u017d\u0080\3\2\2\2\u017e\u0182")
        buf.write("\5\u0083B\2\u017f\u0181\5\u0085C\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3")
        buf.write("\2\2\2\u0183\u0082\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186")
        buf.write("\t\4\2\2\u0186\u0084\3\2\2\2\u0187\u018a\5}?\2\u0188\u018a")
        buf.write("\5\u0083B\2\u0189\u0187\3\2\2\2\u0189\u0188\3\2\2\2\u018a")
        buf.write("\u0086\3\2\2\2\u018b\u018d\5\u0085C\2\u018c\u018b\3\2")
        buf.write("\2\2\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0088\3\2\2\2\u0190\u0191\7%\2\2\u0191")
        buf.write("\u0192\7k\2\2\u0192\u0193\7p\2\2\u0193\u0194\7e\2\2\u0194")
        buf.write("\u0195\7n\2\2\u0195\u0196\7w\2\2\u0196\u0197\7f\2\2\u0197")
        buf.write("\u0198\7g\2\2\u0198\u0199\7>\2\2\u0199\u019a\7k\2\2\u019a")
        buf.write("\u019b\7q\2\2\u019b\u019c\7u\2\2\u019c\u019d\7v\2\2\u019d")
        buf.write("\u019e\7t\2\2\u019e\u019f\7g\2\2\u019f\u01a0\7c\2\2\u01a0")
        buf.write("\u01a1\7o\2\2\u01a1\u01a2\7@\2\2\u01a2\u008a\3\2\2\2\u01a3")
        buf.write("\u01a4\7w\2\2\u01a4\u01a5\7u\2\2\u01a5\u01a6\7k\2\2\u01a6")
        buf.write("\u01a7\7p\2\2\u01a7\u01a8\7i\2\2\u01a8\u01a9\7\"\2\2\u01a9")
        buf.write("\u01aa\7p\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac\7o\2\2\u01ac")
        buf.write("\u01ad\7g\2\2\u01ad\u01ae\7u\2\2\u01ae\u01af\7r\2\2\u01af")
        buf.write("\u01b0\7c\2\2\u01b0\u01b1\7e\2\2\u01b1\u01b2\7g\2\2\u01b2")
        buf.write("\u01b3\7\"\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5\7v\2\2\u01b5")
        buf.write("\u01b6\7f\2\2\u01b6\u01b7\7=\2\2\u01b7\u008c\3\2\2\2\u01b8")
        buf.write("\u01ba\t\5\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3")
        buf.write("\2\2\2\u01bd\u01be\bG\2\2\u01be\u008e\3\2\2\2\u01bf\u01c0")
        buf.write("\7\61\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c5\3\2\2\2\u01c2")
        buf.write("\u01c4\n\6\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u0090\3")
        buf.write("\2\2\2\u01c7\u01c5\3\2\2\2\r\2\u00eb\u00f2\u016b\u0179")
        buf.write("\u017c\u0182\u0189\u018e\u01bb\u01c5\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DOT = 1
    COMMA = 2
    SEMICOLON = 3
    APOSTROPHE = 4
    QUOTE = 5
    COLON = 6
    DOUBLE_COLON = 7
    HASH = 8
    LEFT_BRACKET = 9
    RIGHT_BRACKET = 10
    SQR_LEFT_BRACKET = 11
    SQR_RIGHT_BRACKET = 12
    CURLY_LEFT_BRACKET = 13
    CURLY_RIGHT_BRACKET = 14
    LE = 15
    GE = 16
    LEQ = 17
    GEQ = 18
    PLUS = 19
    MINUS = 20
    MUL = 21
    DIV = 22
    MOD = 23
    ASSIGN = 24
    AND = 25
    OR = 26
    NOT = 27
    NOT_EQ = 28
    EQ = 29
    PP = 30
    MM = 31
    PEQ = 32
    MINEQ = 33
    MULEQ = 34
    DIVEQ = 35
    DARRL = 36
    DARRR = 37
    NUMBER = 38
    INT = 39
    FLOAT = 40
    DOUBLE = 41
    LONG = 42
    CHAR = 43
    STRING = 44
    BOOL = 45
    VOID = 46
    IF = 47
    ELSE = 48
    ELSE_IF = 49
    WHILE = 50
    FOR = 51
    BREAK = 52
    CONTINUE = 53
    RETURN = 54
    MAIN = 55
    TRUE = 56
    FALSE = 57
    COUT = 58
    CIN = 59
    BOOLS = 60
    ENDL = 61
    DIGIT = 62
    NATURAL = 63
    ID = 64
    NONDIGIT = 65
    CHARACTER = 66
    TEXT = 67
    INCLUDE = 68
    STD = 69
    WS = 70
    COMM = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "','", "';'", "'''", "'\"'", "':'", "'::'", "'#'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", "'<='", "'>='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'&&'", "'||'", "'!'", 
            "'!='", "'=='", "'++'", "'--'", "'+='", "'-='", "'*='", "'/='", 
            "'<<'", "'>>'", "'int'", "'float'", "'double'", "'long'", "'char'", 
            "'string'", "'bool'", "'void'", "'if'", "'else'", "'else if'", 
            "'while'", "'for'", "'break'", "'continue'", "'return'", "'main'", 
            "'true'", "'false'", "'cout'", "'cin'", "'endl'", "'#include<iostream>'", 
            "'using namespace std;'" ]

    symbolicNames = [ "<INVALID>",
            "DOT", "COMMA", "SEMICOLON", "APOSTROPHE", "QUOTE", "COLON", 
            "DOUBLE_COLON", "HASH", "LEFT_BRACKET", "RIGHT_BRACKET", "SQR_LEFT_BRACKET", 
            "SQR_RIGHT_BRACKET", "CURLY_LEFT_BRACKET", "CURLY_RIGHT_BRACKET", 
            "LE", "GE", "LEQ", "GEQ", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "ASSIGN", "AND", "OR", "NOT", "NOT_EQ", "EQ", "PP", "MM", "PEQ", 
            "MINEQ", "MULEQ", "DIVEQ", "DARRL", "DARRR", "NUMBER", "INT", 
            "FLOAT", "DOUBLE", "LONG", "CHAR", "STRING", "BOOL", "VOID", 
            "IF", "ELSE", "ELSE_IF", "WHILE", "FOR", "BREAK", "CONTINUE", 
            "RETURN", "MAIN", "TRUE", "FALSE", "COUT", "CIN", "BOOLS", "ENDL", 
            "DIGIT", "NATURAL", "ID", "NONDIGIT", "CHARACTER", "TEXT", "INCLUDE", 
            "STD", "WS", "COMM" ]

    ruleNames = [ "DOT", "COMMA", "SEMICOLON", "APOSTROPHE", "QUOTE", "COLON", 
                  "DOUBLE_COLON", "HASH", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "SQR_LEFT_BRACKET", "SQR_RIGHT_BRACKET", "CURLY_LEFT_BRACKET", 
                  "CURLY_RIGHT_BRACKET", "LE", "GE", "LEQ", "GEQ", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "ASSIGN", "AND", "OR", "NOT", 
                  "NOT_EQ", "EQ", "PP", "MM", "PEQ", "MINEQ", "MULEQ", "DIVEQ", 
                  "DARRL", "DARRR", "NUMBER", "INT", "FLOAT", "DOUBLE", 
                  "LONG", "CHAR", "STRING", "BOOL", "VOID", "IF", "ELSE", 
                  "ELSE_IF", "WHILE", "FOR", "BREAK", "CONTINUE", "RETURN", 
                  "MAIN", "TRUE", "FALSE", "COUT", "CIN", "BOOLS", "ENDL", 
                  "DIGIT", "NATURAL", "ID", "NONDIGIT", "CHARACTER", "TEXT", 
                  "INCLUDE", "STD", "WS", "COMM" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


