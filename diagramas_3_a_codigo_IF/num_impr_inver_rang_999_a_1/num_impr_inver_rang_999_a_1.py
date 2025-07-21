#Angel Alonso Villegas Angulo   Matricula:250217
#elaborar un algoritmo para invertir una cifra almacienda en una variable "A" de tal manera que si ingresa 834 debe darle como salida 438, el dato ingresado debe estar en un rango de 1 y 999.

#ingrese en numero
print("el rango de entrada permitido es de 1-999")
A= float (input("ingrese un numero dentro del rango: "))
#condiciones por rango
if A>999:
    print("fuera de rango")
    quit
elif A>1:
    if A<10:
        print(f"{A} al ser de un digito sigue igual")   #resultado de un digito
        exit()
    elif A>100:
        A1= (A//100)
        A2= (A%100)//10
        A3= (A%10)
        inv= (A1)+(A2*10)+(A3*100)
        print(f"{A} invertido es {inv}")            #resultado invertido de 3 digitos
        exit()
    else: A1= (A//10) 
    inv = float ((A%10)*10+A1)
    print(f"{A} invertido es {inv}")                    #resultado invertido de 2 digitos
    exit()
else: print("fuera de rango")
exit()