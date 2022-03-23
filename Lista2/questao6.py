import random

palpite1 = []
palpite2 = []
palpite3 = []
palpite4 = []
palpite5 = []

cont = 0
sorteado = 0
while cont!=6:
    sorteado = random.randint(1,60)
    if sorteado not in palpite1:
        palpite1.append(sorteado)
        cont += 1
    else:
        continue
while cont!=11:
    sorteado = random.randint(1,60)
    if sorteado not in palpite2:
        palpite2.append(sorteado)
        cont += 1
    else:
        continue
while cont!=16:
    sorteado = random.randint(1,60)
    if sorteado not in palpite3:
        palpite3.append(sorteado)
        cont += 1
    else:
        continue
while cont!=21:
    sorteado = random.randint(1,60)
    if sorteado not in palpite4:
        palpite4.append(sorteado)
        cont += 1
    else:
        continue
while cont!=26:
    sorteado = random.randint(1,60)
    if sorteado not in palpite5:
        palpite5.append(sorteado)
        cont += 1
    else:
        continue
palpite1.sort()
palpite2.sort()
palpite3.sort()
palpite4.sort()
palpite5.sort()
print("Palpite 1: ", palpite1)
print("Palpite 2: ", palpite2)
print("Palpite 3: ", palpite3)
print("Palpite 4: ", palpite4)
print("Palpite 5: ", palpite5)
