def promedio(nota1:float, nota2:float, nota3:float):
    promedio = (nota1 + nota2 + nota3)/3
    return "El promedio del estudiante es: {} " .format(promedio)

nota1 = float(input("Diguite la nota 1: "))
nota2 = float(input("Diguite la nota 2: "))
nota3 = float(input("Diguite la nota 3: "))

print(promedio(nota1, nota2, nota3))