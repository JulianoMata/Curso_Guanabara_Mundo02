""" Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os
comandos if.. elif.. else em programas Python."""

# nome = str(input("Qual é seu nome? "))
# if nome == "Gustavo":
#     print("Que nome legal!")
# elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
#     print("Seu nome é popular no Brasil!!!")
# elif nome in "Ana Claudia Jessica":
#     print("Belo nome menina!!!")
# else:
#     print("Nome horrível!!!")
# print(f"Tenha um bom dia, {nome}!!!")


"""  ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
 O PROGRAMA VAI PERGUNTAR O VALOR DA CASA , O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
 CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO 
 O EMPRÉSTIMO SERÁ NEGADO."""

valor_casa = float(input("Qual valor do imóvel? R$"))
salario = float(input("Quanto você recebe de salário? R$"))
anos = int(input("Em quantos anos você pretende pagar? "))

prestacao = valor_casa / (anos * 12)
print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} a prestação será R${prestacao:.2f}")

if prestacao <= salario * 0.3:
    print("Empréstimo concedido!")
else:
    print("NEGADO!!! Talvez numa próxima vez!!!")
