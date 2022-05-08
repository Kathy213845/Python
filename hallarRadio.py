def circulo(radio: float):
    area = (3.1416 *(radio ** 2))
    return "El area d450el circulo es : {}" .format(area)

radio = float(input("Diguite el radios del circulo: "))

print(circulo(radio))