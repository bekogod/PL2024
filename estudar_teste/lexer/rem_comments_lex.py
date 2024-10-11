import ply.lex as lex
import re

tokens = (
    'CONTEUDO',
    'INLINECOMMENT',
    'COMMENT'
)

states = (
    ('multiline', 'exclusive'),
)

def t_INLINECOMMENT(t):
    r"\/\/[^\n]+"
    pass

def t_ANY_entermultiline(t):
    r"\/\*"
    t.lexer.comment_level += 1
    t.lexer.begin('multiline')
    pass

def t_multiline_exit(t):
    r"\*\/"
    t.lexer.comment_level -= 1
    if t.lexer.comment_level == 0:
        t.lexer.begin('INITIAL')
    pass

def t_multiline_content(t):
    r".+?(?=\/\*|\*\/)"
    pass

def t_CONTEUDO(t):
    r".+?(?=\/\/|\/\*)|.+"
    return t

lexer = lex.lex(reflags=re.DOTALL)
lexer.comment_level = 0

lexer.input("""
texto exemplo com // comentario inline
aqui já não tem comentário
/* comentario 
com
varias /* comentario aninhado */
linhas */ aqui já acabou o multiline
""")

content = ""

while tok := lexer.token():
    content += tok.value

print(content)