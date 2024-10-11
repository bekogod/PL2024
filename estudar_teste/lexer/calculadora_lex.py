import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_LPAREN = r"\("
t_RPAREN = r"\)"

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

frase = """4 * (2 + 3)
3 / 5
"""

lexer.input(frase)

while tok := lexer.token():
    print(tok)