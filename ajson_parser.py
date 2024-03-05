import ply.yacc as yacc
from tokens import Tokens

tokens = Tokens.tokens + Tokens.reserved

def p_programa(p):
    '''programa : ajson
                | empty'''
    p[0] = p[1]
    
def p_ajson(p):
    '''ajson : LLAVE_ABRE lista LLAVE_CIERRA
             | LLAVE_ABRE LLAVE_CIERRA'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = None

def p_lista(p):
    '''lista : elemento
             | elemento COMA 
             | elemento COMA lista'''
    if len(p) == 2 or len(p) == 3:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = {**p[1], **p[3]}

def p_elemento(p):
    '''elemento : CADENA_NO_COMILLAS DOS_PUNTOS valor
                | CADENA_COMILLAS DOS_PUNTOS valor'''
    p[0] = {p[1]: p[3]}

def p_valor(p):
    '''valor : CADENA_COMILLAS
             | NUMERO
             | comparacion
             | TR
             | FL
             | NULL
             | ajson
             | array'''
    p[0] = p[1]

def p_comparacion(p):
    '''comparacion : NUMERO MAYOR NUMERO
                   | NUMERO MENOR NUMERO
                   | NUMERO MAYOR_IGUAL NUMERO
                   | NUMERO MENOR_IGUAL NUMERO
                   | NUMERO IGUAL NUMERO'''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]

def p_array(p):
    '''array : CORCHETE_ABRE lista_array CORCHETE_CIERRA
             | CORCHETE_ABRE CORCHETE_CIERRA'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = None

def p_lista_array(p):
    '''lista_array : ajson
                   | ajson COMA
                   | ajson COMA lista_array'''
    if len(p) == 2 or len(p) == 3:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p.value : print("Syntax error at '%s'" % p.value)
    else : print("Syntax error at EOF")
