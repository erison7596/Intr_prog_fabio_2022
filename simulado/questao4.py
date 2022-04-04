from pickle import TRUE
import random
white = 0
blue = 0
contBranco = 0
contAzul = 0
percorridoBranco = 0
percorridoAzul = 0
for i in range (0, 5):
    gerado = random.randint(60, 1000)#defini esse valor para poder ambos abastecerem no minimo
    branco = 200/3.6
    azul = 240/3.6
    geradoMs = gerado/3.6
    cont = 0
    percorridoAzul = 0
    percorridoBranco = 0
    while (TRUE):
        #cada cont é um km
        cont += 1
        if(contBranco < 10):
            contBranco += 1
            percorridoBranco += branco/10
        else:
            percorridoBranco += branco
        if(contAzul < 6):
            contAzul += 1
            percorridoAzul += azul/6
        else:
            percorridoAzul += azul
        if(cont == 50):
            contBranco = 0
        if(cont == 30):
             contAzul = 0
        if(percorridoBranco >= geradoMs):
            white += 1
            break
        if(percorridoAzul >= geradoMs):
            blue += 1
            break
    print('%d pessoas foram brancas' % white)
    print('%d pessoas foram azuis' % blue)

if(white > blue):
    print('O branco ganhou mais vezes')
else:
    print('O azul ganhou mais vezes')