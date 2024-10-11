import ply.lex as lex

tokens = (
    "PALAVRA",
    "VIRGULA",
    "PONTOEXCL",
    "PONTOINTR",
    "PONTOFINAL",
    "RETICENCIAS"
)

t_PALAVRA = r"\w+"
t_VIRGULA = r","
t_PONTOEXCL = r"!+"
t_PONTOINTR = r"\?+"
t_PONTOFINAL = r"\."
t_RETICENCIAS = r"\.\.\."

t_ignore = " \n\t"

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input("Olá mundo, hoje estou feliz!!!")

while tok := lexer.token():
    print(tok)