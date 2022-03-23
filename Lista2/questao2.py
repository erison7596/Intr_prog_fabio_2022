base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = base
for i in range(1, expoente):
    base *= base
print("O resultado é: ", resultado)