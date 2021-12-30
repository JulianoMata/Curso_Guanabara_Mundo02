"""  Faça um programa que mostre uma contagem regressiva na tela para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles. """

# usar sleep


from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print("FELIZ ANO NOVO!!!")

##############################################################################
for cont in range(7, 0, -1):
    print(cont)
print("Fim")

##############################################################################

num = int(input("Digite um número: "))
for cont in range(0, num + 1):
    print(cont)
print("Fim")

##############################################################################

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Intervalo: "))  # intervalo ou passo
for cont in range(i, f, p):
    print(cont)
print("Fim")

##############################################################################################

soma = 0
for cont in range(0, 5):
    num = int(input("Digite o valor: "))
    soma += num
print(f"A soma de todos valores foi {soma}")

##########################################################################################
