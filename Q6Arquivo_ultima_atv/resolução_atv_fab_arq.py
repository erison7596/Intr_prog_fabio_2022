arquivo=open("Q7_dados.txt","r")     #abre arquivo
nomes = []                        #cria lista
for linha in arquivo.readlines():  #aqui passo toda a linha do arquivo para a lista
    nomes.append(linha)
arquivo.close()                   #fecha arquivo

#ordenando o arquivo
nomes.sort()
# for i in range(len(nomes)):
    # print(i, nomes[i])

#separando so o nome por linha
name= []
for i in range(len(nomes)):
    name.append(nomes[i].split("|"))

##aqui pego as notas e as coloco em uma lista
notas = []
for i in range (len(nomes)):
    for j in range(len(nomes[i])):    
        if nomes[i][j] == '|':   #i é linha e j é coluna
            notas.append(nomes[i][j+2]+str(nomes[i][j+3])+ str(nomes[i][j+4])+str(nomes[i][j+5]))
        if nomes[i][j] == '-' and nomes[i][j+1] == ' ':
            if nomes[i][j+2] == '1' and nomes[i][j+3] == '0':
                notas.append(nomes[i][j+2]+str(nomes[i][j+3])+ str(nomes[i][j+4])+str(nomes[i][j+5]))
                break
            else:
                notas.append(nomes[i][j+2]+str(nomes[i][j+3])+ str(nomes[i][j+4]))
            break
# print(aprovados)
mediadecada = []
# print("\n")
# print("\n")
i=0
#aqui pego as notas pego a media das duas de cada pessoa e as coloco em uma lista
while i <(len(notas)):
    num1 = float(notas[i])
    num2 = float(notas[i+1])
    resulta = round(((num1+num2)/2),2)
    mediadecada.append(resulta)
    i+=2
# print(mediadecada)
#pegando  nome e nota na lista name
fim = []
for i in range(len(mediadecada)):
    if mediadecada[i] >= 7:
        fim.append(name[i][0] + str("- ") + str(mediadecada[i]) )

# print("\n")
# print(name[2][0])
# print("\n")
# print(fim)

arquivo=open("aprovados.txt","w")
for i in range(len(fim)):
    arquivo.write("%s\n" % fim[i])
arquivo.close()