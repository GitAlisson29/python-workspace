# Exercício: Mostra o estado civil pela letra inicial

letra = input("Digite a letra inicial do estado civil (S, C, V, D): ").upper()

if letra == "S":
    print("Solteiro(a).")
elif letra == "C":
    print("Casado(a).")
elif letra == "V":
    print("Viúvo(a).")
elif letra == "D":
    print("Divorciado(a).")
else:
    print("Estado civil inválido.")
