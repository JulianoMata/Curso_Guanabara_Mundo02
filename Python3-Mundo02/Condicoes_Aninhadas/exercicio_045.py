""" CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR OKENPÔ COM VOCÊ. 'PEDRA/PAPEL/TESOURA'"""

from random import randint
from time import sleep
itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
#
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual sua jogada? "))
print("JO")
sleep(1)
print("KEN...")
sleep(1)
print("POOO...")
sleep(1)
print("-=" * 20)
print(f"O computador escolheu {itens[computador]}")
print(f"Jogador escolheu {itens[jogador]}")
print("-=" * 20)

if computador == 0:   # jogou pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada inválida")


elif computador == 1:  # jogou papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada inválida")

elif computador == 2:  # jogou tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida")

