#ler um numero e informar se é multiplo de 2 e 3 ao mesmo tempo
numero = int(input('Digite um numero: '))
if(numero % 2 == 0 and numero % 3 == 0):
    print('O numero %d é multiplo de 2 e 3' % numero)   
else:
    print('O numero %d não é multiplo de 2 e 3' % numero)