def calificaciones(informacion:dict):
   nota = informacion["nota1"] 
   
   if nota >= 0 and nota <=5:
       return "Su nota es insuficiente"
   
   elif nota > 5 and nota <=7:
       return "Su nota es suficiente"
   
   elif nota > 7 and nota <=9:
       return "Su nota esta bien"
   
   elif nota > 9 and nota <=10:
       return "Su nota es excelente"
   
   else:
       return "Su nota es invalida"
   
nota1 = float(input("Ingrese su nota: "))

informacion = {"nota1":nota1}  

print(calificaciones(informacion))   

'''Llamamos la funcion con un print porque
en la funcion tenemos return'''   