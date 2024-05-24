import json
from datetime import datetime
import ply.lex as lex

tokens = (
        "LISTAR",
        "MOEDA", 
        "SELECIONAR", 
        "EURO", 
        "CENT", 
        "COMA", 
        "SAIR")


def loadAprodutos():
    with open('stock_produtos.json') as file:
        return {product['cod']: product for product in json.load(file)}
    


def converter_dinheiro(value):
    euros = int(value)
    cents = int(round((value - euros) * 100))
    return f"{euros}e{cents:02}c" if cents else f"{euros}e"

def listar(t):
    r'LISTAR'
    print(f"{'cod':<10}{'nome':<20}{'quant':<15}{'preço':<10}")
    print("-" * 55)
    for product in products.values():
        print(f"{product['cod']:<10}{product['nome']:<20}{product['quant']:<15}{converter_dinheiro(product['preco']):<10}")
    print("-" * 55)
    return t

def addSaldo(t):
    r'MOEDA\s+(?:(\d+e)|(\d+c))(?:,\s*(?:(\d+e)|(\d+c)))*'
    values = t.value[6:].replace(" ", "").split(',')
    for value in values:
        if value.endswith('e'):
            t.lexer.saldo += int(value[:-1])
        elif value.endswith('c'):
            t.lexer.saldo += int(value[:-1]) / 100
    print(f"Saldo = {converter_dinheiro(t.lexer.saldo)}")
    return t

def selecionarProduto(t):
    r'SELECIONAR\s+[A-Z]\d{2}'
    code = t.value.split()[1]
    if code in products:
        product = products[code]
        if product['quant'] > 0 and t.lexer.saldo >= product['preco']:
            t.lexer.saldo -= product['preco']
            product['quant'] -= 1
            print(f"Pode retirar o produto dispensado \"{product['nome']}\"")
            print(f"Saldo = {converter_dinheiro(t.lexer.saldo)}")
        else:
            print("Saldo insufuciente para satisfazer o seu pedido")
            print(f"Saldo = {converter_dinheiro(t.lexer.saldo)}, Price = {converter_dinheiro(product['preco'])}")
    else:
        print("cod de produto inválido")
    return t

def sairMaq(t):
    r'SAIR'
    if t.lexer.saldo > 0:
        change = t.lexer.saldo
        print(f" Pode retirar o troco: {converter_dinheiro(change)}")
    print("Até à próxima")
    t.lexer.should_stop = True
    return t

def char_inv(t):
    print(f"Character não válido: {t.value[0]}")
    t.lexer.skip(1)

products = loadAprodutos()
t_LISTAR = listar
t_MOEDA = addSaldo
t_SELECIONAR = selecionarProduto
t_SAIR = sairMaq
t_ignore = " \t"
t_error = char_inv


lexer = lex.lex()
lexer.saldo = 0
lexer.should_stop = False

current_date = datetime.now().strftime("%Y-%m-%d")
print(f"{current_date},  Stock carregado, Estado atualizado.")
print("Bom dia. Estou disponível para atender o seu pedido.")

while not lexer.should_stop:
    user_input = input(">")
    lexer.input(user_input)
    for token in lexer:
        pass