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
        buf.write("\u01c6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\5(\u00ef")
        buf.write("\n(\3(\3(\3(\3(\3(\5(\u00f6\n(\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3")
        buf.write(">\3>\5>\u0173\n>\3?\3?\3?\3?\3?\3@\3@\3A\3A\3A\7A\u017f")
        buf.write("\nA\fA\16A\u0182\13A\5A\u0184\nA\3B\3B\7B\u0188\nB\fB")
        buf.write("\16B\u018b\13B\3C\3C\3D\3D\5D\u0191\nD\3E\6E\u0194\nE")
        buf.write("\rE\16E\u0195\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\3G\3G\3G\3H\6H\u01c1\nH\rH\16H\u01c2")
        buf.write("\3H\3H\2\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\3\2\6\3\2\62;\3\2\63;\5")
        buf.write("\2C\\aac|\5\2\13\f\17\17\"\"\2\u01ce\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0093")
        buf.write("\3\2\2\2\7\u0095\3\2\2\2\t\u0097\3\2\2\2\13\u0099\3\2")
        buf.write("\2\2\r\u009b\3\2\2\2\17\u009d\3\2\2\2\21\u00a0\3\2\2\2")
        buf.write("\23\u00a2\3\2\2\2\25\u00a5\3\2\2\2\27\u00a7\3\2\2\2\31")
        buf.write("\u00a9\3\2\2\2\33\u00ab\3\2\2\2\35\u00ad\3\2\2\2\37\u00af")
        buf.write("\3\2\2\2!\u00b1\3\2\2\2#\u00b3\3\2\2\2%\u00b5\3\2\2\2")
        buf.write("\'\u00b8\3\2\2\2)\u00bb\3\2\2\2+\u00bd\3\2\2\2-\u00bf")
        buf.write("\3\2\2\2/\u00c1\3\2\2\2\61\u00c3\3\2\2\2\63\u00c5\3\2")
        buf.write("\2\2\65\u00c7\3\2\2\2\67\u00ca\3\2\2\29\u00cd\3\2\2\2")
        buf.write(";\u00cf\3\2\2\2=\u00d2\3\2\2\2?\u00d5\3\2\2\2A\u00d8\3")
        buf.write("\2\2\2C\u00db\3\2\2\2E\u00de\3\2\2\2G\u00e1\3\2\2\2I\u00e4")
        buf.write("\3\2\2\2K\u00e7\3\2\2\2M\u00ea\3\2\2\2O\u00ee\3\2\2\2")
        buf.write("Q\u00f7\3\2\2\2S\u00fb\3\2\2\2U\u0101\3\2\2\2W\u0108\3")
        buf.write("\2\2\2Y\u010d\3\2\2\2[\u0112\3\2\2\2]\u0119\3\2\2\2_\u011e")
        buf.write("\3\2\2\2a\u0123\3\2\2\2c\u0126\3\2\2\2e\u012b\3\2\2\2")
        buf.write("g\u0133\3\2\2\2i\u0139\3\2\2\2k\u013d\3\2\2\2m\u0143\3")
        buf.write("\2\2\2o\u014c\3\2\2\2q\u0153\3\2\2\2s\u0158\3\2\2\2u\u015d")
        buf.write("\3\2\2\2w\u0163\3\2\2\2y\u016a\3\2\2\2{\u0172\3\2\2\2")
        buf.write("}\u0174\3\2\2\2\177\u0179\3\2\2\2\u0081\u0183\3\2\2\2")
        buf.write("\u0083\u0185\3\2\2\2\u0085\u018c\3\2\2\2\u0087\u0190\3")
        buf.write("\2\2\2\u0089\u0193\3\2\2\2\u008b\u0197\3\2\2\2\u008d\u01aa")
        buf.write("\3\2\2\2\u008f\u01c0\3\2\2\2\u0091\u0092\7\60\2\2\u0092")
        buf.write("\4\3\2\2\2\u0093\u0094\7.\2\2\u0094\6\3\2\2\2\u0095\u0096")
        buf.write("\7=\2\2\u0096\b\3\2\2\2\u0097\u0098\7)\2\2\u0098\n\3\2")
        buf.write("\2\2\u0099\u009a\7$\2\2\u009a\f\3\2\2\2\u009b\u009c\7")
        buf.write("<\2\2\u009c\16\3\2\2\2\u009d\u009e\7<\2\2\u009e\u009f")
        buf.write("\7<\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7%\2\2\u00a1\22\3")
        buf.write("\2\2\2\u00a2\u00a3\7\61\2\2\u00a3\u00a4\7\61\2\2\u00a4")
        buf.write("\24\3\2\2\2\u00a5\u00a6\7*\2\2\u00a6\26\3\2\2\2\u00a7")
        buf.write("\u00a8\7+\2\2\u00a8\30\3\2\2\2\u00a9\u00aa\7]\2\2\u00aa")
        buf.write("\32\3\2\2\2\u00ab\u00ac\7_\2\2\u00ac\34\3\2\2\2\u00ad")
        buf.write("\u00ae\7}\2\2\u00ae\36\3\2\2\2\u00af\u00b0\7\177\2\2\u00b0")
        buf.write(" \3\2\2\2\u00b1\u00b2\7>\2\2\u00b2\"\3\2\2\2\u00b3\u00b4")
        buf.write("\7@\2\2\u00b4$\3\2\2\2\u00b5\u00b6\7>\2\2\u00b6\u00b7")
        buf.write("\7?\2\2\u00b7&\3\2\2\2\u00b8\u00b9\7@\2\2\u00b9\u00ba")
        buf.write("\7?\2\2\u00ba(\3\2\2\2\u00bb\u00bc\7-\2\2\u00bc*\3\2\2")
        buf.write("\2\u00bd\u00be\7/\2\2\u00be,\3\2\2\2\u00bf\u00c0\7,\2")
        buf.write("\2\u00c0.\3\2\2\2\u00c1\u00c2\7\61\2\2\u00c2\60\3\2\2")
        buf.write("\2\u00c3\u00c4\7\'\2\2\u00c4\62\3\2\2\2\u00c5\u00c6\7")
        buf.write("?\2\2\u00c6\64\3\2\2\2\u00c7\u00c8\7(\2\2\u00c8\u00c9")
        buf.write("\7(\2\2\u00c9\66\3\2\2\2\u00ca\u00cb\7~\2\2\u00cb\u00cc")
        buf.write("\7~\2\2\u00cc8\3\2\2\2\u00cd\u00ce\7#\2\2\u00ce:\3\2\2")
        buf.write("\2\u00cf\u00d0\7#\2\2\u00d0\u00d1\7?\2\2\u00d1<\3\2\2")
        buf.write("\2\u00d2\u00d3\7?\2\2\u00d3\u00d4\7?\2\2\u00d4>\3\2\2")
        buf.write("\2\u00d5\u00d6\7-\2\2\u00d6\u00d7\7-\2\2\u00d7@\3\2\2")
        buf.write("\2\u00d8\u00d9\7/\2\2\u00d9\u00da\7/\2\2\u00daB\3\2\2")
        buf.write("\2\u00db\u00dc\7-\2\2\u00dc\u00dd\7?\2\2\u00ddD\3\2\2")
        buf.write("\2\u00de\u00df\7/\2\2\u00df\u00e0\7?\2\2\u00e0F\3\2\2")
        buf.write("\2\u00e1\u00e2\7,\2\2\u00e2\u00e3\7?\2\2\u00e3H\3\2\2")
        buf.write("\2\u00e4\u00e5\7\61\2\2\u00e5\u00e6\7?\2\2\u00e6J\3\2")
        buf.write("\2\2\u00e7\u00e8\7>\2\2\u00e8\u00e9\7>\2\2\u00e9L\3\2")
        buf.write("\2\2\u00ea\u00eb\7@\2\2\u00eb\u00ec\7@\2\2\u00ecN\3\2")
        buf.write("\2\2\u00ed\u00ef\5+\26\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef\u00f5\3\2\2\2\u00f0\u00f6\5\u0081A\2\u00f1")
        buf.write("\u00f2\5\u0081A\2\u00f2\u00f3\5\3\2\2\u00f3\u00f4\5\u0081")
        buf.write("A\2\u00f4\u00f6\3\2\2\2\u00f5\u00f0\3\2\2\2\u00f5\u00f1")
        buf.write("\3\2\2\2\u00f6P\3\2\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7v\2\2\u00faR\3\2\2\2\u00fb\u00fc")
        buf.write("\7h\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7v\2\2\u0100T\3\2\2\2\u0101\u0102")
        buf.write("\7f\2\2\u0102\u0103\7q\2\2\u0103\u0104\7w\2\2\u0104\u0105")
        buf.write("\7d\2\2\u0105\u0106\7n\2\2\u0106\u0107\7g\2\2\u0107V\3")
        buf.write("\2\2\2\u0108\u0109\7n\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7p\2\2\u010b\u010c\7i\2\2\u010cX\3\2\2\2\u010d\u010e")
        buf.write("\7e\2\2\u010e\u010f\7j\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111Z\3\2\2\2\u0112\u0113\7u\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114\u0115\7t\2\2\u0115\u0116\7k\2\2\u0116\u0117")
        buf.write("\7p\2\2\u0117\u0118\7i\2\2\u0118\\\3\2\2\2\u0119\u011a")
        buf.write("\7d\2\2\u011a\u011b\7q\2\2\u011b\u011c\7q\2\2\u011c\u011d")
        buf.write("\7n\2\2\u011d^\3\2\2\2\u011e\u011f\7x\2\2\u011f\u0120")
        buf.write("\7q\2\2\u0120\u0121\7k\2\2\u0121\u0122\7f\2\2\u0122`\3")
        buf.write("\2\2\2\u0123\u0124\7k\2\2\u0124\u0125\7h\2\2\u0125b\3")
        buf.write("\2\2\2\u0126\u0127\7g\2\2\u0127\u0128\7n\2\2\u0128\u0129")
        buf.write("\7u\2\2\u0129\u012a\7g\2\2\u012ad\3\2\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7n\2\2\u012d\u012e\7u\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\u0130\7\"\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7h\2\2\u0132f\3\2\2\2\u0133\u0134\7y\2\2\u0134\u0135")
        buf.write("\7j\2\2\u0135\u0136\7k\2\2\u0136\u0137\7n\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138h\3\2\2\2\u0139\u013a\7h\2\2\u013a\u013b")
        buf.write("\7q\2\2\u013b\u013c\7t\2\2\u013cj\3\2\2\2\u013d\u013e")
        buf.write("\7d\2\2\u013e\u013f\7t\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7c\2\2\u0141\u0142\7m\2\2\u0142l\3\2\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7q\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7k\2\2\u0148\u0149\7p\2\2\u0149\u014a")
        buf.write("\7w\2\2\u014a\u014b\7g\2\2\u014bn\3\2\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7g\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7w\2\2\u0150\u0151\7t\2\2\u0151\u0152\7p\2\2\u0152p\3")
        buf.write("\2\2\2\u0153\u0154\7o\2\2\u0154\u0155\7c\2\2\u0155\u0156")
        buf.write("\7k\2\2\u0156\u0157\7p\2\2\u0157r\3\2\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7t\2\2\u015a\u015b\7w\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015ct\3\2\2\2\u015d\u015e\7h\2\2\u015e\u015f")
        buf.write("\7c\2\2\u015f\u0160\7n\2\2\u0160\u0161\7u\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162v\3\2\2\2\u0163\u0164\7e\2\2\u0164\u0165")
        buf.write("\7q\2\2\u0165\u0166\7w\2\2\u0166\u0167\7v\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u0169\5K&\2\u0169x\3\2\2\2\u016a\u016b")
        buf.write("\7e\2\2\u016b\u016c\7k\2\2\u016c\u016d\7p\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016f\5M\'\2\u016fz\3\2\2\2\u0170\u0173")
        buf.write("\5s:\2\u0171\u0173\5u;\2\u0172\u0170\3\2\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173|\3\2\2\2\u0174\u0175\7g\2\2\u0175\u0176")
        buf.write("\7p\2\2\u0176\u0177\7f\2\2\u0177\u0178\7n\2\2\u0178~\3")
        buf.write("\2\2\2\u0179\u017a\t\2\2\2\u017a\u0080\3\2\2\2\u017b\u0184")
        buf.write("\7\62\2\2\u017c\u0180\t\3\2\2\u017d\u017f\t\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3")
        buf.write("\2\2\2\u0183\u017b\3\2\2\2\u0183\u017c\3\2\2\2\u0184\u0082")
        buf.write("\3\2\2\2\u0185\u0189\5\u0085C\2\u0186\u0188\5\u0087D\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u0189\u018a\3\2\2\2\u018a\u0084\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018c\u018d\t\4\2\2\u018d\u0086\3\2\2\2\u018e")
        buf.write("\u0191\5\177@\2\u018f\u0191\5\u0085C\2\u0190\u018e\3\2")
        buf.write("\2\2\u0190\u018f\3\2\2\2\u0191\u0088\3\2\2\2\u0192\u0194")
        buf.write("\5\u0087D\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u008a\3\2\2\2")
        buf.write("\u0197\u0198\7%\2\2\u0198\u0199\7k\2\2\u0199\u019a\7p")
        buf.write("\2\2\u019a\u019b\7e\2\2\u019b\u019c\7n\2\2\u019c\u019d")
        buf.write("\7w\2\2\u019d\u019e\7f\2\2\u019e\u019f\7g\2\2\u019f\u01a0")
        buf.write("\7>\2\2\u01a0\u01a1\7k\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3")
        buf.write("\7u\2\2\u01a3\u01a4\7v\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6")
        buf.write("\7g\2\2\u01a6\u01a7\7c\2\2\u01a7\u01a8\7o\2\2\u01a8\u01a9")
        buf.write("\7@\2\2\u01a9\u008c\3\2\2\2\u01aa\u01ab\7w\2\2\u01ab\u01ac")
        buf.write("\7u\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae\7p\2\2\u01ae\u01af")
        buf.write("\7i\2\2\u01af\u01b0\7\"\2\2\u01b0\u01b1\7p\2\2\u01b1\u01b2")
        buf.write("\7c\2\2\u01b2\u01b3\7o\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5")
        buf.write("\7u\2\2\u01b5\u01b6\7r\2\2\u01b6\u01b7\7c\2\2\u01b7\u01b8")
        buf.write("\7e\2\2\u01b8\u01b9\7g\2\2\u01b9\u01ba\7\"\2\2\u01ba\u01bb")
        buf.write("\7u\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd\7f\2\2\u01bd\u01be")
        buf.write("\7=\2\2\u01be\u008e\3\2\2\2\u01bf\u01c1\t\5\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c3\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b")
        buf.write("H\2\2\u01c5\u0090\3\2\2\2\f\2\u00ee\u00f5\u0172\u0180")
        buf.write("\u0183\u0189\u0190\u0195\u01c2\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    DOT = 1
    COMMA = 2
    SEMICOLON = 3
    APOSTROPHE = 4
    QUOTE = 5
    COLON = 6
    DOUBLE_COLON = 7
    HASH = 8
    COMMENTS = 9
    LEFT_BRACKET = 10
    RIGHT_BRACKET = 11
    SQR_LEFT_BRACKET = 12
    SQR_RIGHT_BRACKET = 13
    CURLY_LEFT_BRACKET = 14
    CURLY_RIGHT_BRACKET = 15
    LE = 16
    GE = 17
    LEQ = 18
    GEQ = 19
    PLUS = 20
    MINUS = 21
    MUL = 22
    DIV = 23
    MOD = 24
    ASSIGN = 25
    AND = 26
    OR = 27
    NOT = 28
    NOT_EQ = 29
    EQ = 30
    PP = 31
    MM = 32
    PEQ = 33
    MINEQ = 34
    MULEQ = 35
    DIVEQ = 36
    DARRL = 37
    DARRR = 38
    NUMBER = 39
    INT = 40
    FLOAT = 41
    DOUBLE = 42
    LONG = 43
    CHAR = 44
    STRING = 45
    BOOL = 46
    VOID = 47
    IF = 48
    ELSE = 49
    ELSE_IF = 50
    WHILE = 51
    FOR = 52
    BREAK = 53
    CONTINUE = 54
    RETURN = 55
    MAIN = 56
    TRUE = 57
    FALSE = 58
    COUT = 59
    CIN = 60
    BOOLS = 61
    ENDL = 62
    DIGIT = 63
    NATURAL = 64
    ID = 65
    NONDIGIT = 66
    CHARACTER = 67
    TEXT = 68
    INCLUDE = 69
    STD = 70
    WS = 71

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'.'", "','", "';'", "'''", "'\"'", "':'", "'::'", "'#'", "'//'",
                    "'('", "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", "'<='",
                    "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'&&'", "'||'",
                    "'!'", "'!='", "'=='", "'++'", "'--'", "'+='", "'-='", "'*='",
                    "'/='", "'<<'", "'>>'", "'int'", "'float'", "'double'", "'long'",
                    "'char'", "'string'", "'bool'", "'void'", "'if'", "'else'",
                    "'else if'", "'while'", "'for'", "'break'", "'continue'", "'return'",
                    "'main'", "'true'", "'false'", "'endl'", "'#include<iostream>'",
                    "'using namespace std;'"]

    symbolicNames = ["<INVALID>",
                     "DOT", "COMMA", "SEMICOLON", "APOSTROPHE", "QUOTE", "COLON",
                     "DOUBLE_COLON", "HASH", "COMMENTS", "LEFT_BRACKET", "RIGHT_BRACKET",
                     "SQR_LEFT_BRACKET", "SQR_RIGHT_BRACKET", "CURLY_LEFT_BRACKET",
                     "CURLY_RIGHT_BRACKET", "LE", "GE", "LEQ", "GEQ", "PLUS", "MINUS",
                     "MUL", "DIV", "MOD", "ASSIGN", "AND", "OR", "NOT", "NOT_EQ",
                     "EQ", "PP", "MM", "PEQ", "MINEQ", "MULEQ", "DIVEQ", "DARRL",
                     "DARRR", "NUMBER", "INT", "FLOAT", "DOUBLE", "LONG", "CHAR",
                     "STRING", "BOOL", "VOID", "IF", "ELSE", "ELSE_IF", "WHILE",
                     "FOR", "BREAK", "CONTINUE", "RETURN", "MAIN", "TRUE", "FALSE",
                     "COUT", "CIN", "BOOLS", "ENDL", "DIGIT", "NATURAL", "ID", "NONDIGIT",
                     "CHARACTER", "TEXT", "INCLUDE", "STD", "WS"]

    ruleNames = ["DOT", "COMMA", "SEMICOLON", "APOSTROPHE", "QUOTE", "COLON",
                 "DOUBLE_COLON", "HASH", "COMMENTS", "LEFT_BRACKET", "RIGHT_BRACKET",
                 "SQR_LEFT_BRACKET", "SQR_RIGHT_BRACKET", "CURLY_LEFT_BRACKET",
                 "CURLY_RIGHT_BRACKET", "LE", "GE", "LEQ", "GEQ", "PLUS",
                 "MINUS", "MUL", "DIV", "MOD", "ASSIGN", "AND", "OR", "NOT",
                 "NOT_EQ", "EQ", "PP", "MM", "PEQ", "MINEQ", "MULEQ", "DIVEQ",
                 "DARRL", "DARRR", "NUMBER", "INT", "FLOAT", "DOUBLE",
                 "LONG", "CHAR", "STRING", "BOOL", "VOID", "IF", "ELSE",
                 "ELSE_IF", "WHILE", "FOR", "BREAK", "CONTINUE", "RETURN",
                 "MAIN", "TRUE", "FALSE", "COUT", "CIN", "BOOLS", "ENDL",
                 "DIGIT", "NATURAL", "ID", "NONDIGIT", "CHARACTER", "TEXT",
                 "INCLUDE", "STD", "WS"]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
