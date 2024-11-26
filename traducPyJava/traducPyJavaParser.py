# Generated from traducPyJava.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\3\4\2\4\4")
        buf.write("\7\7\2\63\2\22\3\2\2\2\4\26\3\2\2\2\6\33\3\2\2\2\b!\3")
        buf.write("\2\2\2\n%\3\2\2\2\f)\3\2\2\2\16/\3\2\2\2\20\61\3\2\2\2")
        buf.write("\22\23\5\4\3\2\23\24\5\b\5\2\24\25\5\16\b\2\25\3\3\2\2")
        buf.write("\2\26\27\7\3\2\2\27\30\7\4\2\2\30\31\5\6\4\2\31\32\7\13")
        buf.write("\2\2\32\5\3\2\2\2\33\34\7\5\2\2\34\35\t\2\2\2\35\36\7")
        buf.write("\n\2\2\36\37\t\2\2\2\37 \7\6\2\2 \7\3\2\2\2!\"\5\n\6\2")
        buf.write("\"#\7\b\2\2#$\7\4\2\2$\t\3\2\2\2%&\7\4\2\2&\'\7\17\2\2")
        buf.write("\'(\5\f\7\2(\13\3\2\2\2)*\7\4\2\2*+\7\16\2\2+,\7\4\2\2")
        buf.write(",-\7\r\2\2-.\7\4\2\2.\r\3\2\2\2/\60\5\20\t\2\60\17\3\2")
        buf.write("\2\2\61\62\7\t\2\2\62\63\7\5\2\2\63\64\7\4\2\2\64\65\7")
        buf.write("\5\2\2\65\66\7\7\2\2\66\67\7\n\2\2\678\7\7\2\289\7\6\2")
        buf.write("\29:\7\6\2\2:\21\3\2\2\2\2")
        return buf.getvalue()


