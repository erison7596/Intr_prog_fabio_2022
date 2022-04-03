cont = 0
massaInicial = float(input("Massa inicial (g): "))
massaFinal = massaInicial
while(massaFinal >= 0.5):
    massaFinal = massaFinal / 2
    cont += 1

print('O valor da massa Inicial é de %.2f g' % massaInicial)
print('O valor da massa Final é de %.2f g' % massaFinal)
tempo = cont*50
segundo = tempo%60
minuto = (tempo//60)%60
hora = (tempo//3600)%24
print('O tempo de vida do indivíduo é de %d horas, %d minutos e %d segundos' % (hora, minuto, segundo))