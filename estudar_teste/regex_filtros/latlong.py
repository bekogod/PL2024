import re
f = open("latlong.txt","r")
fv = open("latlong_validos.txt","w")
pattern = r"^\([+-]?([0-9]|[1-8][0-9]|90)(\.\d+)?, [+-]?(180(\.0+)?|([0-9]|[0-9][0-9]|1[0-7][0-9])(\.\d+)?)\)$"
for line in f:
    if re.match(pattern,line):
        fv.write("Válido\n")
    else:
        fv.write("Inválido\n")
