baixo = 15
cima = 1
total = 0
for i in range(1,15):
    if i == 1:
        print("S = %d/%d" % (cima,(baixo*baixo)), end="")
        total += cima/(baixo*baixo)
        cima*=2
        baixo-=1
    if i%2==0:
        print(" + %d/%d" % (cima,(baixo*baixo)), end="")
        total += cima/(baixo*baixo)
        cima*=2
        baixo-=1
    else:
        print(" - %d/%d" % (cima,(baixo*baixo)), end="")
        total -= cima/(baixo*baixo)
        cima*=2
        baixo-=1
print("\nO valor total de S = %.4f" % total)