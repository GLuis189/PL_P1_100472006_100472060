import sys
import ajson_lexer
import ply.lex as lex

file_name = sys.argv[1]
file = open(file_name, 'r')
content = file.read()

# print(content)

lexer = lex.lex(module=ajson_lexer)
lexer.input(content)
for token in lexer:
    print(token.type, token.value)