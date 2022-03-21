lado_a = int(input("Digite o primeiro lado do triângulo: "))
lado_b = int(input("Digite o segundo lado do triângulo: "))
lado_c = int(input("Digite o terceiro lado do triângulo: "))
if((lado_a>(lado_b+lado_c)) or (lado_b>(lado_a+lado_c)) or (lado_c>(lado_a+lado_b))):
    print("Não é um triângulo!")
else:
    if((lado_c*lado_c) ==((lado_a*lado_a)+(lado_b*lado_b))):
        print("É um triângulo retângulo!")
    elif((lado_c*lado_c) >((lado_a*lado_a)+(lado_b*lado_b))):
        print("É um triângulo obtusângulo!")
    elif((lado_c*lado_c) <((lado_a*lado_a)+(lado_b*lado_b))):
        print("É um triângulo acutângulo!")
    elif((lado_c*lado_c) ==((lado_a*lado_a)+(lado_b*lado_b))):
        print("É um triângulo equilátero!")
    elif((lado_c*lado_c) ==((lado_a*lado_a)+(lado_b*lado_b))):
        print("É um triângulo isósceles!")
    elif((lado_c*lado_c) ==((lado_a*lado_a)+(lado_b*lado_b))):
        print("É um triângulo escaleno!")