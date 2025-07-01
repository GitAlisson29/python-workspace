# Exercício: Encontra o menor entre três números

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 < n2 and n1 < n3:
	print("MENOR = ", n1)
	
elif n2 < n1 and n2 < n3:
	print("MENOR = ", n2)

else:
	print("MENOR = ", n3)	
