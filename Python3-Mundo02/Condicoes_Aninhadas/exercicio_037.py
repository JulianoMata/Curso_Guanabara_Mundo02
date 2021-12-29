""" ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE
 DE CONVERSÃO:
 -1 PARA BINÁRIO
 -2 PARA OCTAL
 -3 PARA HEXADECIMAL"""

numero = int(input("Digite um número: "))
print(""" Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
conversor = int(input("Digite sua opção: "))
if conversor == 1:
    print(f"{numero} convertido em BINÁRIO é igual a {bin(numero)[2:]}")
    # fatiamento de 'strings' posição 2 ate o final, pois existem 2 caracteres iniciais desnecessários
elif conversor == 2:
    print(f"{numero} convertido em OCTAL é igual a {oct(numero)[2:]:}")
    # fatiamento de 'strings' posição 2 ate o final, pois existem 2 caracteres iniciais desnecessários
elif conversor == 3:
    print(f"{numero} convertido em HEXADECIMAL é igual a {hex(numero)[2:]}")
    # fatiamento de 'strings' posição 2 ate o final, pois existem 2 caracteres iniciais desnecessários
else:
    print("Número inválido!!!")
