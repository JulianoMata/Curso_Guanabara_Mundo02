""" CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SAU MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL,
DE ACORDO COM A MÉDIA ATINGIDA:
- MÉDIA ABAIXO DE 5.0:
REPROVADO
- MÉDIA ENTRE 5.0 E 6.9:
RECUPERAÇÃO
- MÉDIA 7.0 OU SUPERIOR:
APROVADO"""

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
media = (nota01 + nota02)/2
print(f"Tirando {nota01:.1f} e {nota02:.1f} a média é {media:.1f}")
if media >= 7:
    print("APROVADO")
elif 5 < media < 7:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")



