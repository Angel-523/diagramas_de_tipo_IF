#Angel Alonso Villegas Angulo   Matricula:250217
#
#2do planteamiento de los ejercicios grupales

#solicita el monto de la compra
Compra= float (input("ingrese el total de la compra: "))
num= int (input("ingrese un numero aleatorio: "))
#aplique el descuento en funcion del num elegido
if num>=74:
    des=.20
else: des=.15
#obten la cantidad de dinero descontada a la compra total
total_des= Compra*des
#imprime el total
print(f"el dinero descontado de la compra de {Compra} pesos, es de un total de {total_des} pesos.")