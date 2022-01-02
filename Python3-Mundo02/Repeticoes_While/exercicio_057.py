"""  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]  # fatiamento, pega primeira letra
while sexo not in "MF":
    sexo = str(input("Inválido!!! Digite 'M' ou  'F' por favor!!! ")).strip().upper()[0]
print(f"Sexo registrado: {sexo}")


# if sexo not in "MmFf":
#     print("Opção INVÁLIDA")








#####################################################################################################

# QUANDO SE SABE O LIMITE PODE USAR O FOR OU WHILE
# QUANDO NÃO SABE O LIMITE USE WHILE

# for cont in range(1, 10):
#     print(cont, end=" ")
# print("FIM!!!")
#
# cont = 1
# while cont < 10:
#     print(cont, end=" ")
#     cont += 1
# print("FIM!")

######################################################################################################




