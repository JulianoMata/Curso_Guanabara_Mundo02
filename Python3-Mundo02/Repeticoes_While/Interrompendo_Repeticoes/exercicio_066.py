""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag)
"""
cont = soma = 0

while True:

    numero = int(input("Digite um número [999 parar]: "))

    if numero == 999:
        break
    cont += 1
    soma += numero
print(f"Você digitou {cont} números e a soma é {soma}")










# cont = 1
# while cont <= 10:
#     print(cont, " → ", end="")
#     cont += 1
# print("Acabou")
#
# ###########################################################################################
#
# numero = soma = 0
# while True:
#     numero = int(input("Digite um número: "))
#     if numero == 999:
#         break
#     soma += numero
#
# print(f"A soma vale {soma}")
#
# #############################################################################################