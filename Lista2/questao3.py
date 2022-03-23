import random
terra1 = random.randint(1,29)
terra2 = random.randint(1,29)
terra3 = random.randint(1,29)
while terra1 == terra2 or terra1 == terra3 or terra2 == terra3:
    terra1 = random.randint(1,29)
    terra2 = random.randint(1,29)
    terra3 = random.randint(1,29)

print("Vibração da Terra 1: ", terra1)
print("Vibração da Terra 2: ", terra2)
print("Vibração da Terra 3: ", terra3)