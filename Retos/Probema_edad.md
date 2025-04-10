3. Se requiere determinar la edad actual de una persona basándose en su fecha de nacimiento. Además, es necesario establecer si la persona ya ha cumplido años en el año en curso, si aún no lo ha hecho, o si hoy es su cumpleaños, para celebrarlo. La fecha de nacimiento y la fecha actual estarán representadas mediante tres variables: día, mes y año.
    
    **Instrucciones:**
    
    - Diseñe un algoritmo que permita calcular la edad de la persona.
    - Dentro de la solución, determine si la persona ya celebró su cumpleaños este año o si aún no lo ha hecho.
    - Verifique si la fecha actual corresponde al día de su cumpleaños. De ser así, imprima el mensaje “Feliz Cumpleaños”.
    - Represente la solución utilizando **pseudocódigo** claro y estructurado.


    Pseudocodigo 

    Inicio
    
        Entrada: Pedir la fecha de nacimiento y la fecha actual
    Escribir "Ingrese el día de nacimiento:"
    Leer dia_nacimiento
    Escribir "Ingrese el mes de nacimiento:"
    Leer mes_nacimiento
    Escribir "Ingrese el año de nacimiento:"
    Leer año_nacimiento

    Escribir "Ingrese el día actual:"
    Leer dia_actual
    Escribir "Ingrese el mes actual:"
    Leer mes_actual
    Escribir "Ingrese el año actual:"
    Leer año_actual

         Cálculo de la edad
    edad = año_actual - año_nacimiento

         Verificación de cumpleaños
    Si (mes_actual < mes_nacimiento) o (mes_actual = mes_nacimiento y dia_actual < dia_nacimiento) Entonces
        edad = edad - 1
        Escribir "Aún no ha cumplido años este año."
    Sino Si (mes_actual = mes_nacimiento y dia_actual = dia_nacimiento) Entonces
        Escribir "Feliz Cumpleaños!"
    Sino
        Escribir "Ya ha cumplido años este año."
    FinSi

         Mostrar la edad
    Escribir "La edad actual es:", edad
Fin
