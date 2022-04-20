total = 0
baixo = 1
for i in range(1,51):
    if i==1:
        total += 1/(baixo**3)
        print(" %d/%d " % (1,(baixo**3)), end="")
    elif i%2==0:
        total -= 1/(baixo**3)
        print(" - %d/%d " % (1,(baixo**3)), end="")
    else:
        total += 1/(baixo**3)
        print(" + %d/%d " % (1,(baixo**3)), end="")
    baixo+=2
print("\nO valor total de pi é: %.4f" % total)