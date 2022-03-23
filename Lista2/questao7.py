media = []
for i in range(0, 20):
    media.append(int(input("Digite a media do aluno: ")))
    while(media[i] < 0 or media[i] > 10):
        media[i] = int(input("Digite a media do aluno pois a digitada esta incorreta: "))
    if media[i] < 7:
        print("Reprovado")
    else:
        print("Aprovado")