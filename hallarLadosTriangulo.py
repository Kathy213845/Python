def triangulo(base:float, lado:float, altura:float):
    perimetro = base + lado + altura
    area = base * (altura/2)
    return "El perimetro del triangulo es: {} en y el area es de: {} " .format(perimetro, area)

base = float(input("Diguite la base del triangulo: "))
lado = float(input("Diguite el lado del triangulo: "))
altura = float(input(input("Diguite la altura del triangulo: ")))

print(triangulo(base, lado, altura))