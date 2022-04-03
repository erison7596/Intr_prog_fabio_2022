cont = 0
idade = []
total = 0
while True:
    idade.append(int(input("Digite a idade: ")))
    total += idade[cont]
    if idade[cont]==0:
        break
    cont += 1
media = total/cont
print("A média das idades é: ", media)