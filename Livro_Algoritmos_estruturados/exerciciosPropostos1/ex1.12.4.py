from pickle import TRUE


nome = []
precoCompra = []
precoVenda = []
cont = 0
prodMenorQue10 = 0
prodDe10a20 = 0
prodMaiorQue20 = 0
valorTotalCompras = 0
valorTotalVendas = 0
valorLucro = 0
while(TRUE):
    nome.append(input("Nome do produto: "))
    precoCompra.append(float(input("Preço de compra: ")))
    precoVenda.append(float(input("Preço de venda: ")))
    valorLucro += (precoVenda[cont] - precoCompra[cont])
    valorTotalCompras += precoCompra[cont]
    valorTotalVendas += precoVenda[cont]

    if((precoCompra[cont]+(precoCompra[cont]*0.1)) > precoVenda[cont]):
        prodMenorQue10 += 1
    elif((precoCompra[cont]+(precoCompra[cont]*0.2)) >= precoVenda[cont] or (precoCompra[cont]+(precoCompra[cont]*0.1)) >= precoVenda[cont]):
        prodDe10a20 += 1
    else:
        prodMaiorQue20 += 1

    if(input("Deseja continuar? (S/N) ") == "N"):
        break
    
    cont += 1

print('Tem %d produtos com preço de compra menor que 10%% do preço de venda' % prodMenorQue10)
print('Tem %d produtos com preço de compra entre 10%% e 20%% do preço de venda' % prodDe10a20)
print('Tem %d produtos com preço de compra maior que 20%% do preço de venda' % prodMaiorQue20)
print('O valor total de compras foi de R$ %.2f' % valorTotalCompras)
print('O valor total de vendas foi de R$ %.2f' % valorTotalVendas)
print('O lucro total foi de R$ %.2f' % valorLucro)