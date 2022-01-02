"""  Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep
n1 = int(input("\033[33mDigite primeiro número: \033[m"))
n2 = int(input("\033[33mDigite segundo número: \033[m"))
opcoes = 0
while opcoes != 5:
    print("\033[34m\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n{ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA\n\033[m")
    opcoes = int(input("\033[36m>>>>>>>>>> Escolha uma opção: \033[m"))

    if opcoes == 1:
        soma = n1 + n2
        print(f"A soma é {soma}")
    elif opcoes == 2:
        produto = n1 * n2
        print(f"O produto é {produto}")
    elif opcoes == 3:
        if n1 == n2:
            print("Números iguais!!! Nem maior e nem menor!!!")
        elif n1 > n2:
            maior = n1
            print(f"Entre {n1} e {n2} o maior é {maior}")
        else:
            maior = n2
            print(f"Entre {n1} e {n2} o maior é {maior}")

    elif opcoes == 4:
        print("Informe novamente os números: ")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif opcoes == 5:
        print("Saindo...")
    else:
        print("Inválido")
    print("\033[31m=-=\033[m" * 10)
    sleep(2)
print("Fim do programa!!!")
