'''Escribe un programa que pregunte al usuario su nombre, edad
direccion y telefono y lo guarde en un diccionario.
Despues debe msotrar por pantalla el mensaje <nombre> tiene
<edad> años, vive en <direccion> y su telefono es <telefono>'''


nombre = input("Por favor digite su nmbre: ")
edad = input("Por favor digite su edad: ")
direccion = input("Por favor digite su direccion: ")
telefono = input("Por favor digite su telefono: ")

#Crear el diccionario para guardarlo
persona = {'nombre':nombre, 
           'edad':edad, 
           'direccion':direccion, 
           'telefono':telefono}

#Ahora el mensaje especifico

print(persona["nombre"], "tiene", persona["edad"], "años, vive en: ", persona["direccion"], "y su telefono es: ", persona["telefono"])