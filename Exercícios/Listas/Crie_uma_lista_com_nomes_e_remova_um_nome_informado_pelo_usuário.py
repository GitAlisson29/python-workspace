# Exercício: Cria lista de nomes e remove um nome digitado

nomes = ["Ana", "Bruno", "Carla", "Diego", "Eduarda"]

print("Lista original:", nomes)

nome_remover = input("Digite o nome que deseja remover: ")

if nome_remover in nomes:
    nomes.remove(nome_remover)
    print("Nome removido.")
else:
    print("Nome não encontrado.")

print("Lista atualizada:", nomes)
