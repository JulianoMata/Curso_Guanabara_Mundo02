""" Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de 'Três' e que se encontram no intervalo de 1 até 500 """

soma = 0
cont = 0
for num in range(1, 501, 2): # números ímpares
    if num % 3 == 0:
        # print(num, end=" ")
        soma += num   # acumulador soma valor
        cont += 1  # contador soma +1
print(f" A soma de {cont} múltiplos ímpares de '3' é {soma}")
