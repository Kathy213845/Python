nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

persona = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "anios": 0
}

def edadAlta (persona:dict):
    name = persona["nombre"]
    lastname = persona["apellido"]
    age = persona["edad"]
    year = persona["anios"]
    
    if age >=0 and age < 18:
        year = 2022 - age #Hallo el a;os de nacimiento
        mayorEdad = year + 18 #Cuando cumple los 18 a;os
        return name, lastname, "eres menor de edad no podemos darte de alta hasta ", mayorEdad
    
    elif age > 18 and age < 25:
        return "tienes un 10%  de descuento"
    elif age > 25 and age < 100:
        return "Lo sentimos, no tienes descuento"
    elif age ==18 or age ==25:
        return "Premio, tienes un descuento especial del 20%"
    elif age < 0:
        return "no se puede calcular la edad"
    elif age >= 100:
        return "sigue vivo ?"
    
    else:
        return "dato no es valido"
    
    
print(edadAlta(persona))