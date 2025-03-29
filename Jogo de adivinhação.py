# Importamos aos random (aleatorios)
import random

#O random.randint faz números aleatorios interios entre 1 e 10
num = random.randint(1,10)
palpite = 0

#Desde que o número for difente do palpite o while continuara rodando e pedindo o palpite ate acertar o número
while num != palpite:
    palpite = int(input("Digite seu palpite:"))
    if num > palpite:
        print("Palpite esta muito baixo")
    elif num < palpite:
        print("Palpite esta muito alto")
    else:
        print("Você acertou o número")