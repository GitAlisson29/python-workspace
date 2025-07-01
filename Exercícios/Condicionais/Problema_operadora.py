minutos = int(input("Digite a quantidade de minutos: "))

plano =  50.00

if minutos >= 100:
	restante = minutos - 100
	valor = restante * 2.00 + plano
	print("Valor a pagar: R$ ", "{:.2f}".format(valor))
else: 
	print("Valor a pagar: R$ ", "{:.2f}".format(plano))	


# Exercício: Calcula valor excedente de minutos em plano de telefonia

# Entrada dos minutos utilizados
