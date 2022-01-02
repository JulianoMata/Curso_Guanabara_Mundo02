""" Melhore o jogo exercício_028 onde o computador vai 'pensar' em um número entre 0 e 10.
Contudo, agora o jogador vai tentar até acertar, mostrando no final quantos palpites
foram necessários para vencer.

                                                EXERCÍCIO_28

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu. """

from random import randint  # importa o metodo randint da biblioteca random para escolha aleatoria do numero
from time import sleep  # importa o metodo sleep da biblioteca time para determinar tempo de espera


computador = randint(0, 10)  # faz o computador "pensar"

print("\033[33m-=-\033[m" * 20)  # aplicando enfeite com cor
print("Vou pensar em um numero entre 0 e 10. Tente adivinhar...")
print("\033[33m-=-\033[m" * 20)  # aplicando enfeite com cor

acertou = False
cont = 0  # tentativas do jogador
while not acertou:
    # Jogador tenta adivinhar
    jogador = int(input("Pensei em qual numero? "))
    cont += 1
    # aplicando enfeite com cor
    print("\033[31mPROCESSANDO...\033[m")
    sleep(3)  # intervalo de 3segundos

    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Menos... De novo...")
        else:
            print("Mais... De novo...")

print(f"Acertou com {cont} tentativas!!!")





