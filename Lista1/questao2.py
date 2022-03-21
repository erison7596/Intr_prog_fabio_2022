sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
while(sexo != 1 and sexo != 2):
    sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
altura = float(input("Digite sua altura: "))
while(altura < 0):
    altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
while(peso < 0):
    peso = float(input("Digite seu peso: "))
if(sexo == 1):
    pesoIdeal = (72.7*altura)-58
    print("Seu peso ideal é: ", pesoIdeal)
else:
    pesoIdeal = (62.1*altura)-44.7
    print("Seu peso ideal é: ", pesoIdeal)