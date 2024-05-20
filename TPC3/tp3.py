import re

def on_off(file_path):
    with open(file_path, 'r') as file:
        exemplo = file.read()

    is_active = True  
    total = 0  


    pattern = re.compile(r'(?:On|Off|(\+|-)?\d+|=)', re.IGNORECASE)

    for match in pattern.finditer(exemplo):
        token = match.group()
        if token.lower() == 'on':
            is_active = True
        elif token.lower() == 'off':
            is_active = False
        elif token.isdigit() and is_active:
            total += int(token)
        elif token == '=':
            print("res:", total)
            total = 0  


on_off("test.txt")