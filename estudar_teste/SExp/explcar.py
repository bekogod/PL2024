import math
import readline

from ply import lex as lex
from ply.yacc import yacc

# -----------------
# Analisador Lexico
# -----------------

tokens = ('NBR', 'ID', 'FUN1')
t_ignore = ' \t\r\n'

literals = '+-*/()%^='

def t_NBR(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+'

    funcs = {
        'cos': math.cos,
        'sin': math.sin,
        'tan': math.tan,
        'inc': lambda x: x + 1,
    }

    if t.value in funcs:
        t.type = 'FUN1'
        t.value = funcs[t.value]

    return t

def t_error(t):
    print(f'Illegal character: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

def debug_lexer(exemplo):
    lexer.input(exemplo)

    while tok := lexer.token():
        print(tok)

#debug_lexer(exemplo)

# --------------------
# Analisador Sintatico
# --------------------

"""
Stmt -> ID '=' Stmt
Stmt -> Exp

Exp -> Parcela
Exp -> Exp '+' Parcela
Exp -> Exp '-' Parcela

Parcela -> Fator
Parcela -> Parcela '*' Fator
Parcela -> Parcela '/' Fator
Parcela -> Parcela '%' Fator

Fator -> Termo
Fator -> Termo '^' Fator

Termo -> NBR
Termo -> ID
Termo -> FUN1 '(' Exp ')'
Termo -> '+' Termo
Termo -> '-' Termo
Termo -> '(' Exp ')'
"""

vars = {}


def p_Stmt1(t):    "Stmt : ID '=' Stmt";          t[0] = vars[t[1]] = t[3]
def p_Stmt2(t):    "Stmt : Exp";                  t[0] = t[1]

def p_Exp1(t):     "Exp : Parcela";               t[0] = t[1]
def p_Exp2(t):     "Exp : Exp '+' Parcela";       t[0] = t[1] + t[3]
def p_Exp3(t):     "Exp : Exp '-' Parcela";       t[0] = t[1] - t[3]

def p_Parcela1(t): "Parcela : Fator";             t[0] = t[1]
def p_Parcela2(t): "Parcela : Parcela '*' Fator"; t[0] = t[1] * t[3]
def p_Parcela3(t): "Parcela : Parcela '/' Fator"; t[0] = t[1] / t[3]
def p_Parcela4(t): "Parcela : Parcela '%' Fator"; t[0] = math.fmod(t[1], t[3])

def p_Fator1(t):   "Fator : Termo";               t[0] = t[1]
def p_Fator2(t):   "Fator : Termo '^' Fator";     t[0] = t[1] ** t[3]

def p_Termo1(t):   "Termo : NBR";                 t[0] = t[1]
def p_Termo2(t):   "Termo : ID";                  t[0] = vars.get(t[1], 0.)
def p_Termo3(t):   "Termo : FUN1 '(' Exp ')'";    t[0] = t[1](t[3])
def p_Termo4(t):   "Termo : '+' Termo";           t[0] = +t[2]
def p_Termo5(t):   "Termo : '-' Termo";           t[0] = -t[2]
def p_Termo6(t):   "Termo : '(' Exp ')'";         t[0] = t[2]

def p_error(t):
    print(f"Syntax error: {t.value}")

parser = yacc()

readline.parse_and_bind("tab: complete")
while line := input("> "):
    exp = parser.parse(line)

    print(exp)