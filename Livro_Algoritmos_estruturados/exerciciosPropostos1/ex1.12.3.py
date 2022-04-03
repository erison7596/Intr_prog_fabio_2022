print('Centígrados em Fahrenheit:')
for i in range(50,151):
    print(i, '°C = %.2f'% ((i*1.8)+32), '°F |')
    print('__________________')
print('Fahrenheit em Centígrados:')
for i in range(50,151):
    print(i, '°F = %.2f' %((i-32)/1.8), '°C |')
    print('__________________')