""" Faça um programa que leia um número qualquer e mostre o seu fatorial.

ex:
5!= 5x4x3x2x1 = 120
"""
from math import factorial
num = int(input("Digite um número para calcular seu fatorial:\n"))
fatorial = factorial(num)
print(f"O fatorial de {num} é {fatorial}")

##############################################################################################

num = int(input("Digite um número para calcular seu fatorial: "))
cont = num
fatorial = 1
print(f"Calculando {num}! : ", end="")
while cont > 0:
    print(f"{cont} ", end='')
    print("x " if cont > 1 else "=", end="")
    fatorial *= cont
    cont -= 1
print(f" {fatorial}")

#################################################################################################
num = int(input("Digite numero para calcular seu fatorial: "))
for cont in range(num, 1, -1):
    fatorial *= 1
print(fatorial)






