#26 anos de idade

cont = 0
media = 0

for i in range(0,30):
    idade = int(input("digite sua idade : "))
    altura = float(input("digite sua altura: "))
    if(idade>26):
        media += altura
        cont += 1
media = media/cont
print("A media das alturas do pessoal com mais de 26 anos: ", media)