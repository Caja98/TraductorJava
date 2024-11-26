grammar traducPyJava;

// Lexer rules;

CLASE: 'def';
NAME: [a-zA-Z_][a-zA-Z0-9_]*;
LPAREN: '(';
RPAREN: ')';
NUMBER: [0-9]+;
RETURN: 'return';
PRINT: 'print';
COMA : ',';
TWOP : ':';
WS: [ \t\r\n]+ ->skip;

//Operators
MINUS: '-';
MULT: '*';
EQUALS: '=';

//Parser rules
programa
    : nclase cuerpo main
    ;

nclase
    : CLASE NAME term TWOP
    ;

term
    : LPAREN (NUMBER | NAME) COMA (NUMBER | NAME) RPAREN
    ;

cuerpo
    : operacion RETURN NAME
    ;

operacion
    : NAME EQUALS expr
    ;

expr
    : NAME MULT NAME MINUS NAME
    ;
    
main
    : impre
    ;

impre
    : PRINT LPAREN NAME LPAREN NUMBER COMA NUMBER RPAREN RPAREN
    ;

