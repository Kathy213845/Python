can = int(input("Cuantos dulces deseas: "))
tipo = int(input("Que tipo de dulce desea: (1 - 2 - 3): "))
dulceria = {"can":can, "tipo":tipo, "precio":0, "monto":0}

if dulceria["tipo"] ==1:
    dulceria["precio"]=3
    dulceria["monto"] = dulceria["can"]*dulceria["precio"]
    if dulceria["can"] <=5:
        dulceria["monto"]-= 0.5 #monto = monto - 0.5
    elif dulceria["can"] <= 10:
        descuento = dulceria["monto"]*0.07
        dulceria["monto"] -= descuento
        
elif dulceria["tipo"] ==2:
    dulceria["precio"]=4
    dulceria["monto"] = dulceria["can"]*dulceria["precio"]
    if dulceria["can"] >7:
        dulceria["monto"]-= 0.5 #monto = monto - 0.5
    elif dulceria["can"] <= 10:
        descuento = dulceria["monto"]*0.05
        dulceria["monto"] -= descuento

elif dulceria["tipo"] ==3:
    dulceria["precio"]=5
    dulceria["monto"] = dulceria["can"]*dulceria["precio"]
    if dulceria["can"] >4:
        dulceria["monto"]-= 0.5 #monto = monto - 0.5
    elif dulceria["can"] <= 10:
        descuento = dulceria["monto"]*0.15
        dulceria["monto"] -= descuento
        
else: 
    print('tipo de dulce no disponible')

print('el tipo de dulce', dulceria["tipo"],
      'tiene un costo unitario', dulceria["precio"],
      'el numero de dulces comparados:', dulceria["can"])
print('tiene un costo total de:', dulceria["monto"])