paiA = 90000000
paisB = 200000000
cont = 0
while(paiA <= paisB):
    paiA += paiA*0.03
    paisB += paisB*0.015
    cont += 1
print('O tempo de crescimento do pais A para igualar ou ultrapassar o pais B é de %d anos' % cont)