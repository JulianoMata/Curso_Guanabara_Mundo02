""" Crie um programa que leia uma frase qualquer e diga se ela é um 'políndromo', desconsiderando
os espaços"""

"""Ex:
Apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
tem o mesmo significado de trás p frente"""

frase = str(input("Digite uma frase: \n")).strip().upper()  # elimina espaços e devolve em maiúsculas
palavras = frase.split()  # separar a frase em palavras numa lista
junto = "".join(palavras)  # junta numa string
# inverso = ""
# for letra in range(len(junto) - 1, - 1, - 1):  # criando o inverso
#     inverso += junto[letra]
inverso = junto[::-1]   # maneira mais simples de fazer sem o 'for', utilizando fatiamento
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("A frase é um palíndromo")
else:
    print('A frase não é um palíndromo')
