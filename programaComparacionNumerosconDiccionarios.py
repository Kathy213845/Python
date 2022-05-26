'''Escribir un programa que me compare dos numeros y me diga cual es mayor
los numeros debe ser almacenados en un diccionario'''

diccionario = {"a": 10,
               "b": 20}

if diccionario["a"] == diccionario["b"]:
    print(f"El numero", diccionario["a"], "y", diccionario["b"])
elif diccionario["a"] < diccionario["b"]:
    print(f"El numero", diccionario["a"],"es menor que ", diccionario["b"])
else:
    print(f"El numero", diccionario["a"],"es mayor que ", diccionario["b"])