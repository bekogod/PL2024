
total = 0
aptos = 0
inaptos = 0
escaloes = [0] * 4
modalidades = []


with open('emd.csv', 'r') as dataset:
    next(dataset)  

    for line in dataset:
        total += 1
        valores = line.strip().split(',')
        if valores[12] == "true":
            aptos += 1
        else:
            inaptos += 1

        if valores[8] not in modalidades:
            modalidades.append(valores[8])

        age = int(valores[5])
        if 20 <= age <= 24:
            escaloes[0] += 1
        elif 25 <= age <= 29:
            escaloes[1] += 1
        elif 30 <= age <= 34:
            escaloes[2] += 1
        else:
            escaloes[3] += 1

        


percentagem_aptos = aptos / total * 100
percentagem_inaptos = inaptos / total * 100

modalidades.sort()



with open('result.txt', 'w') as result:
    
    result.write('Modalidades: ')
    for modalidade in modalidades:
        result.write(modalidade + ', ')
    result.write('\n')

    
    result.write('Percentagem de aptos: ' + str(percentagem_aptos) + '%\n')
    result.write('Percentagem de inaptos: ' + str(percentagem_inaptos) + '%\n')

    
    result.write('Numero de pessoas por escalao:\n')
    result.write('20-24: ' + str(escaloes[0]) + '\n')
    result.write('25-29: ' + str(escaloes[1]) + '\n')
    result.write('30-34: ' + str(escaloes[2]) + '\n')
    result.write('35-39: ' + str(escaloes[3]) + '\n')
