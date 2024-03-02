import sys
import ajson_lexer
import ajson_parser
import ply.lex as lex
import ply.yacc as yacc

file_name = sys.argv[1]
file = open(file_name, 'r')
content = file.read()

# print(content)

lexer = lex.lex(module=ajson_lexer)
lexer.input(content)
for token in lexer:
    print(token.type, token.value)

parser = yacc.yacc(module=ajson_parser)
result = parser.parse(content, lexer=lexer)
print(result)