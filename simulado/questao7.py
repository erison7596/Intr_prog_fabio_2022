import random

palpite = []

cont = 0
sorteado = 0
n = int(input("Digite o numero de jogos: "))
for i in range(0, n):
    while cont!=6:
        sorteado = random.randint(1,60)
        if sorteado not in palpite:
            palpite.append(sorteado)
            cont += 1
        else:
            continue
    palpite.sort()
    print("Palpite %d: " % (i+1), palpite)
    palpite.clear()
    cont = 0