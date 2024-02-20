# module: ajson_lexer.py

import ply.lex as lex

tokens = [
    "LLAVE_ABRE",
    "LLAVE_CIERRA",
    "COMA",
    "DOS_PUNTOS",
    "NUMERO",
    "CADENA_COMILLAS",
    "CADENA_NO_COMILLAS",
    "TRUE",
    "FALSE",
    "NULO",
    "IGUAL",
    "MAYOR",
    "MENOR",
    "MAYOR_IGUAL",
    "MENOR_IGUAL",
    # "ENTERO",
    # "DECIMAL",
    # "CIENTIFICO",
    # "BINARIO",
    # "OCTAL",
    # "HEXADECIMAL"
    "NUMERO"
]

t_LLAVE_ABRE = r"\{"
t_LLAVE_CIERRA = r"\}"
t_COMA = r","
t_DOS_PUNTOS = r":"
t_IGUAL = r"=="
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYOR_IGUAL = r">="
t_MENOR_IGUAL = r"<="
t_CADENA_NO_COMILLAS = r"[a-zA-Z_][a-zA-Z_0-9]*"

def t_CADENA_COMILLAS(t):
    r"\"[^\"]*\""
    t.value = t.value[1:-1]
    return t

def t_TRUE(t):
    r"TR"
    t.value = True
    return t

def t_FALSE(t):
    r"FL"
    t.value = False
    return t

def t_NULO(t):
    r"NULL"
    t.value = None
    return t

# def t_BINARIO(t):
#     r"0(b|B)[01]+"
#     t.value = int(t.value, 2)
#     return t

# def t_HEXADECIMAL(t):
#     r"0(x|X)[0-9a-fA-F]+"
#     t.value = int(t.value, 16)
#     return t

# def t_OCTAL(t):
#     r"0[0-7]+"
#     t.value = int(t.value, 8)
#     return t

# def t_CIENTIFICO(t):
#     r"-?((\d+\.\d+)|(\.\d+)|(\d))[eE]-?\d+"
#     t.value = float(t.value)
#     return t

# def t_DECIMAL(t):
#     r"-?(\d+\.\d+)|(\.\d+)"
#     t.value = float(t.value)
#     return t

# def t_ENTERO(t):
#     r"-?\d+"
#     t.value = int(t.value)
#     return t

entero = r"-?\d+"
decimal = r"-?(\d+\.\d+)|(\.\d+)"
cientifico = r"-?((\d+\.\d+)|(\.\d+)|(\d))[eE]-?\d+"
binario = r"0(b|B)[01]+"
octal = r"0[0-7]+"
hexadecimal = r"0(x|X)[0-9a-fA-F]+"
numero = r"|".join([ binario, hexadecimal, cientifico, decimal, entero, octal])

@lex.TOKEN(numero)
def t_NUMERO(t):
    if t.value.startswith("0b") or t.value.startswith("0B"):
        t.value = int(t.value, 2)
    elif t.value.startswith("0x") or t.value.startswith("0X"):
        t.value = int(t.value, 16)
    elif t.value.startswith("0") and all(c in '01234567' for c in t.value[1:]):
        t.value = int(t.value, 8)
    elif "." in t.value or "e" in t.value or "E" in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)