""" A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM
ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
- ATÉ 9 ANOS: MIRIM
- ATÉ 14 ANOS: INFANTIL
- ATÉ 19 ANOS: JUNIOR
- ATÉ 25 ANOS: SÊNIOR
- ACIMA: MASTER"""
from datetime import date

anoAtual = date.today().year
anoNasc = int(input("Digite seu ano de nascimento: "))
idade = anoAtual - anoNasc
print(f"O atleta tem {idade}")
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("Sênior")
else:
    print("Master")

