import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Existe uma raiz real: x = {x:.2f}")
else:
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    
    print(f"x1 = {x1:.4f}")
    print(f"x2 = {x2:.4f}")


# Exercício: Calcula as raízes de uma equação do 2º grau (Bhaskara)
