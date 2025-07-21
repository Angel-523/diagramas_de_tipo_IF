#Angel Alonso Villegas Angulo   Matricula:250217
#elabore un algoritmo que calcule su edad actual en (dd-mm-aaaa)
#7mo planteamiento de los ejercicios individuales
#solicite la fecha de nacimiento
fecha_n= input("ingrese la fecha de nacimiento en (dd-mm-aaaa): ")
n_dia= int (fecha_n[0:2])
n_mes= int (fecha_n[4:5])
n_año= int (fecha_n[7:10])
#solicite la fecha
fecha_actual= input("ingrese la fecha actual en (dd-mm-aaaa): ")
dia_actual= int (fecha_actual[0:2])
mes_actual= int (fecha_actual[4:5])
año_actual= int (fecha_actual[7:10])
#calcula la edad
E_años= (año_actual - n_año)
E_meses=(mes_actual - n_mes)
#revisa si el año vigente cumple con los meses suficientes
if mes_actual<n_mes:
    E_años= E_años-1
    E_meses= (n_mes-12)*(-1)+mes_actual
    print(f"la edad de alguien nacido en {fecha_n} a dia de {fecha_actual} es de {E_años} años con {E_meses} meses")
else: print(f"la edad de alguien nacido en {fecha_n} a dia de {fecha_actual} es de {E_años} años con {E_meses} meses")