import ply.lex as lex

tokens = (
    'NAME',
    'AGE',
    'GENDER',
    'HEIGHT',
    'ADRESS',
    'STREET',
    'CITY',
    'ZIP',
    'MARRIED'
    'HOBBIES',
    'BOOKS',
    'TITLE',
    'AUTHOR',
    'GENRES',
    'GAMES',
    'PLATFORM'
)

literals = (
    '{',
    '}'
    ':',
    '[',
    ']',
    ',',
    ':',
    '"'
)

t_NAME = r'\w+\s'
t_AGE = r''
t_GENDER = r'gender'
t_HEIGHT = r'height'
t_ADRESS = r'adress'
t_STREET = r'street'
t_CITY = r'city'
t_ZIP = r'zip'
t_MARRIED = r'married'
t_HOBBIES = r'hobbies'
t_BOOKS = r'books'
t_TITLE = r'title'
t_AUTHOR = r'author'
t_GENRES = r'genres'
t_GAMES = r'games'
t_PLATFORM = r'platform'

t_ignore = r' \n\t'

def t_error(t):
    print(f"Caracter Ilegal {t.value[0]}")
    t.lex.skip(1)

lexer = lex.lex()
lex.input(input.json)
while tok := lexer.token():
    print(tok)

