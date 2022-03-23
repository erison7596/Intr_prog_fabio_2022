nome = []
sexo = []
idade = []
parar = False
velha = 0
nome_velho = ''
nome_velha = ''
novo = 500
while parar!=True:
    nome.append(input("Digite o nome: "))
    sexo.append(int(input("Digite 1 para mulher e 2 para homem: ")))
    idade.append(int(input("Digite a idade: ")))
    parar = input("Deseja parar? (S/N) ")
    if parar=='S' or parar=='s':
        parar = True
    else:
        parar = False
for i in range(len(sexo)):
    if sexo[i]==1:
        if idade[i]>velha:
            velha = idade[i]
            nome_velha = nome[i]
    else:
        if idade[i]<novo:
            novo = idade[i]
            nome_velho = nome[i]
if velha==0:
    print("Não há mulheres cadastradas")
else:
    print("A Mulher mais velha é: ", nome_velha, " com ", velha, " anos")
if novo==500:
    print("Não há homens cadastrados")
else:
    print("O Homem mais novo é: ", nome_velho, " com ", novo, " anos")