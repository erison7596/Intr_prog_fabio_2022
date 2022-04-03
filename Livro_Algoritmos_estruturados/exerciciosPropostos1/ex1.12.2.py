#para testar eu vou pedir todos os dados ao usuario, para ficar tudo certo

altura = []
sexo = []
numeroH = 0
mediaAlturaM = 0
maiorAltura = 0
menorAltura = 0
cont = 0
for i in range(0,50):
    altura.append(float(input("Digite a altura: ")))
    sexo.append(int(input("Digite o sexo, 1 para homem, 2 para mulher: ")))
    if(i==0):
        menorAltura = altura[i]
    if altura[i] > maiorAltura:
       maiorAltura = altura[i]
    if altura[i] < menorAltura:
        menorAltura = altura[i]
    if sexo[i] == 2:
        mediaAlturaM += altura[i]
        cont+=1
    else:
        numeroH += 1

print('A maior altura é : ', maiorAltura)
print('A menor altura é : ', menorAltura)
print('A média das alturas das mulheres é : ', mediaAlturaM/cont)
if numeroH>1 or numeroH==0:
    print('Tem ', numeroH, ' homens')
else:
    print('Tem ', numeroH, ' homem')