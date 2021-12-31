""" Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos """
pesoMaior = 0
pesoMenor = 0
for pessoa in range(1, 6):
    peso = float(input(f"Digite o peso da {pessoa}ª pessoa: "))
    if pessoa == 1:        # primeiro peso é o maior o menor
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso


print(f"O maior peso é {pesoMaior:.1f}Kg e o menor peso é {pesoMenor:.1f}Kg")

