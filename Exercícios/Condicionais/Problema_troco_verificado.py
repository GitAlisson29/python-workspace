# Exercício: Calcula troco ou informa dinheiro insuficiente

preco = float(input("Preço unitário do produto: "))
quantidade = float(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))

troco = recebido - preco * quantidade 

if troco > 0:	
	print ("TROCO = ", "{:.2f}".format(troco))
else:
	falta = troco * (-1)
	print("DINHEIRO INSUFICIENTE. FALTAM, ", "{:.2f}".format(falta), " REAIS")
