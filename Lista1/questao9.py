temp_agua = float(input("Digite a temperatura em ºC: "))
if(temp_agua < 0):
    print("A água está solida")
elif(temp_agua >= 0 and temp_agua < 100):
    print("A água está líquida")
else:
    print("A água está gasosa")