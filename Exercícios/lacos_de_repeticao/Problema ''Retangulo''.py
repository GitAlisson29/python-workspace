import math 
b = float(input("Base do retangulo: "))
h = float(input("Base do retangulo: "))

Area = b * h
Perimetro = 2 * (b + h)
Diagonal = math.sqrt((b**2)+(h**2))

print("AREA: ", "{:.4f}".format(Area))
print("PERIMETRO: ", "{:.4f}".format(Perimetro))
print("Diagonal: ", "{:.4f}".format(Diagonal))
