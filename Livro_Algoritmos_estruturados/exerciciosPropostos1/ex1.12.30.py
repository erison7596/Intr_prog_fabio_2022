total = 0
cima = 3
baixo = 1
a = 0.0
cont = 0
while a <= 6.3:
    for i in range (cima,1,-1):
        baixo *= i
    if cont==0:
        print("sen A = ",a, end="")
    elif cont%2==0:
        print(" + %.1f^%d/%d" % (a,cima, baixo), end="")
        total += (a**cima)/baixo
        cima+=2
    else:
        print(" - %.1f^%d/%d" % (a,cima, baixo), end="")
        total -= (a**cima)/baixo
        cima+=2
    a+=0.1
    cont+=1
    baixo = 1
print("\nO valor total de sen A é: %.4f" % total)