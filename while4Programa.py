# Un ciclo de continuar

def main(): #Una funcion principal no le podemos cambiar el nombre
    print('Digite si, para continuar con el programa')
    respuesta = input('Desea continuar con el programa: ') #Capturando la respuesta del mensaje
    
    while respuesta == 'si':
        respuesta = input('Desea continuar con el programa: ')
        
    print('Ha terminado el programa')

if __name__ == '__main__': #Para llamar la funcion main con un while 
    main()                 #necesariamente debo de incluir el if con el nombre de la funcion principal
        
    