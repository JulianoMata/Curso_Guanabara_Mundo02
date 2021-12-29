""" ESCREVA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
- SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
- SE É A HORA DE ALISTAR.
- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO."""

from datetime import date
anoAtual = date.today().year
# BUSCA A DATA ATUAL NO SISTEMA
ano_nasc = int(input("Digite seu ano de nascimento: "))
idade = anoAtual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} em {anoAtual}")

if idade < 18:
    prazo = 18 - idade
    print(f"Ainda falta(m) {prazo}ano(s) para o serviço militar")
    anoAlistamento = anoAtual + prazo
    print(f"Seu alistamento será em {anoAlistamento}")
elif idade == 18:
    print("Hora de se alistar")
else:
    prazo = idade - 18
    print(f"Já serviu ou passou do prazo em {prazo}ano(s) para alistamento militar")
    anoAlistamento = anoAtual - prazo
    print(f"O ano de seu alistamento foi {anoAlistamento}")
