# Programa para calcular a nota final de um aluno com base em duas notas semestrais.
# Se a soma das duas notas for maior ou igual a 60.0, o aluno é aprovado.
# Caso contrário, o programa deve exibir a nota final com uma casa decimal e a mensagem "REPROVADO".


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

total = nota1 + nota2

if total > 60.00:
	print("NOTA FINAL: ", "{:.1f}".format(total))
else: 
	print("NOTA FINAL: ", "{:.1f}".format(total))
	print("REPROVADO")
