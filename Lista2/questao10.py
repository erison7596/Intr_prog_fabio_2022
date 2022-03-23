muda = 0
total = 0
for i in range(1, 51):
    if muda == 0 or muda ==1:
        print(" -",i, end="")
        total -= i
    else:
        print(" +",i, end="")
        total += i
    muda +=1
    if muda == 4:
        muda = 0
print("\nTotal: ", total)