""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a se sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.

obs.: considere que o caixa possui cédulas de 50, 20, 10 e 1

"""
print("\033[33m$  $  $\033[m".center(38))
print("\033[36mBANCO GUANABARA\033[m".center(38))
print("\033[33m $  $ \033[m" * 5)

valor = int(input("Qual valor deseja sacar? R$ "))
print("\033[36m=-=\033[m" * 10)
total = valor
cedula = 50
totalCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f"total de \033[34m{totalCedulas}\033[m cédulas de \033[34mR${cedula},00\033[m")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            print("\033[36m=-=\033[m" * 10)
            break

print("\033[33m $  $ \033[m" * 5)
print("\033[35mVolte sempre\033[m!!!")





# banco BMG
# que valor você quer sacar?
# total de {} cedulas d R$50,00
# total de {} cedulas d R$20,00
# total de {} cedulas d R$10,00
# total de {} cedulas d R$1,00
#
# volte sempre ao banco bmg! tenha um bom dia!!