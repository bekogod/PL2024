import ply.lex as lex

reserved_keywords = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE'
}

tokens = (
    'IDENTIFIER',
    'COMMA',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'EQUAL',
    'NUMBER'
) + tuple(reserved_keywords.values())


t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_FROM = r'[Ff][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_COMMA = r'\,'
t_GREATER = r'\>'
t_LESS = r'\<'
t_GREATER_EQUAL = r'\>\='
t_LESS_EQUAL = r'\<\='
t_EQUAL = r'\='

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved_keywords.get(t.value.upper(), 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Unknown character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

print('Escreva uma frase do género:\n')
print('Select id, nome, salario From empregados Where salario >= 820\n')
input=input()
lexer.input(input)

while 1:
    token = lexer.token()
    if not token:
        break
    print (token)


