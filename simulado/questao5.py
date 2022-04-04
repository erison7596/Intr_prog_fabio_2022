import random
from tkinter import TRUE
cont = 0
while (TRUE):
    um = random.randint(0, 200)
    dois = random.randint(0, 200)
    tres = random.randint(0, 200)
    cont+=1
    if(um == dois and um == tres):
        break
print('Foram necessarios %d tentativas para sair um trio igual de' % cont ,um)