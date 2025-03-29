import random

chance = 3
num = random.randint(1,10)
palpite = 0

while chance != 0 and palpite != num:
    print('Números de chances:', chance)
    palpite = int(input("Digite seu palpite:"))
    print("---------------------------------------------")
    chance = chance - 1
    if palpite > num:
        print("Palpite muito grande")
        print("-----------------------------------")
    elif palpite < num:
        print("Palpite muito pequeno")
        print("-----------------------------------")
    elif palpite == num:
        print("você acertou o número!!!!!")
    elif chance == 0:
        print("Mais sorte da proxima vez")

