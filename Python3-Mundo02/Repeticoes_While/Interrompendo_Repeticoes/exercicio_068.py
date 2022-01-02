""" Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando jogador PERDER, mostrando o total de vitória consecutivas que
ele conquistou no final do jogo.
"""
from random import randint

print(("\033[32m=-=\033[m" * 15).center(50))
print("\033[34mJOGO PAR OU ÍMPAR\033[m".center(50))
print(("\033[32m=-=\033[m" * 15).center(50))
vitoria = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "   # inicializa vazio o tipo string P ou I
    while tipo not in "PI":
        tipo = str(input("Digite Par ou Ímpar [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} ", end="")
    print(" DEU PAR " if total % 2 == 0 else " DEU ÍMPAR ")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!!")
            vitoria += 1
        else:
            print("Você PERDEU!!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!!")
            vitoria += 1
        else:
            print("Você PERDEU!!")
            break
    print("\033[34mVamos jogar novamente?\033[m")
print(f"\033[31mGAME OVER!!!\033[m Você venceu {vitoria} vezes.")
