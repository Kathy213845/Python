
num1 = float(input("Diguite el primer valor: "))
num2 = float(input("Diguite el segundo valor: "))
operacion = input("Diguite la operacion deseada: S=Suma, R=Resta, M=Multiplicacion, D=Division: ") .upper()

if operacion == "S":
    suma = num1 + num2
    print(f"La suma de los numeros es: {suma}")
    
elif operacion == "R":
    resta = num1 - num2
    print(f"La resta de los numeros es: {resta}")

elif operacion == "M":
    multiplicacion = num1 * num2
    print(f"La multiplicacion de los numeros es: {multiplicacion}")
    
elif operacion == "D":
    division = num1 / num2
    print(f"La division de los numeros es: {division}")
    
else:
    print("La operacion no es valida")