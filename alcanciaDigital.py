def main():
    print("Alcancia Digital")
    
    objetivo = float(input('Cuanto desea ahorrar?: '))
    
    ahorrado = 0.0
    while objetivo >= ahorrado:
        ahorrado += float(input('Cuanto va a depositar?: '))
        limite = objetivo == objetivo
        restante = objetivo - ahorrado
    print(f'Has ahorrado {limite}, y le sobra {restante}')  

if __name__ == "__main__":
    main()  