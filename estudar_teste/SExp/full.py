import ply.lex as lex
import ply.yacc as yacc
import sys
from sexp_lex import tokens


 ##ANALISADOR LEXICO
tokens = (
    'NUM',
    'PAL',
    'LPAREN',
    'RPAREN'
)

def t_NUM(t):
    r'\d+(\.\d+)?'
    #t.value = float(t.value)
    return t

t_PAL = r'[a-zA-Z]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \n\t'

def t_error(t):
    print('Illegal character: %s', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#ANALISADOR SINTATICO
## incio da GIC

def p_lisp_grammar(p):
    """
       lisp : sexp
       sexp : PAL
       sexp : NUM
       sexp : LPAREN sexplist RPAREN
       sexplist : sexp sexplist
       sexplist :  
    """

def p_error(p):
    parser.success = False
    print('Syntax error!')

###inicio do parsing
parser = yacc.yacc()

for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
       print('Parsing successful!')


import ply.yacc as yacc
import sys

from sexp_lex import tokens

## incio da GIC

def p_lisp(p): "lisp : sexp"; p[0] = p[1]

def p_sexp_pal(p): "sexp : PAL"; p[0] = p[1]

def p_sexp_num(p): "sexp : NUM"; p[0] = p[1]

def p_sexp_sexplist(p): "sexp : LPAREN sexplist RPAREN"; p[0] = p[2]

def p_sexplist_sexp(p): "sexplist : sexp sexplist"; p[0] = p[1] + " , " + p[2]

def p_sexplist_empty(p): "sexplist : "; p[0] = "$"


def p_error(p):
    parser.success = False
    print('Syntax error!')
    exit()

###inicio do parsing
parser = yacc.yacc()
parser.success = True

for linha in sys.stdin:
    parser.parse(linha)

   

