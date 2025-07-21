#Angel Alonso Villegas Angulo   Matricula:250217
#identifica de tres numeros cual es el mayor
#1er planteamiento de los ejercicios individuales
num1= float (input("ingrese el primer numero: "))
num2= float (input("ingrese el segundo numero: "))
num3= float (input("ingrese el tercer numero: "))

#establesca la escala y condiciones
#si num1 es mayor o igual que num2 y num1 es mayor o igual que num3 
if num1>=num2 and num1>=num3:
    max=num1
#si num2 es igual o mayor que num1 y num2 es igual o mayor que 
elif num2>num3:
    max=num2
else: max=num3

print({max})