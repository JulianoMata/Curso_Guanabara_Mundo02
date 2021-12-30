""" Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher,
contudo, utilizando agora um laço (for)"""

num = int(input("Digite um numero para ver sua tabuada: "))
for cont in range(1, 11):
    print(f"{num} x {cont:2} = {num * cont}")
    # onde ":2" para alinhar os números com uma casa na tabuada



