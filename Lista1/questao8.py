tipo = int(input("Digite\n- 1 para retângulo\n- 2 para triângulo\n- 3 para circulo\n"))
while(tipo != 1 and tipo != 2 and tipo != 3):
    tipo = int(input("Digite\n- 1 para retângulo\n- 2 para triângulo\n- 3 para circulo\n"))
if(tipo == 1):
    base = int(input("Digite a base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    print("A área do retângulo é: ", base*altura)
elif(tipo == 2):
    base = int(input("Digite a base do triângulo: "))
    altura = int(input("Digite a altura do triângulo: "))
    print("A área do triângulo é: ", (base*altura)/2)
else:
    raio = int(input("Digite o raio do circulo: "))
    print("A área do circulo é: ", 3.14*(raio*raio))