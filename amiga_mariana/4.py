n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
if n1 > n2 and n1 > n3:
    print("O maior numero é",n1)
elif n2 > n1 and n2 > n3:
    print("O maior numero é",n2)
elif n3 > n1 and n3 > n2:
    print("O maior numero é",n3)
elif n1 == n2 and n1 > n3:
    print("Os numero %d é o maior" %n2)
elif n1 == n3 and n1 > n2:
    print("Os numero %d é o maior" %n1)
elif n2 == n3 and n2 > n1:
    print("Os numero %d é o maior" %n2)
else: 
    print("Todos os números são iguais")