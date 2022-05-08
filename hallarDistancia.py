def distancia(velocidad:float, tiempo:float):
    distancia = velocidad * tiempo
    return "La distancia recorrida es: {} km/h" .format(distancia)

velocidad = float(input("Ingrese la velocidad: "))
tiempo = float(input("Ingrese el tiempo: "))

print(distancia(velocidad, tiempo))