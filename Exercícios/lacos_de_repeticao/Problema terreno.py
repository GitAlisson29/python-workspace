largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
metro_quadrado = float (input("Digite o valor do metro quadrado: "))

area = largura * comprimento
preco = area * metro_quadrado

print("Area do terreno: ", "{:.2f}".format(area))
print("Preco do terreno: ", "{:.2f}".format(preco))
