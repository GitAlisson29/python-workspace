# Exercício: Lê 5 números, armazena em lista e soma

numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = 0
for n in numeros:
    soma += n

print(f"A soma dos números é {soma}.")
