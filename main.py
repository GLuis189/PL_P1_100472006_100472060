import sys
import ajson_lexer
import ajson_parser
import ply.lex as lex
import ply.yacc as yacc

file_name = sys.argv[1]
file = open(file_name, 'r')
content = file.read()

def print_salida(result):
    if not result:
        print(f'>> FICHERO AJSON VACIO "{sys.argv[1]}" ')
        return
    print(f'>> FICHERO AJSON "{sys.argv[1]}" ')
    for key, value in result.items():
        if isinstance(value, dict) or isinstance(value, list):
            _print_salida(value, str(key))
        else:
            print("  { " + key + " : " + str(value) + " }")

def _print_salida(result, origen):
    if isinstance(result, dict):
        for key, value in result.items():
            if isinstance(value, dict) or isinstance(value, list):
                _print_salida(value, origen + "." + str(key) )
            else:
                print("  { " + origen + "." + key + ": " + str(value) + " }")
    if isinstance(result, list):
        for i, item in enumerate(result):
            if isinstance(item, dict) or isinstance(item, list):
                _print_salida(item, str(origen) + "." + str(i))
            else:
                print("  { " + str(origen) + "." + str(i) + " : " + str(item) + " }")



# print(content)
if len(sys.argv) < 3:
    lexer = lex.lex(module=ajson_lexer)
    lexer.input(content)
    for token in lexer:
        print(token.type, token.value)
    parser = yacc.yacc(module=ajson_parser)
    result = parser.parse(content, lexer=lexer)
    print_salida(result)
elif sys.argv[2] and sys.argv[2] == 'lexer':
    lexer = lex.lex(module=ajson_lexer)
    lexer.input(content)
    for token in lexer:
        print(token.type, token.value)

elif sys.argv[2] and sys.argv[2] == 'parser':
    lexer = lex.lex(module=ajson_lexer)
    lexer.input(content)
    parser = yacc.yacc(module=ajson_parser)
    result = parser.parse(content, lexer=lexer)
    print_salida(result)
else:
    print("Invalid command")
    