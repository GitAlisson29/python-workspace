# Exercício: Lê 5 nomes e cria uma tupla

nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

nomes_tupla = tuple(nomes)

for i in range(5):
    print(nomes_tupla[i])
