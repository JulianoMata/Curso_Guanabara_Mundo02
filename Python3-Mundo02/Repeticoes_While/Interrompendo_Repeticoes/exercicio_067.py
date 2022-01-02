""" Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for
negativo."""
from time import sleep
print(("\033[34m=+=\033[m" * 15).center(50))  # Apenas enfeitando com cores e centralizado
print("\033[34mTABUADA\033[m".center(50))
print(("\033[34m=+=\033[m" * 15).center(50))
cont = 1
while True:
    numero = int(input("Digite um número: "))
    print(("\033[34m=+=\033[m" * 15).center(50))
    if numero < 0:
        break
    for cont in range(1, 11):
        print(f"\033[33m{numero}\033[m x {cont:2} = \033[31m{numero * cont}\033[m")
        sleep(0.5)
    print(("\033[34m=+=\033[m" * 15).center(50))
print("Fim")
