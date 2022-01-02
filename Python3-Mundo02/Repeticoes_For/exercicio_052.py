""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input("Digite um número: "))
numeroDivisivel = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print("\033[33m", end="")
        numeroDivisivel += 1
    else:
        print("\033[31m", end="")
    print(f"{cont}", end=" ")
print(f"\n\033[mO numero {num} foi divisível {numeroDivisivel} vezes")
if numeroDivisivel == 2:
    print("Por isso ele é \033[33mPRIMO\033[m")
else:
    print("Por isso \033[31mNÃO É PRIMO\033[m")