class traducPyJavaParser ( Parser ):

    grammarFileName = "traducPyJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "<INVALID>", "'('", "')'", "<INVALID>", 
                     "'return'", "'print'", "','", "':'", "<INVALID>", "'-'", 
                     "'*'", "'='" ]

    symbolicNames = [ "<INVALID>", "CLASE", "NAME", "LPAREN", "RPAREN", 
                      "NUMBER", "RETURN", "PRINT", "COMA", "TWOP", "WS", 
                      "MINUS", "MULT", "EQUALS" ]

    RULE_programa = 0
    RULE_nclase = 1
    RULE_term = 2
    RULE_cuerpo = 3
    RULE_operacion = 4
    RULE_expr = 5
    RULE_main = 6
    RULE_impre = 7

    ruleNames =  [ "programa", "nclase", "term", "cuerpo", "operacion", 
                   "expr", "main", "impre" ]

    EOF = Token.EOF
    CLASE=1
    NAME=2
    LPAREN=3
    RPAREN=4
    NUMBER=5
    RETURN=6
    PRINT=7
    COMA=8
    TWOP=9
    WS=10
    MINUS=11
    MULT=12
    EQUALS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nclase(self):
            return self.getTypedRuleContext(traducPyJavaParser.NclaseContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(traducPyJavaParser.CuerpoContext,0)


        def main(self):
            return self.getTypedRuleContext(traducPyJavaParser.MainContext,0)


        def getRuleIndex(self):
            return traducPyJavaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = traducPyJavaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.nclase()
            self.state = 17
            self.cuerpo()
            self.state = 18
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NclaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASE(self):
            return self.getToken(traducPyJavaParser.CLASE, 0)

        def NAME(self):
            return self.getToken(traducPyJavaParser.NAME, 0)

        def term(self):
            return self.getTypedRuleContext(traducPyJavaParser.TermContext,0)


        def TWOP(self):
            return self.getToken(traducPyJavaParser.TWOP, 0)

        def getRuleIndex(self):
            return traducPyJavaParser.RULE_nclase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNclase" ):
                listener.enterNclase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNclase" ):
                listener.exitNclase(self)




    def nclase(self):

        localctx = traducPyJavaParser.NclaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nclase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(traducPyJavaParser.CLASE)
            self.state = 21
            self.match(traducPyJavaParser.NAME)
            self.state = 22
            self.term()
            self.state = 23
            self.match(traducPyJavaParser.TWOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(traducPyJavaParser.LPAREN, 0)

        def COMA(self):
            return self.getToken(traducPyJavaParser.COMA, 0)

        def RPAREN(self):
            return self.getToken(traducPyJavaParser.RPAREN, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(traducPyJavaParser.NUMBER)
            else:
                return self.getToken(traducPyJavaParser.NUMBER, i)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(traducPyJavaParser.NAME)
            else:
                return self.getToken(traducPyJavaParser.NAME, i)

        def getRuleIndex(self):
            return traducPyJavaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = traducPyJavaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(traducPyJavaParser.LPAREN)
            self.state = 26
            _la = self._input.LA(1)
            if not(_la==traducPyJavaParser.NAME or _la==traducPyJavaParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 27
            self.match(traducPyJavaParser.COMA)
            self.state = 28
            _la = self._input.LA(1)
            if not(_la==traducPyJavaParser.NAME or _la==traducPyJavaParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 29
            self.match(traducPyJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CuerpoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacion(self):
            return self.getTypedRuleContext(traducPyJavaParser.OperacionContext,0)


        def RETURN(self):
            return self.getToken(traducPyJavaParser.RETURN, 0)

        def NAME(self):
            return self.getToken(traducPyJavaParser.NAME, 0)

        def getRuleIndex(self):
            return traducPyJavaParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = traducPyJavaParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.operacion()
            self.state = 32
            self.match(traducPyJavaParser.RETURN)
            self.state = 33
            self.match(traducPyJavaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(traducPyJavaParser.NAME, 0)

        def EQUALS(self):
            return self.getToken(traducPyJavaParser.EQUALS, 0)

        def expr(self):
            return self.getTypedRuleContext(traducPyJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return traducPyJavaParser.RULE_operacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion" ):
                listener.enterOperacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion" ):
                listener.exitOperacion(self)




    def operacion(self):

        localctx = traducPyJavaParser.OperacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(traducPyJavaParser.NAME)
            self.state = 36
            self.match(traducPyJavaParser.EQUALS)
            self.state = 37
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(traducPyJavaParser.NAME)
            else:
                return self.getToken(traducPyJavaParser.NAME, i)

        def MULT(self):
            return self.getToken(traducPyJavaParser.MULT, 0)

        def MINUS(self):
            return self.getToken(traducPyJavaParser.MINUS, 0)

        def getRuleIndex(self):
            return traducPyJavaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = traducPyJavaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(traducPyJavaParser.NAME)
            self.state = 40
            self.match(traducPyJavaParser.MULT)
            self.state = 41
            self.match(traducPyJavaParser.NAME)
            self.state = 42
            self.match(traducPyJavaParser.MINUS)
            self.state = 43
            self.match(traducPyJavaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def impre(self):
            return self.getTypedRuleContext(traducPyJavaParser.ImpreContext,0)


        def getRuleIndex(self):
            return traducPyJavaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = traducPyJavaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.impre()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImpreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(traducPyJavaParser.PRINT, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(traducPyJavaParser.LPAREN)
            else:
                return self.getToken(traducPyJavaParser.LPAREN, i)

        def NAME(self):
            return self.getToken(traducPyJavaParser.NAME, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(traducPyJavaParser.NUMBER)
            else:
                return self.getToken(traducPyJavaParser.NUMBER, i)

        def COMA(self):
            return self.getToken(traducPyJavaParser.COMA, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(traducPyJavaParser.RPAREN)
            else:
                return self.getToken(traducPyJavaParser.RPAREN, i)

        def getRuleIndex(self):
            return traducPyJavaParser.RULE_impre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpre" ):
                listener.enterImpre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpre" ):
                listener.exitImpre(self)




    def impre(self):

        localctx = traducPyJavaParser.ImpreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_impre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(traducPyJavaParser.PRINT)
            self.state = 48
            self.match(traducPyJavaParser.LPAREN)
            self.state = 49
            self.match(traducPyJavaParser.NAME)
            self.state = 50
            self.match(traducPyJavaParser.LPAREN)
            self.state = 51
            self.match(traducPyJavaParser.NUMBER)
            self.state = 52
            self.match(traducPyJavaParser.COMA)
            self.state = 53
            self.match(traducPyJavaParser.NUMBER)
            self.state = 54
            self.match(traducPyJavaParser.RPAREN)
            self.state = 55
            self.match(traducPyJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





