cima = 1
baixo = 1
total = 0
while cima <=99:
    total += cima/baixo
    print(" %d/%d " % (cima, baixo), end="")
    cima+=2
    baixo+=1
print("\nO valor total de S é: %.4f" % total)