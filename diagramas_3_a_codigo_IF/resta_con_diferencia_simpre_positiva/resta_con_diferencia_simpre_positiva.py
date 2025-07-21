#Angel Alonso Villegas Angulo   Matricula:250217
#algoritmo que descifre si dos numeros cuentan con signos iguales o opuestos
#3er planteamiento de los ejercicios individuales

num1= float (input("ingrese el primer numero: "))#ingrese el primer numero
num2= float (input("ingrese el segundo numero: "))#ingrese el segundo numero
#realice la operacion
resta= num1-num2

if resta>0:                         #en caso de que la resta sea positiva
    print(f"diferencia es: {resta}")#imprima la resta directamente
else:
    resta=resta*-1                  #caso contrario, multiplique la resta por menos uno para invertir su signo
    print(f"diferencia es: {resta}")#una vez hecho imprima la resta