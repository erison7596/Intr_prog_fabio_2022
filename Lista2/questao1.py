import random
import array
# forma menos eficiente de se programar, obs.: não terminei tudo assim
jesseQuick = random.randint(1, 100)
barryAllen = random.randint(1, 100)
wallyWest = random.randint(1, 100)
drWells = random.randint(1, 100)
jayGarrick = random.randint(1, 100)
maxMercury = random.randint(1, 100)

if jesseQuick > barryAllen and jesseQuick > wallyWest and jesseQuick > drWells and jesseQuick > jayGarrick and jesseQuick > maxMercury:
    print("O Jesse Quick é o melhor jogador e sua velocidade foi : ", jesseQuick*300000, "km/s")
elif barryAllen > jesseQuick and barryAllen > wallyWest and barryAllen > drWells and barryAllen > jayGarrick and barryAllen > maxMercury:
    print("O Barry Allen é o melhor jogador e sua velocidade foi : ", barryAllen*300000, "km/s")
elif wallyWest > jesseQuick and wallyWest > barryAllen and wallyWest > drWells and wallyWest > jayGarrick and wallyWest > maxMercury:
    print("O Wally West é o melhor jogador e sua velocidade foi : ", wallyWest*300000, "km/s")
elif drWells > jesseQuick and drWells > barryAllen and drWells > wallyWest and drWells > jayGarrick and drWells > maxMercury:
    print("O Dr. Wells é o melhor jogador e sua velocidade foi : ", drWells*300000, "km/s")
elif jayGarrick > jesseQuick and jayGarrick > barryAllen and jayGarrick > wallyWest and jayGarrick > drWells and jayGarrick > maxMercury:
    print("O Jay Garrick é o melhor jogador e sua velocidade foi : ", jayGarrick*300000, "km/s")
elif maxMercury > jesseQuick and maxMercury > barryAllen and maxMercury > wallyWest and maxMercury > drWells and maxMercury > jayGarrick:
    print("O Max Mercury é o melhor jogador e sua velocidade foi : ", maxMercury*300000, "km/s")
elif jesseQuick == barryAllen and jesseQuick > wallyWest and jesseQuick > drWells and jesseQuick > jayGarrick and jesseQuick > maxMercury:
    print("Jesse Quick está empate com Barry Allen e sua velocidade foi : ", jesseQuick*300000, "km/s")
elif jesseQuick == wallyWest and jesseQuick > barryAllen and jesseQuick > drWells and jesseQuick > jayGarrick and jesseQuick > maxMercury:
    print("Jesse Quick está empate com Wally West e sua velocidade foi : ", jesseQuick*300000, "km/s")
elif jesseQuick == drWells and jesseQuick > barryAllen and jesseQuick > wallyWest and jesseQuick > jayGarrick and jesseQuick > maxMercury:
    print("Jesse Quick está empate com Dr. Wells e sua velocidade foi : ", jesseQuick*300000, "km/s")
elif jesseQuick == jayGarrick and jesseQuick > barryAllen and jesseQuick > wallyWest and jesseQuick > drWells and jesseQuick > maxMercury:
    print("Jesse Quick está empate com Jay Garrick e sua velocidade foi : ", jesseQuick*300000, "km/s")
elif jesseQuick == maxMercury and jesseQuick > barryAllen and jesseQuick > wallyWest and jesseQuick > drWells and jesseQuick > jayGarrick:
    print("Jesse Quick está empate com Max Mercury e sua velocidade foi : ", jesseQuick*300000, "km/s")
elif barryAllen == wallyWest and barryAllen > jesseQuick and barryAllen > drWells and barryAllen > jayGarrick and barryAllen > maxMercury:
    print("Barry Allen está empate com Wally West e sua velocidade foi : ", barryAllen*300000, "km/s")
elif barryAllen == drWells and barryAllen > jesseQuick and barryAllen > wallyWest and barryAllen > jayGarrick and barryAllen > maxMercury:
    print("Barry Allen está empate com Dr. Wells e sua velocidade foi : ", barryAllen*300000, "km/s")
elif barryAllen == jayGarrick and barryAllen > jesseQuick and barryAllen > wallyWest and barryAllen > drWells and barryAllen > maxMercury:
    print("Barry Allen está empate com Jay Garrick e sua velocidade foi : ", barryAllen*300000, "km/s")
elif barryAllen == maxMercury and barryAllen > jesseQuick and barryAllen > wallyWest and barryAllen > drWells and barryAllen > jayGarrick:
    print("Barry Allen está empate com Max Mercury e sua velocidade foi : ", barryAllen*300000, "km/s")
elif wallyWest == drWells and wallyWest > jesseQuick and wallyWest > barryAllen and wallyWest > jayGarrick and wallyWest > maxMercury:
    print("Wally West está empate com Dr. Wells e sua velocidade foi : ", wallyWest*300000, "km/s")
elif wallyWest == jayGarrick and wallyWest > jesseQuick and wallyWest > barryAllen and wallyWest > drWells and wallyWest > maxMercury:
    print("Wally West está empate com Jay Garrick e sua velocidade foi : ", wallyWest*300000, "km/s")
elif wallyWest == maxMercury and wallyWest > jesseQuick and wallyWest > barryAllen and wallyWest > drWells and wallyWest > jayGarrick:
    print("Wally West está empate com Max Mercury e sua velocidade foi : ", wallyWest*300000, "km/s")
elif drWells == jayGarrick and drWells > jesseQuick and drWells > barryAllen and drWells > wallyWest and drWells > maxMercury:
    print("Dr. Wells está empate com Jay Garrick e sua velocidade foi : ", drWells*300000, "km/s")
elif drWells == maxMercury and drWells > jesseQuick and drWells > barryAllen and drWells > wallyWest and drWells > jayGarrick:
    print("Dr. Wells está empate com Max Mercury e sua velocidade foi : ", drWells*300000, "km/s")
elif jayGarrick == maxMercury and jayGarrick > jesseQuick and jayGarrick > barryAllen and jayGarrick > wallyWest and jayGarrick > drWells:
    print("Jay Garrick está empate com Max Mercury e sua velocidade foi : ", jayGarrick*300000, "km/s")
else:
    print("Os jogadores são iguais e sua velocidade foi : ", jesseQuick*300000, "km/s")
