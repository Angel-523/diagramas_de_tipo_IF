#Angel Alonso Villegas Angulo   Matricula:250217
#escriba un algoritmo que lea dos numeros enteros como entrada y escriba el mensaje "signos opuestos" si solo uno es positivo y el otro negativo
#2do planteamiento de los ejercicios individuales

#solicite los dos numeros enteros
num1= int (input("ingrese el primer numero: "))
num2= int (input("ingrese el segundo numero: "))
#primera condicion
if num1>0:                              #se prueba si num1 es positivo o negativo
    if num2<0:                          #num1+ fue positivo, y se prueba si num2 es negativo
        print(f"Signos Opuestos")                   #num2- y num1+ fueron de signos opuestos
    else: print(f"signos iguales")                  #num2+ y num1+ resultaron de signos iguales
elif num2>0:                            #num1- fue negativo y se revisa el signo de num2
    if num2>0:                          #se revisa a num2 con redundancia para poder acomodar la linea
        print(f"Signos Opuestos")                   #num2+ y num1- son de signos opuestos
else: print(f"signos iguales")                      #num2- y num1- son de signos iguales