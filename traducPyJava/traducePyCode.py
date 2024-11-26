from traducPyJavaListener import traducPyJavaListener
from traducPyJavaParser import *

class traducePyCode(traducPyJavaListener):
    def __init__(self):
        # Inicializa un archivo para escribir el código traducido
        self.file = open("SalidaJava.java", "w")

    # Enter a parse tree produced by traducPyJavaParser#programa.
    def enterPrograma(self, ctx:traducPyJavaParser.ProgramaContext):
         self.file.write('public class SalidaJava {\n\n')

    # Exit a parse tree produced by traducPyJavaParser#programa.
    def exitPrograma(self, ctx:traducPyJavaParser.ProgramaContext):
        self.file.write('     }\n')
        self.file.close()


    # Enter a parse tree produced by traducPyJavaParser#nclase.
    def enterNclase(self, ctx:traducPyJavaParser.NclaseContext):
        nombre_funcion = ctx.NAME().getText()
        self.file.write(f'     public static int {nombre_funcion}')

    # Exit a parse tree produced by traducPyJavaParser#nclase.
    def exitNclase(self, ctx:traducPyJavaParser.NclaseContext):
        pass


    # Enter a parse tree produced by traducPyJavaParser#term.
    def enterTerm(self, ctx:traducPyJavaParser.TermContext):
        # Extrae dinámicamente los nombres de los parámetros
        param1 = ctx.getChild(1).getText()  # Primer parámetro
        param2 = ctx.getChild(3).getText()  # Segundo parámetro
        self.file.write(f'(int {param1}, int {param2}) {{\n\n')

    # Exit a parse tree produced by traducPyJavaParser#term.
    def exitTerm(self, ctx:traducPyJavaParser.TermContext):
        pass


    # Enter a parse tree produced by traducPyJavaParser#cuerpo.
    def enterCuerpo(self, ctx:traducPyJavaParser.CuerpoContext):
       self.file.write("          int resul;\n")

    # Exit a parse tree produced by traducPyJavaParser#cuerpo.
    def exitCuerpo(self, ctx:traducPyJavaParser.CuerpoContext):
        self.file.write(f"          return resul;\n\n")
        self.file.write('   }\n')
        


    # Enter a parse tree produced by traducPyJavaParser#operacion.
    def enterOperacion(self, ctx:traducPyJavaParser.OperacionContext):
        nombre_variable = ctx.getToken(traducPyJavaParser.NAME, 0).getText()  # Obtén el primer NAME solo en asignación
        self.file.write(f'          {nombre_variable} =')

    # Exit a parse tree produced by traducPyJavaParser#operacion.
    def exitOperacion(self, ctx:traducPyJavaParser.OperacionContext):
        pass


    # Enter a parse tree produced by traducPyJavaParser#expr.
    def enterExpr(self, ctx:traducPyJavaParser.ExprContext):
        param1 = ctx.getChild(0).getText()  # Primer parámetro
        param2 = ctx.getChild(2).getText()  # Segundo parámetro
        self.file.write(f' {param1} * {param2} - {param1};\n')

    # Exit a parse tree produced by traducPyJavaParser#expr.
    def exitExpr(self, ctx:traducPyJavaParser.ExprContext):
        pass

    # Enter a parse tree produced by traducPyJavaParser#main.
    def enterMain(self, ctx:traducPyJavaParser.MainContext):
        self.file.write('     public static void main(String[] args) {\n\n')

    # Exit a parse tree produced by traducPyJavaParser#main.
    def exitMain(self, ctx:traducPyJavaParser.MainContext):
        self.file.write('     }\n');


    # Enter a parse tree produced by traducPyJavaParser#impre.
    def enterImpre(self, ctx:traducPyJavaParser.ImpreContext):
        nombre_funcion = ctx.getChild(3).getText() 
        param1 = ctx.getChild(5).getText()  # Primer parámetro
        param2 = ctx.getChild(7).getText()  # Segundo parámetro
        self.file.write(f'        System.out.println({nombre_funcion}({param1}, {param2})); \n');

    # Exit a parse tree produced by traducPyJavaParser#impre.
    def exitImpre(self, ctx:traducPyJavaParser.ImpreContext):
        pass