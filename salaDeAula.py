frase = input("Digite uma frase: ")
tamanho = len(frase)
espaco = 0
quant_palav = 1
tipo = input("a) A frase lida na vertical\nb) A frase lida na diagonal\nc) A frase lida na ordem inversa\nd) A frase lida na diagonal invertida\ne) A frase lida de sem vogais\nf) A frase lida com as vogais em maiusculo\ng) A quantidade de palavras presente na frase\nh) Se existir a primeira palavra na frase substituir pela segunda\ni) Quantas vezes a letra i aparece na frase\nj) Quantas consoantes estão na frase\nescolha a opção desejada")
if tipo == "a" or tipo =="A":
    #vertical
    print("Frase Vertical:")
    for i in range(tamanho):
        print(frase[i])
elif tipo == "b" or tipo =="B":
    #diagonal
    print("Frase diagonal:")
    for i in range(tamanho):
        print(frase[i])
        for j in range(espaco):
            print(" ", end="")
        espaco += 1
elif tipo == "c" or tipo =="C":
    #inversa
    print("")
    print("Frase invertida: ")
    for i in range(tamanho-1, -1, -1):
        print(frase[i], end="")
elif tipo == "d" or tipo =="D":
    #diagonal invertida
    espaco = 0
    print("Frase diagonal invertida:")
    for i in range(tamanho-1, -1, -1):
        print(frase[i])
        for j in range(espaco):
            print(" ", end="")
        espaco += 1
elif tipo == "e" or tipo =="E":
    #sem vogal
    print("")
    print("Frase sem vogais: ")
    for i in range(tamanho):
        if frase[i] not in "aeiou":
            print(frase[i], end="")
elif tipo == "f" or tipo =="F":
    #vogais em Maiusculo
    print("")
    print("Frase com vogais em maiusculo: ")
    for i in range(tamanho):
        if frase[i] == 'a': 
            print("A", end="")
        elif frase[i] == 'e':
            print("E", end="")
        elif frase[i] == 'i':
            print("I", end="")
        elif frase[i] == 'o':
            print("O", end="")
        elif frase[i] == 'u':
            print("U", end="")
        else:
            print(frase[i], end="")
    print("")
elif tipo == "g" or tipo =="G":
    #quantidade de palavras
    for i in range(tamanho):
        if frase[i] == " ":
            quant_palav += 1
    print("Quantidade de palavras: ", quant_palav)
    print("")
elif tipo == "h" or tipo =="H":
    frase2 = frase
    #substituir a primeira pela segunda 
    local= 0 
    cont = 0
    j=0
    verificar = input("Digite uma palavra: ")
    tamanho_verificar = len(verificar)
    if verificar in frase:
        segunda = input("Digite a segunda palavra: ")
        tam_seg = len(segunda)
        print("antes de mudar : ", frase)
        for i in range(tamanho):
            if verificar[j] == frase[i]:
                print("Palavra encontrada")
                cont += 1
                j+=1
            else:
                cont = 0
                local = 0
            if cont == tamanho_verificar:
                local = i - tamanho_verificar+1
                break
        print(local)
        tamanho2 = tamanho - tamanho_verificar
        if local == 0:
            print(segunda, end="")
            for i in range(tamanho_verificar, tamanho):
                #print(i)
                print(frase[i], end="")
        else:
            for i in range(tamanho_verificar+2):
                print(frase2[i], end="")
            print(segunda, end="")
            
            for m in range(tamanho_verificar+local+1, tamanho2):
                print(frase2[m], end="")
    else:
        print("Palavra não encontrada")
elif tipo == "i" or tipo =="I":
    #quantas vezes o i aparece na frase
    print("\n\n")
    cont=0
    for i in range(tamanho):
        if frase[i] == "i" or frase[i] == "I":
            cont += 1
    print("Quantidade de vezes que aparece o i: ", cont)
elif tipo == "j" or tipo =="J":
    #quantas consoantes estão na frase 
    print("")
    cont=0
    for i in range(tamanho):
        if frase[i] not in "aeiou" and frase[i] != " ":
            cont += 1
    print("Quantidade de consoantes: ", cont)