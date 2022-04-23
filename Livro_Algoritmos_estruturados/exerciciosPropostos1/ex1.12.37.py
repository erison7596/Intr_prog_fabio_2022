baixo = 1
fat = 1
total = 0
cont = 2
for i in range(1,51):
    fat*=i
    if i == 1:
        print("S = %d!/%d" % (i,baixo), end="")
        total += fat/baixo
        baixo+=cont
    elif i%2==0:
        print(" - %d!/%d" % (i,baixo), end="")
        total -= fat/baixo
        baixo+=cont

    else:
        print(" + %d!/%d" % (i,baixo), end="")
        total += fat/baixo
        baixo+=cont
    cont*=2
print("\nO valor total de S = %.4f" % total)