def numeros(informacion:dict) ->dict(): #Esto es un diccionario
    a = informacion ["numero1"]
    b = informacion ["numero2"]
    c = informacion ["numero3"]
    
    if (a > b and b > c):
        print(f"el orden de los numeros de mayor a menor es: {a}, {b}, {c}")
        
    elif (a > c and c > b):
         print(f"el orden de los numeros de mayor a menor es: {a}, {c}, {b}")
    
    elif(b > a and a > c):
         print(f"el orden de los numeros de mayor a menor es: {b}, {a}, {c}")
         
    elif(b > c and c > a):
         print(f"el orden de los numeros de mayor a menor es: {b}, {c}, {a}")
         
    elif(c > a and a > b):
         print(f"el orden de los numeros de mayor a menor es: {c}, {a}, {b}")
         
    elif(c > b and b > a):
         print(f"el orden de los numeros de mayor a menor es: {c}, {b}, {a}")
         
    else:
        print("Algunos de los numeros son iguales")
        
informacion = {"numero1": 1, "numero2": 3, "numero3":4}

numero1 = int(input("ingrese el numero 1: "))
numero2 = int(input("ingrese el numero 2: "))
numero3 = int(input("ingrese el numero 3: "))

informacion = {'numero1':numero1, 'numero2':numero2, 'numero3':numero3}

numeros(informacion) #llamado de la funcion sin el print