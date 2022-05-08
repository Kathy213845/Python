def vel(tiempo: int, distancia: int):
    velocidad = distancia/tiempo
    return "La velocidad es: {} metros/segundos" .format(velocidad)

tiempo = int(input("Diguite la distancia (segundos): "))
distancia = int(input("Diguite la distancia (en metros): "))

print(vel(tiempo,distancia))