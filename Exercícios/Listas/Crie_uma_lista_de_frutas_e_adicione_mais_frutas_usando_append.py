# Exercício: Cria lista de frutas e adiciona mais frutas com append

frutas = ["Banana", "Maçã", "Pera"]

for i in range(2):
    nova_fruta = input("Digite o nome de uma fruta para adicionar: ")
    frutas.append(nova_fruta)

print("Lista de frutas:", frutas)
