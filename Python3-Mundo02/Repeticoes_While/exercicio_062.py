""" Melhore o exercício_061, perguntando para o usuáriose ele quer mostrar mais alguns termo.
O programa encerra quando ele disser que quer mostrar '0' termos.
"""
print("\033[34mGerador de PA\033[m")
print("\033[31m=-=\033[m" * 12)
primeiroTermo = int(input("Primeiro: "))
razao = int(input("razao: "))
termo = primeiroTermo
cont = 1
total = 0
continua = 10  # no início do programa são 10 termos
while continua != 0:  # enquanto não sai do programa
    total += continua
    while cont <= total:
        print(f"{termo} → ", end="")
        termo += razao
        cont += 1
    print("\033[33mPAUSA\033[m")
    continua = int(input("Quantos termos quer mostrar a mais? "))

print(f"\033[31mFIM \033[mcom \033[31m{total}\033[m termos mostrados ")




