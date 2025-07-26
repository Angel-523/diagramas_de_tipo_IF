#Angel Alonso Villegas Angulo   Matricula:250217
#calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico,se aplica una formula diferente segun el sexo del usuario
#femenino: puls=(220-edad)/10
#masculino: puls=(210-edad)/10
#3er planteamiento de los ejercicios grupales

#solicite los valores con los que se trabajara
print("al ingresar su genero, use la letra F para referirse a femenino; caso contrario, M para referirse a masculino ")
genero= str (input("favor de ingresar su genero: "))
edad= float (input("favor de ingresar su edad: "))

#divida el procedimiento segun los datos ingresados
if genero == "F" or genero == "f" or genero == "Female" or genero == "female" or genero == "fem" or genero == "Fem":
    puls=(220-edad)/10
    print(f"la cantidad de pulsaciones cada 10 segundos de una mujer de {edad} años haciendo ejercicios aeróbicos es de {puls}")
    exit()
elif genero == "M" or genero == "m" or genero == "Masculino" or genero == "masculino" or genero == "mas" or genero == "Mas":
    puls=(210-edad)/10
    print(f"la cantidad de pulsaciones cada 10 segundos de un hombre de {edad} años haciendo ejercicios aeróbicos es de {puls}")
    exit()
else:
    print("introdujo valores invalidos")
    exit()