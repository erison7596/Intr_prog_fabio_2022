from operator import truediv


baixo = 3
pi = 4
fim = 0
cont = 0
while True:
    if cont == 0 or cont%2==0:
        pi -= (4/baixo)
        fim = 4/baixo
        baixo += 2
        
    else:
        pi += (4/baixo)
        fim = 4/baixo
        baixo += 2
    cont += 1
    if fim <= 0.0001:
        break
    #print(pi)

print("O valor de pi é: %.4f" % pi)