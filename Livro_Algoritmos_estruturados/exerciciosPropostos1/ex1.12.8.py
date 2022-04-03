sexo = []
resposta = []
sim = 0
nao = 0
porcentSim = 0
porcentNao = 0
homem = 0
mulher = 0
for i in range(1, 2001):
    sexo.append(int(input("Sexo da %dº pessoa 1 para homem ou 2 para Mulher: " % i)))
    resposta.append(int(input("Resposta da %dº pessoa, 1 para Sim ou 2 para Não: " % i)))
    if(sexo[i-1] == 1):
        homem += 1
        if(resposta[i-1] == 2):
            porcentNao += 1
    else:
        mulher += 1
        if(resposta[i-1] == 1):
            porcentSim += 1
    if(resposta[i-1] == 1):
        sim += 1
    else:
        nao += 1
totalPorcentH = 0
if(homem > 0):
    totalPorcentH = (porcentNao/homem)*100
totalPorcentM = 0
if(mulher > 0):
    totalPorcentM = (porcentSim/mulher)*100
print('Numero de pessoas que responderam Sim: %d' % sim)
print('Numero de pessoas que responderam Não: %d' % nao)
print('A porcentagem de homens que responderam Não é de %.2f%%' % totalPorcentH)
print('A porcentagem de mulheres que responderam Sim é de %.2f%%' % totalPorcentM)