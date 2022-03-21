import random
tipo = int(input("Digite 1 para votos automáticos e 2 para manual: "))
while(tipo != 1 and tipo != 2):
    tipo = int(input("Digite 1 para votos automáticos e 2 para manual: "))
if(tipo == 1):
    print("Votos automáticos")
    naruto = random.randint(1, 10000)
    sakura = random.randint(1, 10000)
    shin = random.randint(1, 10000)
    nulos = random.randint(1, 10000)
    brancos = random.randint(1, 10000)
    print("Votos para o candidato Naruto: ", naruto )
    print("Votos para o candidato Sakura: ", sakura)
    print("Votos para o candidato Shin: ", shin)
    print("Votos nulos: ", nulos)
    print("Votos brancos: ", brancos)
    invalida = nulos + brancos
    geral = naruto + sakura + shin
    if(geral>invalida):
        if(naruto > sakura and naruto > shin):
            print("O candidato Naruto foi eleito!")
        elif(sakura > naruto and sakura > shin):
            print("O candidato Sakura foi eleito!")
        elif(shin > naruto and shin > sakura):
            print("O candidato Shin foi eleito!")
        elif(shin==naruto and shin==sakura and naruto==sakura):
            print("Houve um empate geral!")
        elif(naruto==sakura and naruto>shin):
            print("Houve um empate entre naruto e sakura!")
        elif(naruto==shin and naruto>sakura):
            print("Houve um empate entre naruto e shin!")
        elif(sakura==shin and sakura>naruto):
            print("Houve um empate entre sakura e shin!")
    else:
        print("A soma dos votos nulos e brancos são maiores que a soma de todos os cadidatos, logo, a votação foi invalidada!")
else:
    print("Votos manual")
    naruto = int(input("Digite o número de votos para o candidato Naruto: "))
    sakura = int(input("Digite o número de votos para o candidato Sakura: "))
    shin = int(input("Digite o número de votos para o candidato Shin: "))
    nulos = int(input("Digite o número de votos nulos: "))
    brancos = int(input("Digite o número de votos brancos: "))
    invalida = nulos + brancos
    geral = naruto + sakura + shin
    if(geral>invalida):
        if(naruto > sakura and naruto > shin):
            print("O candidato Naruto foi eleito!")
        elif(sakura > naruto and sakura > shin):
            print("O candidato Sakura foi eleito!")
        elif(shin > naruto and shin > sakura):
            print("O candidato Shin foi eleito!")
        elif(shin==naruto and shin==sakura and naruto==sakura):
            print("Houve um empate geral!")
        elif(naruto==sakura and naruto>shin):
            print("Houve um empate entre naruto e sakura!")
        elif(naruto==shin and naruto>sakura):
            print("Houve um empate entre naruto e shin!")
        elif(sakura==shin and sakura>naruto):
            print("Houve um empate entre sakura e shin!")
    else:
        print("A soma dos votos nulos e brancos são maiores que a soma de todos os cadidatos, logo, a votação foi invalidada!")