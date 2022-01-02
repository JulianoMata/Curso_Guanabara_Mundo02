"""  Refaça o exercício_051, lendo o primeiro termo e a razão de uma PA(Progressão Aritmética),
mostrando os primeiros termos da progressão usando a estrutura while.


                                                EXERCÍCIO_051

Desenvolva um programa que leia o primeiro termo e a razão de uma 'PA'. No final,
mostre os 10 primeiros termos dessa progressão. ***obs: PA é progressão aritmetica
"""

# primeiroTermo = int(input("Digite um número: "))  # numero do usuário
# razao = int(input("Digite a razão: "))
# decimoTermo = primeiroTermo + 10 * razao
# for cont in range(primeiroTermo, decimoTermo, razao):
#     print(cont, end=" → ")
# print("Acabou.")


print("Gerador de PA")
print("=-=" * 12)
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiroTermo
cont = 1
while cont <= 10:
    print(f"{termo} → ", end="")
    termo += razao
    cont += 1
print("\033[31mFIM\033[m")




