x = int(input("Digite o valor de x: "))
total = 0
elevado = 25
for i in range(1,26):
    if i==1:
        print("S = %d^%d/%d" % (x,elevado,i), end="")
        total += (x**elevado)/i
        elevado-=1
    elif(i%2==0):
        print(" - %d^%d/%d" % (x,elevado,i), end="")
        total -= (x**elevado)/i
        elevado-=1
    else:
        print(" + %d^%d/%d" % (x,elevado,i), end="")
        total += (x**elevado)/i
        elevado-=1
print("\nO valor total de S = %.4f" % total)