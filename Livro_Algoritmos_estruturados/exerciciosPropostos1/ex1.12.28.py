cima = 1000
total = 0
for i in range(1,51):
    if i==1:
        total += cima/i
        print(" %d/%d " % (cima,i), end="")
    elif i%2==0:
        total -= cima/i
        print(" - %d/%d " % (cima,i), end="")
    else:
        total += cima/i
        print(" + %d/%d " % (cima,i), end="")
    cima-=3
print("\nO valor total de S é: %.4f" % total)