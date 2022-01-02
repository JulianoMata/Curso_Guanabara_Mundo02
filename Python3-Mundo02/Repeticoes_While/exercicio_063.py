"""Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos
de uma Sequência de Fibonacci.

Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print("\033[36mFREQUÊNCIA DE FIBONACCI\033[m")
num = int(input("\033[33mQtos termos você deseja mostrar? \033[m"))
termo01 = 0
termo02 = 1
print(f"{termo01} → {termo02}", end="")
cont = 3
while cont <= num:
    termo03 = termo01 + termo02
    print(f" → {termo03}", end="")
    termo01 = termo02
    termo02 = termo03
    cont += 1
print("\033[31m → FIM\033[m")
