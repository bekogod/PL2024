import ply.lex as lex

tokens = (
    'ON',
    'OFF',
    'NUMBER',
    'EQUALS'
)

states = (
    ('COUNTOFF', 'inclusive'),
    ('COUNTON', 'inclusive')
)

def t_ON(t):
    r"(?i:on)"
    t.lexer.begin('COUNTON')
    return t

def t_OFF(t):
    r"(?i:off)"
    t.lexer.begin('COUNTOFF')
    return t

def t_COUNTON_NUMBER(t):
    r"\d+"
    t.lexer.soma += int(t.value)
    return t

def t_COUNTOFF_NUMBER(t):
    r"\d+"
    return t

def t_EQUALS(t):
    r"="
    print("Soma:", t.lexer.soma)
    return t

def t_qualqueroutracoisa(t):
    r".+?"
    pass

t_ignore = " \t\n"

lexer = lex.lex()

lexer.soma = 0
lexer.begin('COUNTON')

lexer.input("""vamos somar numeros: 3 e 5 e 10 e 2
vamos parar agora: OFF 
mais números: 7 1 9 3 10 20
e ver o resultado: =
""")

while tok := lexer.token():
    # print(tok)
    pass