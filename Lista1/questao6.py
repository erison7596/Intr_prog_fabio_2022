import random
tipo = int(input("Digite 1 para forma automáticos e 2 para manual: "))
while(tipo != 1 and tipo != 2):
    tipo = int(input("Digite 1 para forma automáticos e 2 para manual: "))
if(tipo == 1):
    c =  random.randint(1, 10000)
    b =  random.randint(1, 10000)
    a =  random.randint(1, 10000)
    if((c*c) ==((a*a)+(b*b))):
        print("É um triângulo retângulo!")
    elif((c*c) >((a*a)+(b*b))):
        print("É um triângulo obtusângulo!")
    elif((c*c) <((a*a)+(b*b))):
        print("É um triângulo acutângulo!")
    else:
        print("Não é um triângulo!")
else:
    a = int(input("Digite o primeiro lado do triângulo: "))
    b = int(input("Digite o segundo lado do triângulo: "))
    c = int(input("Digite o terceiro lado do triângulo: "))
    if((c*c) ==((a*a)+(b*b))):
        print("É um triângulo retângulo!")
    elif((c*c) >((a*a)+(b*b))):
        print("É um triângulo obtusângulo!")
    elif((c*c) <((a*a)+(b*b))):
        print("É um triângulo acutângulo!")
    else:
        print("Não é um triângulo!")