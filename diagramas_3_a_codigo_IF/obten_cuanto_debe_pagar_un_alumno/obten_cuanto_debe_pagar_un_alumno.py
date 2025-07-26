#Angel Alonso Villegas Angulo   Matricula:250217
#en una escuela se otorga un descuento del 30% en funcion de si el promedio durante su ultimo periodo llega a cierto umbral(9), caso contrario, se aplicara un iva del 10%.
#4to planteamiento de los ejercicios grupales

#valores establecidos
des=0.3 #o tambien se entiende como un multiplicador del 30%
iva=0.1 #o tambien se entiende como un multiplicado del 10%

#solicita el promedio y la colegiatura
prom= float (input("ingrese el promedio alcansado: "))
coleg= float (input("ingrese la colegiatura total sin descuentos, ni iva: "))

#se alcanso el umbral?
if prom >= 9:
    total= coleg-(coleg*des)
    print(f"el monto total que el alumno tendra que pagar es de {total} pesos con descuentos y sin iva")
else: 
    total= coleg+(coleg*iva)
    print(f"el monto total que el alumno tendra que pagar es de {total} pesos con iva y sin descuentos")