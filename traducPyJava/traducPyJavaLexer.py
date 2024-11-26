# Generated from traducPyJava.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\3\3\3\7\3$\n\3\f\3\16\3\'\13\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\6\6.\n\6\r\6\16\6/\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\6\13D\n\13\r\13\16\13E\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\3\2\6\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\5\2\13\f\17\17\"\"\2Q\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5!")
        buf.write("\3\2\2\2\7(\3\2\2\2\t*\3\2\2\2\13-\3\2\2\2\r\61\3\2\2")
        buf.write("\2\178\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25C\3\2\2\2\27")
        buf.write("I\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2\35\36\7f\2\2\36\37\7")
        buf.write("g\2\2\37 \7h\2\2 \4\3\2\2\2!%\t\2\2\2\"$\t\3\2\2#\"\3")
        buf.write("\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\6\3\2\2\2\'%\3")
        buf.write("\2\2\2()\7*\2\2)\b\3\2\2\2*+\7+\2\2+\n\3\2\2\2,.\t\4\2")
        buf.write("\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\f\3\2")
        buf.write("\2\2\61\62\7t\2\2\62\63\7g\2\2\63\64\7v\2\2\64\65\7w\2")
        buf.write("\2\65\66\7t\2\2\66\67\7p\2\2\67\16\3\2\2\289\7r\2\29:")
        buf.write("\7t\2\2:;\7k\2\2;<\7p\2\2<=\7v\2\2=\20\3\2\2\2>?\7.\2")
        buf.write("\2?\22\3\2\2\2@A\7<\2\2A\24\3\2\2\2BD\t\5\2\2CB\3\2\2")
        buf.write("\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\13\2\2")
        buf.write("H\26\3\2\2\2IJ\7/\2\2J\30\3\2\2\2KL\7,\2\2L\32\3\2\2\2")
        buf.write("MN\7?\2\2N\34\3\2\2\2\6\2%/E\3\b\2\2")
        return buf.getvalue()


class traducPyJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASE = 1
    NAME = 2
    LPAREN = 3
    RPAREN = 4
    NUMBER = 5
    RETURN = 6
    PRINT = 7
    COMA = 8
    TWOP = 9
    WS = 10
    MINUS = 11
    MULT = 12
    EQUALS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "'return'", "'print'", "','", "':'", 
            "'-'", "'*'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "CLASE", "NAME", "LPAREN", "RPAREN", "NUMBER", "RETURN", "PRINT", 
            "COMA", "TWOP", "WS", "MINUS", "MULT", "EQUALS" ]

    ruleNames = [ "CLASE", "NAME", "LPAREN", "RPAREN", "NUMBER", "RETURN", 
                  "PRINT", "COMA", "TWOP", "WS", "MINUS", "MULT", "EQUALS" ]

    grammarFileName = "traducPyJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


