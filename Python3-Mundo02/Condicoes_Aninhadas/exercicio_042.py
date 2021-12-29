""" REFAÇA O EXERCÍCIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO
SERÁ FORMADO:
- EQUILÁTERO: TODOS OS LADOS IGUAIS
- ISÓSCELES: DOIS LADOS IGUAIS
- ESCALENO: TODOS OS LADOS DIFERENTES"""

a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))
if a < b + c and b < a + c and c < a + b:
    print("Pode formar um triângulo", end="")
    if a == b == c:
        print("Equilátero")
    elif a == b or b == c or a == c:
        print("Isósceles")
    else:
        print("Escaleno")  # a != b != c != a "seria outra forma"

else:
    print("Não é triângulo!!!")
