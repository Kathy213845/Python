#Bucle positivo raiz

import math

numero = int(input('Digite el numero: '))

while numero < 0:
    print('El numero ingresado es negativo')
    numero = int(input('Debe registrar un numero positivo: '))
    
print(f'la raiz es: {(math.sqrt(numero)): .2f}')

#sqrt es raiz cuadrada
#.2f es un formato de salida saca dos decimales
#.4f saca 4 decimales