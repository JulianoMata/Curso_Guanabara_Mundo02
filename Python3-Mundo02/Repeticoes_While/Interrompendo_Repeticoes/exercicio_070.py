""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:

A) qual é o total gasto na compra
B) quantos produtos custam mais de R$1000,00
C) qual é o nome do produto mais barato

"""
valorTotal = cont1000 = menorPrecoProduto = contProduto = 0
menorNomeProduto = ""

print("\033[36m=-=\033[m"*11)
print("\033[34mLOJA SUPER BARATÃO\033[m".center(40))
print("\033[36m=-=\033[m"*11)

while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o valor do produto: R$"))
    contProduto += 1
    valorTotal += preco
    if preco > 1000:
        cont1000 += 1
    if contProduto == 1 or preco < menorPrecoProduto:
        menorPrecoProduto = preco
        menorNomeProduto = produto

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break
print("\033[31mFIM DO PROGRAMA\033[m".center(40))
print(f"O total gasto foi de \033[34mR${valorTotal:.2f}\033[m")
print(f"{cont1000} produtos custam mais de \033[34mR$1000,00\033[m")
print(f"O produto mais barato é \033[34m{menorNomeProduto}\033[m e custa \033[34m{menorPrecoProduto:.2f}\033[m")
