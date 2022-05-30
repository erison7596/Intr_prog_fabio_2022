gasto = float(input("Digite o valor total gasto: "))
imposto = 0
if gasto <= 500:
    print("O valor do imposto será de R$", imposto)
else:
    imposto = (gasto - 500) * 0.5
    print("O valor do imposto será de R$", imposto)