""" ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO
NORMAL E CONDIÇÃO DE PAGAMENTO:
- À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
- À VISTA NO CARTÃO: 5% DE DESCONTO
- EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
- 3X OU MAIS NO CARTÃO:
20% DE JUROS"""

print(f"{' JFMATTA - SERVIÇOS DE TI ':*^60}")  # CENTRALIZAR TÍTULO

total = 0  # não é obrigatório
valor = float(input("Digite o valor do produto: R$"))
pagamento = int(input("""Digite a forma de pagamento: 
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] EM ATÉ 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO\n"""))

if pagamento == 1:
    total = valor - valor * 0.1
elif pagamento == 2:
    total = valor - valor * 0.05
elif pagamento == 3:
    total = valor
    parcela = total / 2
    print(f"Sua compra foi parcelada em 2x de R${parcela:.2f} sem juros")
elif pagamento == 4:
    total = valor + valor * 0.2
    totalParcelas = int(input("Quantas parcelas? "))
    parcela = total / totalParcelas
    print(f"Sua compra foi parcelada em {totalParcelas}x de R${parcela:.2f} com juros")
else:
    print("Valor Inválido")
print(f"Valor é {valor:.2f} e você vai pagar: R${total:.2f}")
