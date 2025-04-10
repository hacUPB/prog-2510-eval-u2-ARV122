#Solicitar fecha de nacimiento 
dia_nacimiento = int(input("Ingerese el dia de nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de nacimiento: "))
año_nacimento = int(input("Ingrese el año de nacimiento: "))

#fecha actual
dia_actual = int(input("Ingrese el dia actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
año_actual = int(input("Ingrese el año actual: "))

#calculo de la edad inicial 
edad = año_actual - año_nacimento

#Verificamos si ya cumplio este año 
if mes_actual < mes_nacimiento: 
    edad -= 1
    print("aun no ha cumplido años este año")