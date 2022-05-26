num1 = float(input("Por favor ingrese el numero 1: "))
num2 = float(input("Por favor ingrese el numero 2: "))
num3 = float(input("Por favor ingrese el numero 3: "))

if (num1 >= num2 and num1 >= num3):
    print(f"El numero mayor es el {num1}")
    
elif (num2 >= num1 and num2 >= num3):
    print(f"El numero mayor es el {num2}")
    
elif(num3 >= num1 and num3 > num2):
    print(f"El numero mayor es el {num3}")
    
else:
    print("Los numeros son iguales") # CORREGUIR NO funciona el igual.