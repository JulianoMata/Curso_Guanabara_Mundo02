""" Desenvolva um programa que leia o primeiro termo e a razão de uma 'PA'. No final,
mostre os 10 primeiros termos dessa progressão. ***obs: PA é progressão aritmetica"""


primeiroTermo = int(input("Digite um número: "))  # numero do usuário
razao = int(input("Digite a razão: "))
decimoTermo = primeiroTermo + 10 * razao
for cont in range(primeiroTermo, decimoTermo, razao):
    print(cont, end=" → ")
print("Acabou.")
