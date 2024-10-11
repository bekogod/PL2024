import ply.lex as lex

import sys

tokens = (
    'LPAREN',
    'RPAREN',
    'VIRG',
    'ID',
    'NUM',
    'BOOL'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VIRG   = r','
t_ID     = r'\w+'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOL(t):
    r'(?i)true|false'
    t.value = t.value.upper()
    return t
    


t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    return

lexer = lex.lex() # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'

# Reading input
#for linha in sys.stdin:
#    lexer.input(linha) 
#    tok = lexer.token()
#    while tok:
#        print(tok)
#        tok = lexer.token()


###ANALISADOR SINTATICO

#
# (1)
# (aahah)
# (True,false)
# (1,aa, 2, bbb, TRUE, 3,False)
#

import sys
import ply.yacc as yacc
from aula11_mistas_lex import tokens

def p_list(p):
    "LIST : LPAREN ELS RPAREN"
    p[0] = p[2]
    if (parser.cntN != parser.cntP):
        print("Erro Semantico: O número de PALAVRAS e INTEIROS é Diferente!")

def p_els_varios(p):
    "ELS : ELS VIRG EL"
    parser.conta += 1
    p[0] = p[1]
    if (p[3] != []):
       p[0].append(p[3])

def p_els_um(p):
    "ELS : EL"
    parser.conta = 1
    if (p[1]):
        p[0] = [p[1]]
    else:
        p[0] = []

def p_el_num(p):
    "EL : NUM"
    parser.soma += p[1]
    parser.cntN += 1
    p[0] = []

def p_el_bool(p):
    "EL : BOOL"
    p[0] = p[1]

def p_el_id(p):
    "EL : ID"
    parser.pals.append(p[1])
    parser.cntP += 1
    p[0] = []

def p_error(p):
    print("Syntax error!")
    parser.exito = False

parser = yacc.yacc()

for linha in sys.stdin:
    parser.exito = True
    parser.conta = 0
    parser.cntP = 0
    parser.cntN = 0
    parser.soma = 0
    parser.pals = []
    out = parser.parse(linha)
    if parser.exito:
       print("Lista sintetizada de Booleanos: ",out)
       print ("Informação final relativa ao processamento da frase analisada:")
       print("O total de elementos é : ", parser.conta)
       print("A soma é : ", parser.soma)
       print("As palavras são : ", parser.pals)


#parser.conta = 0
#parser.cntP = 0
#parser.cntN = 0
#parser.soma = 0
#parser.pals = []
#arser.exito = True
#fonte = ""
#for linha in sys.stdin:
    #fonte += linha
#parser.parse(fonte)
#if parser.exito:
#    print ("Parsing teminou com sucesso!")
#    print ("Informação final relativa ao processamento da frase analisada:")
#    print("O total de elementos é : ", parser.conta)
#    print("A soma é : ", parser.soma)
#    print("As palavras são : ", parser.pals)
