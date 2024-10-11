import ply.lex as lex

tokens = (
    'NBR',
    'PALAVRAS',
    'BOOL',
    'NBR_DECIMAL',
)

literals = [",", "[", "]"]

t_NBR = r'\d+'
t_PALAVRAS = r'\w+'
t_BOOL = r'([fF][aA][lL][sS][eE]|[Tt][rR][uU][eE])'
t_NBR_DECIMAL = r'\d+\.\d+'


t_ignore = r' \n\t'

def t_error(t):
    print(f"Caracter Ilegal{t.value[0]}")
    t.lexer.skip(1)

input = "[ 1,5, palavra, False ,3.14, 0, fim]"
lexer = lex.lex()
lex.input(input)
while tok := lexer.token():
    print(tok)


