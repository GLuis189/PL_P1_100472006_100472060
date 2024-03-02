import ply.yacc as yacc
from tokens import Tokens

tokens = Tokens.tokens

def p_programa(p):
    '''programa : LLAVE_ABRE lista LLAVE_CIERRA
                | LLAVE_ABRE LLAVE_CIERRA'''


def p_lista(p):
    '''lista : elemento
             | elemento COMA 
             | elemento COMA lista'''

def p_elemento(p):
    '''elemento : CADENA_NO_COMILLAS DOS_PUNTOS valor
                | CADENA_COMILLAS DOS_PUNTOS valor
                | NULO'''

def p_valor(p):
    '''valor : CADENA_COMILLAS
             | NUMERO
             | comparacion
             | TRUE
             | FALSE
             | NULO
             | programa'''

def p_comparacion(p):
    '''comparacion : NUMERO MAYOR NUMERO
                   | NUMERO MENOR NUMERO
                   | NUMERO MAYOR_IGUAL NUMERO
                   | NUMERO MENOR_IGUAL NUMERO
                   | NUMERO IGUAL NUMERO'''
    
def p_error(p):
    if p.value : print("Syntax error at '%s'" % p.value)
    else : print("Syntax error at EOF")
