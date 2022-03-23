import random

tipoVeiculo = ["Carro", "Moto", "Onibus"]
lucro = 0
for i in range(1, 401):
    tipo = random.choice(tipoVeiculo)
    
    print("Veiculo ", i, ": ", tipo)
    if tipo == "Carro":
        lucro +=8
    elif tipo == "Moto":
        lucro +=4
    else:
        lucro +=20
print("Lucro total foi de: R$", lucro,",00")