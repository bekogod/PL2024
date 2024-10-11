import re
f = open("ipv46.txt","r")
fv = open("ipv46_validos.txt","w")

for line in f:
    if re.match(r"^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$", line):
        fv.write("IPv4\n")
    elif re.match(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-f]{1,4}$",line):
        fv.write("IPv6\n")
    else:
        fv.write("Erro\n")
print("Validated")



