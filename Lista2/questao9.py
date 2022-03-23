#jogos 
# 1 - Metal Gear Solid
# 2 - Driver
# 3 - Crash Bandicoot
# 4 - Warped
# 5 - Tekken 3
# 6 - Cortex Strikes Back
# 7 - Final Fantasy VIII
# 8 - Gran Turismo 2
# 9 - Final Fantasy VII
# 10 - Gran Turismo
jogo= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
jogosEscolhidos = []

for i in range(0,35):
    print(" 1 - Metal Gear Solid\n2 - Driver\n3 - Crash Bandicoot\n4 - Warped\n5 - Tekken 3\n6 - Cortex Strikes Backz\n7 - Final Fantasy VIII\n8 - Gran Turismo 2\n9 - Final Fantasy VII\n10 - Gran Turismo")
    print("Aluno ", i+1, ":")
    jogosEscolhidos.append(int(input("Digite o numero do jogo que você prefere: ")))
for i in range(0,35):
    if jogosEscolhidos[i] == 1:
        jogo[0] += 1
    elif jogosEscolhidos[i] == 2:
        jogo[1] += 1
    elif jogosEscolhidos[i] == 3:
        jogo[2] += 1
    elif jogosEscolhidos[i] == 4:
        jogo[3] += 1
    elif jogosEscolhidos[i] == 5:
        jogo[4] += 1
    elif jogosEscolhidos[i] == 6:
        jogo[5] += 1
    elif jogosEscolhidos[i] == 7:
        jogo[6] += 1
    elif jogosEscolhidos[i] == 8:
        jogo[7] += 1
    elif jogosEscolhidos[i] == 9:
        jogo[8] += 1
    elif jogosEscolhidos[i] == 10:
        jogo[9] += 1

if jogo[0] > jogo[1] and jogo[0] > jogo[2] and jogo[0] > jogo[3] and jogo[0] > jogo[4] and jogo[0] > jogo[5] and jogo[0] > jogo[6] and jogo[0] > jogo[7] and jogo[0] > jogo[8] and jogo[0] > jogo[9]:
    print("O jogo preferido é Metal Gear Solid")
elif jogo[1] > jogo[0] and jogo[1] > jogo[2] and jogo[1] > jogo[3] and jogo[1] > jogo[4] and jogo[1] > jogo[5] and jogo[1] > jogo[6] and jogo[1] > jogo[7] and jogo[1] > jogo[8] and jogo[1] > jogo[9]:
    print("O jogo preferido é Driver")
elif jogo[2] > jogo[0] and jogo[2] > jogo[1] and jogo[2] > jogo[3] and jogo[2] > jogo[4] and jogo[2] > jogo[5] and jogo[2] > jogo[6] and jogo[2] > jogo[7] and jogo[2] > jogo[8] and jogo[2] > jogo[9]:
    print("O jogo preferido é Crash Bandicoot")
elif jogo[3] > jogo[0] and jogo[3] > jogo[1] and jogo[3] > jogo[2] and jogo[3] > jogo[4] and jogo[3] > jogo[5] and jogo[3] > jogo[6] and jogo[3] > jogo[7] and jogo[3] > jogo[8] and jogo[3] > jogo[9]:
    print("O jogo preferido é Warped")
elif jogo[4] > jogo[0] and jogo[4] > jogo[1] and jogo[4] > jogo[2] and jogo[4] > jogo[3] and jogo[4] > jogo[5] and jogo[4] > jogo[6] and jogo[4] > jogo[7] and jogo[4] > jogo[8] and jogo[4] > jogo[9]:
    print("O jogo preferido é Tekken 3")
elif jogo[5] > jogo[0] and jogo[5] > jogo[1] and jogo[5] > jogo[2] and jogo[5] > jogo[3] and jogo[5] > jogo[4] and jogo[5] > jogo[6] and jogo[5] > jogo[7] and jogo[5] > jogo[8] and jogo[5] > jogo[9]:
    print("O jogo preferido é Cortex Strikes Back")
elif jogo[6] > jogo[0] and jogo[6] > jogo[1] and jogo[6] > jogo[2] and jogo[6] > jogo[3] and jogo[6] > jogo[4] and jogo[6] > jogo[5] and jogo[6] > jogo[7] and jogo[6] > jogo[8] and jogo[6] > jogo[9]:
    print("O jogo preferido é Final Fantasy VIII")
elif jogo[7] > jogo[0] and jogo[7] > jogo[1] and jogo[7] > jogo[2] and jogo[7] > jogo[3] and jogo[7] > jogo[4] and jogo[7] > jogo[5] and jogo[7] > jogo[6] and jogo[7] > jogo[8] and jogo[7] > jogo[9]:
    print("O jogo preferido é Gran Turismo 2")
elif jogo[8] > jogo[0] and jogo[8] > jogo[1] and jogo[8] > jogo[2] and jogo[8] > jogo[3] and jogo[8] > jogo[4] and jogo[8] > jogo[5] and jogo[8] > jogo[6] and jogo[8] > jogo[7] and jogo[8] > jogo[9]:
    print("O jogo preferido é Final Fantasy VII")
elif jogo[9] > jogo[0] and jogo[9] > jogo[1] and jogo[9] > jogo[2] and jogo[9] > jogo[3] and jogo[9] > jogo[4] and jogo[9] > jogo[5] and jogo[9] > jogo[6] and jogo[9] > jogo[7] and jogo[9] > jogo[8]:
    print("O jogo preferido é Final Fantasy X")
else:
    print("Pode ter algum empate")
