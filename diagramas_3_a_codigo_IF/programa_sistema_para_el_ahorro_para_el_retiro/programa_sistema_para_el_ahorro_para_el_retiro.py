#Angel Alonso Villegas Angulo   Matricula:250217
#
#5to planteamiento de los ejercicios grupales
#solicite la variable salario como salario mensual

salario= float (input("ingrese el salario mensual sin deducciones: "))
#solicite si el usuario depende de la deduccion predeterminada o una personalisada
print("favor de responder con Y para afirmar o N para negar")
y_n= str (input("la deduccion es impuesta por el usuario: "))
if y_n in ["Y","y","S","s","si","Si","SI","Yes","YES","YEs"]:
    
    print("responda con una C en caso de tratarse de cuotas fijas; o una P en el caso de ser un porcentaje")
    p_c= str(input("es una cuota fija o un porcentaje: "))
    if p_c in ["P","p","%","porcentaje","por","porce"]:
        print("favor de ingresar el porcentaje en decimales, ejemplos: 60% = 0.6, 25% = 0.25, 5.5% = 0.055")
        porcentaje= float (input("ingrese el porcentaje: "))
        #calcule la deduccion o diferencia
        deduccion= salario*porcentaje
        #calcule el resto del salario tras las deducciones
        total_s= salario-deduccion
        #calcule la suma que se le agrega a la cuenta
        total_c_a= float (input("favor de ingresar el saldo de la cuenta antes de agregar el aporte: "))
        total_c= total_c_a+deduccion
        print(f"en caso de no haber cambios en el salario o deducciones, cada mes la cuenta de ahorros del ´SAR´ recibe {deduccion} pesos, teniendo la cuenta un total de {total_c} pesos, y el salario restante del mismo mes, es de {total_s} pesos")
        exit()
    elif p_c in ["C","c","Cuota","Cuotas","cuota fija","Cuota fija","Cuota Fija","cuota fija","cuota","cuotas"]: 
        print("favor de ingresar una cuota razonable, que no exceda el salario mensual")
        cuota= float (input("favor de ingresar la cuota fija: "))
        if cuota>salario:
            print("valor invalido")
            exit()
        else: deduccion=cuota
        #calcule el resto del salario tras las deducciones
        total_s= salario-deduccion
        #calcule la suma que se le agrega a la cuenta
        total_c_a= float (input("favor de ingresar el saldo de la cuenta antes de agregar el aporte: "))
        total_c= total_c_a+deduccion
        print(f"en caso de no haber cambios en el salario o deducciones, cada mes la cuenta de ahorros del ´SAR´ recibe {deduccion} pesos, teniendo la cuenta un total de {total_c} pesos, y el salario restante del mismo mes, es de {total_s} pesos")
        exit()
    else:
     print("valor invalido")
     exit()
elif y_n in ["N","n","No","no"]:
 porcentaje =0.065
 deduccion=salario*porcentaje
 total_s=salario-deduccion
 total_c_a= float (input("favor de ingresar el saldo de la cuenta antes de agregar el aporte: "))
 total_c= total_c_a+deduccion
 print(f"en caso de no haber cambios en el salario o deducciones, cada mes la cuenta de ahorros del ´SAR´ recibe {deduccion} pesos, teniendo la cuenta un total de {total_c} pesos, y el salario restante del mismo mes, es de {total_s} pesos")
 exit()
else:
 print("valor invalido")
 exit()