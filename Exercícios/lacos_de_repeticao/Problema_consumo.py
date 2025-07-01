distancia = int(input("Distancia percorrida: "))
combustivel = float(input("Combustível gasto: "))

consumo = distancia / combustivel

print("Consumo medio = ", "{:.3f}".format(consumo))
