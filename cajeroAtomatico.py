# simule un cajero atomatico saldo inicial de 1000 
# con un menu - ingresar - retirar - mostrar - salir
 
saldo = 1000
while True:
    print("\t : menu")
    print("1: ingresar dinero a la cuenta: ")
    print("2: retirar el dinero a la cuenta: ")
    print("3: mostrar el saldo disponible: ")
    print("4: salir: ")
    opcion = int(input("Diguite la opcion del menu: "))
    print()


    if opcion == 1: # desea continuar reto
        cantidad = float(input("cuanto dinero desea ingresar: "))
        #saldo = saldo + cantidad
        saldo += cantidad
        print(f"Su nuevo saldo es: {saldo}")
        
    elif opcion == 2:
        retirar = float(input("Cuanto desea retirar: "))
        if retirar > saldo:
            print("No tiene fondos suficientes")
            
        else:
            saldo -= retirar
            print(f"Su nuevo saldo es: {saldo}")
            
    elif opcion == 3:
        print(f"Su nuevo saldo es: {saldo}")
        
    elif opcion == 4:
        print("Gracias por utilizar nuestros servicios")
        break
    else:
        print("Entrada no valida")
        