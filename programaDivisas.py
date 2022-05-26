'''Escribir un programa que guarde en una variable el diccionario
{'Euro':' ', 'Dollar':'$', 'Yen':' '}. 
pregunte al usuario por una divisa y muestre su
simbolo o un mensaje de aviso si la divisa no esta en el diccionario'''

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':' ¥'}

divisa = input("Diguite la divisa: ")

#.title si la persona escribe en mayuscula o minuscula lo pueda identificar
if divisa.title() in monedas: 
    print(monedas[divisa.title()])
    
else: 
    print("Lo sentimos, no se encuentra la divisa")
    