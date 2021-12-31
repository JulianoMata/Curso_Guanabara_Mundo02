""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- a media de idade do grupo
- qual o nome do homem mais velho
- quantas mulheres têm menos de 20 anos
"""
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ""
totalMulher20 = 0
for pessoa in range(1, 5):
    print(f" ----- {pessoa}ª PESSOA ----- ")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaIdade += idade

    if pessoa == 1 and sexo in 'Mm':  # caso digite M ou m
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in "Mm" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in "Ff" and idade < 20:
        totalMulher20 += 1

    mediaIdade = somaIdade / 4
    print(f"A media de idade do grupo é {mediaIdade:.1f}")
    print(f"O nome do homem mais velho é {nomeMaisVelho} e sua idade é {maiorIdadeHomem}")
    print(f"O número de mulheres com menos de 20 anos é {totalMulher20}")
