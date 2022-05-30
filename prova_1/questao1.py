#2/3 + 4/5 + 6/7 - 8/9 - 10/11 - 12/13 - 14/15 + 16/17...

quant = int(input("Digite a quantidade de termos: "))
cima = 2
baixo = 3
cont = 0
for i in range(quant):
    if i == 0:
        print(cima,end="")
        print("/",end="")
        print(baixo,end="")
        cont+=1
        
    else:
        if cont <= 2:
            print(" + ",end="")
            print(cima,end="")
            print("/",end="")
            print(baixo,end="")
            cont += 1
        else:
            print(" - ",end="")
            print(cima,end="")
            print("/",end="")
            print(baixo,end="")
            cont+=1
        if cont == 7:
            cont = 0
    cima += 2
    baixo += 2