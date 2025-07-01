# Exercício: Imprime a tabuada do número digitado pelo usuário

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
