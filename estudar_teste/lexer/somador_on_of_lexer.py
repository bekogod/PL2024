import ply.lex as lex

tokens = (
    'ON',
    'OFF',
    'NBR',
    'EQUALS'
)
states = (
    ('ITSON', 'inclusive'),
    ('ITSOFF', 'inclusive')
)


def t_ON (t):
    r'[oO][nN]'
    t.lexer.begin('ITSON')
    return t

def t_OFF (t):
    r'[Oo][fF][Ff]'
    t.lexer.begin('ITSOFF')
    return t

def t_ITSON_NBR (t):
    r'\d+'
    t.lexer.soma += int(t.value)
    return t

def t_ITSOFF_NBR (t):
    r'\d+'
    return t


def t_EQUALS(t):
    r"="
    print("Soma:", t.lexer.soma)
    return t



t_ignore = r' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


def t_qualquer_coisa (t):
    r'.+?'
    pass

lexer = lex.lex()

lexer.soma = 0
lexer.begin('ITSON')

lexer.input("""vamos somar numeros: 3 e 5 e 10 e 2
vamos parar agora: OFF 
mais números: 7 1 9 3 10 20
e ver o resultado: =
""")

while tok := lexer.token():
    # print(tok)
    pass