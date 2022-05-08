def dinero(dineguillermo:float):
    luis = dineguillermo / 2
    juan = (luis + dineguillermo) / 2
    total = dineguillermo + luis + juan
    return "Juan tiene un total de: {} Luis tiene un total de: {} el total de los tres es de: {}" .format(juan, luis, total)

dineguillermo = float(input("Diguite la cantidad de dinero que tiene guillermo"))

print(dinero(dineguillermo))