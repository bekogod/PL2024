# -- Problema: Alien username
import re 

f = open("usernames.txt", "r")
fv = open("usernames_válidos.txt", "w")

print("««« Searching Valid Alien Usernames »»»")

for linha in f:
  if re.search(r'^[_\.]\d+[A-Za-z]{3,}_?$', linha):
    fv.write("Válido: " + linha)
  else:
    fv.write("Inválido: " + linha)
    
print("««« Validados »»»")
print("««« Search »»»")