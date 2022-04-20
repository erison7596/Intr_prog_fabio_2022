cima = 37
baixo = 1
total = 0
while baixo <= 37:
    if total ==0:
        total +=(cima*(cima+1))/baixo
        print(" %dx%d/%d " % (cima,cima+1, baixo), end="")
        cima-=1
        baixo+=1
    else:
        total +=(cima*(cima+1))/baixo
        print("+ %dx%d/%d " % (cima,cima+1, baixo), end="")
        cima-=1
        baixo+=1
print("\nO valor total de S é: %.4f" % total)