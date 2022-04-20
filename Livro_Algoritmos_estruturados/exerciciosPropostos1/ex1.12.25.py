baixo = 50
elevado = 1
total = 0
while elevado <= 50:
    if total == 0:
        total += (2**elevado)/baixo
        print(" %d/%d " % (2**elevado, baixo), end="")
        elevado += 1
        baixo -= 1
    else:
        total += (2**elevado)/baixo
        print("+ %d/%d " % (2**elevado, baixo), end="")
        elevado += 1
        baixo -= 1
    
print ("\nO valor total de S é: %.4f" % total)