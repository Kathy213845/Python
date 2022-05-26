fruta = "banana"
letra = fruta[0] #imprime la posicion de la palabra banana
print(letra)

verdura = "pepino"
longitud = len(verdura)
ultimo = verdura[longitud -1] #impreme la ultima letra
print(ultimo)
print(longitud)

mensaje = "Hoy es martes"
print(mensaje[0:3])
print(mensaje[7:13])

hola = "Hoy es martes, "
if hola == "Hoy es martes, ":
   print(f"{hola} lo se")

print(dir(hola))

texto = "Hola Kathy estas triunfando"
nueva = texto.lower() #imprime el texto en mayuscula
print(nueva)

texto1 = "Amo a mi mama"
otra = texto1.find("o") #Imprime la posicion que tiene una letra
print(otra)

texto2 = "    Hola kathy"
otra1 = texto2.strip()
print(otra1)


texto3 = "La vida es bella"
otra2 = texto3.startswith("la") # si la palabra se encuentra en el texto


num = 2
print(" a ls %d tenemos clase " %num)

mensaje1 = "Tenemos que practicar todos los dias"
print(mensaje1.count("os"))
print(mensaje1.count("os", 10))
print (mensaje1.count("os",0,10))
print(mensaje1.replace("os", "es"))
