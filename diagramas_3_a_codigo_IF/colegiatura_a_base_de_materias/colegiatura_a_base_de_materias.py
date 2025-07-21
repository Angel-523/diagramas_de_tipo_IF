#Angel Alonso Villegas Angulo   Matricula:250217
#algoritmo en el que la entrada es el numero de materias y la salida es la colegiatura
#6to planteamiento de los ejercicios individuales

#solicite el numero de materias
nm= int (input("favor de ingresar el numero de materias tomadas: "))
#realiza el calculo preliminar de la colegiatura
cn= 50*nm
#condicional, el limite de cobro en la colegiatura es 750, si esto se exede se asigna 750 como el costo total
if cn>750:
    coleg= 750
else: coleg= cn

print(f"el total de la colegiatura es {coleg}")