import re
f = open("matriculas.txt","r")
fv = open("matriculas_validas.txt","w")
pattern = r"(\d\d)(\.\.\.|-|:)\1\2\1\2\1"
for line in f:
    if re.match(pattern,line):
        fv.write(line.strip("\n")+"Válido\n")
    else:
        fv.write(line.strip("\n")+"Inválido\n")

