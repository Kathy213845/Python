'''Escribir un programa que guarde en un diccionario los precios de las frutas
de la tabla, pregunte al usuario por una fruta, un nuero de kilos y muestre por 
pantalla el precio ese numero de kilos de fruta. Si la fruta no esta en el diccionario
debe mostrar un mensaje informando de ello.'''

frutasDicc = {"guanabana":10.3,"mango":30.2, "banano":20.3, "naranja":5.5}
fruta = input("Que fruta desea comprar? : ").title()
kilos = input(float("Cuantos kilos desea? : "))

if fruta in frutasDicc:
    print("Para la fruta ", fruta, kilos, "kilos, tiene un costo de: ", frutasDicc[fruta]*kilos)
else:
    print(f"Lo siento la fruta: {fruta}, no esta disponible")    