""" DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA. CALCULE SEU IMC E MOSTRE SEU STATUS, DE
ACORDO COM A TABELA ABAIXO:
- ABAIXO DE 18.5: ABAIXO DO PESO
- ENTRE 18.5 E 25: PESO IDEAL
- 25 ATÉ 30: SOBREPESO
- 30 ATÉ 40: OBESIDADE
- ACIMA DE 40: OBESIDADE MÓRBIDA"""

peso = float(input("Digite seu peso: (kg) "))
altura = float(input("Digite sua altura: (m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc <= 18.5:
    print("Abaixo do peso.")
elif imc <= 25:
    print("Peso ideal.")
elif imc <= 30:
    print("Sobrepeso.")
elif imc <= 40:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")
