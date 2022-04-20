cima = 1
total = 0
while cima<=10:
    if cima ==1 or cima%2==0:
        if cima ==1:
            total += cima/cima**2
            print(" %d/%d " % (cima,cima**2), end="")
            cima+=1
        else:
            total -= cima/cima**2
            print("- %d/%d " % (cima,cima**2), end="")
            cima+=1
    else:
        total += cima/cima**2
        print("+ %d/%d " % (cima,cima**2), end="")
        cima+=1
print("\nO valor total de S é: %.4f" % total)
        