""" ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
 - O PRIMEIRO VALOR É MAIOR
 - O SEGUNDO VALOR É MAIOR
 - O NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS """

num01 = int(input("Digite o primeiro número: "))
num02 = int(input("Digite o segundo número: "))
if num01 > num02:
    print(f"Primeiro número {num01} é MAIOR que o segundo número {num02}!!!")
elif num02 > num01:
    print(f"O segundo número {num02} é MAIOR que o primeiro número {num01}!!!")
else:
    print(f"O primeiro número {num01} e o segundo numero {num02} são iguais!!! ")
