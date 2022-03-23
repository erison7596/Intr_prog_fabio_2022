import random

comidaVolstagg = random.randint(1,100)
comidaLoki = random.randint(1,100)
print("Comida entre Volstagg e Loki ")

if comidaVolstagg > comidaLoki:
    print("Volstagg ganhou")
elif comidaVolstagg < comidaLoki:
    print("Loki ganhou")
else:
    print("Empate entre Volstagg e Loki")

frandalFlecha = []
lokiFlecha = []
print("\n")
print("Flecha entre Frandal e Loki")

for i in range(0,10):
    frandalFlecha.append(random.randint(0,60))
    lokiFlecha.append(random.randint(0,60))
for i in range(0,10):
    if frandalFlecha[i] > 50 and lokiFlecha[i] > 50:
        print("ninguem ganhou a flecha", i)
    elif frandalFlecha[i] > 50 and lokiFlecha[i] < 50:
        print("loki ganhou a flecha", i)
    elif frandalFlecha[i] < 50 and lokiFlecha[i] > 50:
        print("Frandal ganhou a flecha", i)
    elif frandalFlecha[i] < lokiFlecha[i]:
        print("Frandal ganhou a flecha", i)
    elif frandalFlecha[i] > lokiFlecha[i]:
        print("Loki ganhou a flecha", i)
    else:
        print("Empate entre Frandal e Loki na flecha", i)

print("\n")
print("Loki vs Hogun")
prenderLoki = random.randint(0,1)
prenderHogun = random.randint(0,1)
if prenderLoki == 0 and prenderHogun == 1:
    print("Hogun ganhou")
elif prenderLoki == 1 and prenderHogun == 0:
    print("Loki ganhou")
else:
    print("Empate")

print("\n")
print("Valquiria vs Loki")
fim=0
i=0
while fim==0:
    valquiria1 = random.randint(0,60)
    valquiria2 = random.randint(0,60)
    loki1 = random.randint(0,60)
    loki2 = random.randint(0,60)
    if valquiria1 == valquiria2:
        print("Valquiria ganhou")
        fim=1
    elif loki1 == loki2:
        print("Loki ganhou")
        fim=1
    else:
        continue
    i+=1
print("\n")
print("Lady sif vs Loki")

ataqueloki = []
defesaloki = []
ataqueladysif = []
defesaladysif = []
lokiganha = 0
ladysifganha = 0
for i in range(0,5):
    ataqueloki.append(random.randint(1,2))
    defesaloki.append(random.randint(1,2))
    ataqueladysif.append(random.randint(1,2))
    defesaladysif.append(random.randint(1,2))
    #fiz de 1 a 2 pq não importa o tamanho do numero ele so quer saber se é impar ou par
    if ataqueloki[i] == 1 and defesaladysif[i] == 2 or ataqueloki[i] == 2 and defesaladysif[i] == 1:
        lokiganha+=1
    elif ataqueladysif[i] == 2 and defesaloki[i] == 1 or ataqueladysif[i] == 1 and defesaloki[i] == 2:
        ladysifganha+=1
    else:
        continue
if lokiganha > ladysifganha:
    print("Loki ganhou")
else:
    print("Lady Sif ganhou")