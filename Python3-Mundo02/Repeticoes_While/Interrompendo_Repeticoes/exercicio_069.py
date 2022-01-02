""" Crie um programa que leia a idade e o sexo d várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20anos.
"""
print("\033[36mCADASTRO DE PESSOAS\033[m")
total18 = totalMulher20 = totalHomem = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    # condições necessárias para responder o enunciado
    if idade >= 18:
        total18 += 1
    if sexo == "M":
        totalHomem += 1
    if sexo == "F" and idade <= 20:
        totalMulher20 += 1

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {total18}")
print(f"Total de homens cadastrados: {totalHomem}")
print(f"Total de mulheres com menos de 20 anos: {totalMulher20}")
print("FIM!!!")
