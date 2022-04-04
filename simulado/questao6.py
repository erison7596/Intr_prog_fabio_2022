pessoa = []
idade = []
pessoa1 = 0
pessoa2 = 0
pessoa3 = 0
continuar = 0
menor1=0
menor2=0
menor3=0
cont = 0
muda= 0;
while(True):
    pessoa.append(input("Digite o nome da pessoa: "))
    idade.append(int(input("Digite a idade da pessoa: ")))
    if(cont == 0):
        pessoa1 = idade[cont]
        menor1 = cont
    if(cont == 1):
        pessoa2 = idade[cont]
        menor2 = cont
    if(cont == 2):
        pessoa3 = idade[cont]
        menor3 = cont
    
    
    if(cont>=2):
        continuar = int(input("Deseja continuar? 1 para sim e 0 para não: "))
        if(pessoa1<pessoa2 and pessoa1>pessoa3):
            muda = pessoa1
            pessoa1 = pessoa3
            pessoa3 = muda
            muda = menor1
            menor1 = menor3
            menor3 = muda
        elif(pessoa2<pessoa1 and pessoa2>pessoa3):
            muda = pessoa2
            pessoa2 = pessoa3
            pessoa3 = muda
            muda = menor2
            menor2 = menor3
            menor3 = muda
        elif(pessoa3<pessoa1 and pessoa3>pessoa2):
            muda = pessoa3
            pessoa3 = pessoa2
            pessoa2 = muda
            muda = menor3
            menor3 = menor2
            menor2 = muda

        if(idade[cont]<pessoa1):
            menor3 = menor2
            menor2 = menor1
            menor1 = cont
            pessoa3 = pessoa2
            pessoa2 = pessoa1
            pessoa1 = idade[cont]

        elif(idade[cont]<pessoa2 and idade[cont]>pessoa1):
            menor3 = menor2
            menor2 = cont
            pessoa3 = pessoa2
            pessoa2 = idade[cont]
        elif(idade[cont]<pessoa3):
            menor3 = cont
            pessoa3 = idade[cont]
        
        if(continuar == 0):
            break
    cont += 1
print("Pessoa 1: " , pessoa[menor1])
print("Pessoa 2: ", pessoa[menor2])
print("Pessoa 3: ", pessoa[menor3])
print("Idade 1: %d" % idade[menor1])
print("Idade 2: %d" % idade[menor2])
print("Idade 3: %d" % idade[menor3])