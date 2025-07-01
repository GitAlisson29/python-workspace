# Exercício: Cria tupla e encontra maior e menor valor

numeros = (15, 8, 22, 5, 19)

maior = numeros[0]
menor = numeros[0]

for i in range(5):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]

print("Maior:", maior)
print("Menor:", menor)
