#Angel Alonso Villegas Angulo   Matricula:250217
#resumen: el gobierno quiere reforestar, siguiendo algunas pautas, tambien desea saber el numero y tipo de arboles en los terronos dichos
#6to planteamiento de los ejercicios grupales
#solicite las hectarias del terreno
hectarias= int (input("favor de ingresar el numero de hectarias del terreno: "))
#convierte las hectarias para trabajar con metros cuadrados
m_2= hectarias*10000

#ahora, segun los requisitos puestos en el planteamiento
if m_2>1000000:
    pin= (m_2*0.7)*(8/10)
    oya= (m_2*0.2)*(15/15)
    ced= (m_2*0.1)*(10/18)
    print(f"en un terreno de {hectarias} hectarias o {m_2} metros cuadrados, hay {pin:.0f} pinos, {oya:.0f} oyameles, {ced:.0f} cedros")
    exit()
else: 
    pin= (m_2*0.5)*(8/10)
    oya= (m_2*0.3)*(15/15)
    ced= (m_2*0.2)*(10/18)
    print(f"en un terreno de {hectarias} hectarias o {m_2} metros cuadrados, hay {pin:.0f} pinos, {oya:.0f} oyameles, {ced:.0f} cedros")
    exit()