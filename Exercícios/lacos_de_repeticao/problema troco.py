preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))

troco = recebido - (preco * quantidade)

print("TROCO = ", "{:.2f}".format(troco)) 
