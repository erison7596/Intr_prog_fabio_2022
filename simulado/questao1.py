#dois maiores numeros entre 50 gerados
import random
gerado = 0
maior1 = 0  
maior2 = 0
for i in range(1, 11):
    gerado = random.randint(0, 100)
    if(gerado > maior1):
        maior2 = maior1
        maior1 = gerado
    elif(gerado > maior2 and gerado < maior1):
        maior2 = gerado
   # print(gerado) para testar se estava funcionando corretamente
print('O maior numero gerado foi %d' % maior1)
print('O segundo maior numero gerado foi %d' % maior2)