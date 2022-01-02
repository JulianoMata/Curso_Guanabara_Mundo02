""" Crie um programa que leia o ano de nascimento de 'sete' pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores."""

# considere 21 (anos) maioridade
from datetime import date
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 8):
    anoNasc = int(input(f"Digite o ano de nascimento: {pessoa}ª pessoa "))
    idade = anoAtual - anoNasc
    if idade >= 21:
        totalMaior += 1

    else:
        totalMenor += 1

print(f"{totalMaior} pessoa(s) é ou são maior(es).")
print(f"{totalMenor} pessoa(s) é ou são menor(es).")
