x = int(input("Digite o valor de x: "))
total = 0
elevado = 2
baixo = 3
fat = 1
for i in range(1,21):
    fat=1
    for j in range(elevado+1,1,-1):
        fat*=j
    if i==1:
        print("S = %d" % x, end="")
        total += x
    elif(i%2==0):
        print(" - %d^%d/%d!" % (x,elevado,baixo), end="")
        total -= (x**elevado)/fat
        elevado+=2
        baixo+=2
    else:
        print(" + %d^%d/%d!" % (x,elevado,baixo), end="")
        total += (x**elevado)/fat
        elevado+=2
        baixo+=2
print("\nO valor total de S = %.4f" % total)