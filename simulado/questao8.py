um = int(input('Digite um numero: '))
dois = int(input('Digite um numero: '))
tres = int(input('Digite um numero: '))
i=2
mmc = 1

while(um>1 or dois > 1 or tres >1):
    n1 = um % i
    n2 = dois % i
    n3 = tres % i
    if(n1 == 0):
        um = um / i
    if(n2 == 0):
        dois = dois / i
    if(n3 == 0):
        tres = tres / i
    if(n1!=0 and n2!=0 and n3!=0):
        i +=1
    else:
        mmc*=i

print(mmc)