#Angel Alonso Villegas Angulo   Matricula:250217
#calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es de $800 si se compran menos de 5, y $700 si se compran 5 o mas.

#1er planteamiento de los ejercicios grupales

#solicita la cantidad de llantas
CL= int (input("cantidad de llantas a comprar: "))
#segun la cantidad de las llantas se aplica un precio diferente
if CL>5:
    Total= CL*700
else: Total= CL*800
#devuelva el total
print(f"el cobro total es de ${Total}")