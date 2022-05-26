letra = input('Por favor diguite la letra: ') .lower() #Si el programa tiene las letras minusculas puede determinar las mayusculas
                                             #upper() 

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra es una vocal")
    
else:
    print("Letra es una consonante")