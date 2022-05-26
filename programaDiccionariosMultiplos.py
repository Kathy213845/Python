'''Realice un programa que compruebe dos numeros y que diga si es multiplo'''
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input('Diguite el segundo numero: '))  #Entrada

numeros = {"numero1": numero1,
           "numero2": numero2
           }

def multiplos(numeros:dict):
    num1 = numeros["numero1"] #clave
    num2 = numeros["numero2"]                           #Proceso
    
    if num1 >= num2 and num1% num2 != 0:
        return num1, "no es multiplo de ", num2
    elif num1 >=2 and num1 % num2 == 0:
        return num1, "es multiplo de ", num2
    elif num2 >= num1 and num2 % num1 != 0:
        return num2, "no es multiplo de ", num1
    
    else: num2, "es multiplo de ", num1
    
    print(multiplos(numeros))                           #Salida