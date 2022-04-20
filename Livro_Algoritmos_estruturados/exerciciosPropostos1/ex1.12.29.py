total = 0
cima = 480
for i in range(1,31):
    if i==1:
        total += cima/(i+9)
        print(" %d/%d " % (cima,i+9), end="")
    elif i%2==0:
        total -= cima/(i+9)
        print(" - %d/%d " % (cima,(i+9)), end="")
    else:
        total += cima/(i+9)
        print(" + %d/%d " % (cima,(i+9)), end="")
    cima-=5
print("\nO valor total de S é: %.4f" % total)