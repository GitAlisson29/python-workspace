# Exercício: Pede números até o usuário digitar zero

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        print("Encerrando...")
        break
