from antlr4 import *
from traducPyJavaLexer import traducPyJavaLexer
from traducPyJavaParser import traducPyJavaParser
from traducPyJavaListener import traducPyJavaListener
from traducePyCode import traducePyCode

def main():
    with open('PyToJAva.py', 'r') as fileope:
        file_content = fileope.read()
    
    lexer = traducPyJavaLexer(InputStream(file_content))
    stream = CommonTokenStream(lexer)
    parser = traducPyJavaParser(stream)
    tree = parser.programa()

    walker = ParseTreeWalker()
    walker.walk(traducePyCode(),tree)

if __name__=='__main__':
    main()