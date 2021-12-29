""" Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os
comandos if.. elif.. else em programas Python."""

nome = str(input("Qual é seu nome? "))
if nome == "Gustavo":
    print("Que nome legal!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é popular no Brasil!!!")
elif nome in "Ana Claudia Jessica":
    print("Belo nome menina!!!")
else:
    print("Nome horrível!!!")
print(f"Tenha um bom dia, {nome}!!!")
