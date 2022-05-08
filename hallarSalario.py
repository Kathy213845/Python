def salarioPorHora(salario:float, hora:int):
    salario = hora * salario
    return "El salario semanal es: {}" .format(salario)

hora = int(input("Diguite la hora: "))
salario = float(input("Duiguite su salario por horas: "))

print(salarioPorHora(hora, salario))