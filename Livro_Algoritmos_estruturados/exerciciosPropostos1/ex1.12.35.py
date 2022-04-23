total = 0
cima = 100
baixo = 0
fat = 1
for i in range(1,21):
    if baixo > 0:
        fat *= baixo
    if i == 1:
        print("S = %d/%d!" % (cima,baixo), end="")
        total += cima/1
        cima-=1
        baixo+=1
    elif i%2==0:
        print(" + %d/%d!" % (cima,baixo), end="")
        total += cima/fat
        cima-=1
        baixo+=1
    else:
        print(" - %d/%d!" % (cima,baixo), end="")
        total -= cima/fat
        cima-=1
        baixo+=1
print("\nO valor total de S = %.4f" % total)