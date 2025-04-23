# Simbologia que se utiliza para la representacion de cada operacion en un diagrama de flujo 
![simbolos de diagrama de flujo](simbolos-de-diagramas-de-flujo.png)

# Ejercicios 
# Realice un algoritmo para determinar cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de $85 cada uno; de lo contrario, el precio es de $90. Represéntelo con el pseudocódigo y el diagrama de flujo

# Pseudocodigo 
Inicio
    Escribir "Ingrese la cantidad de lápices a comprar:"
    Leer cantidad

    Si cantidad >= 1000 Entonces
        precio <- 85
    Sino
        precio <- 90
    FinSi

    total <- cantidad * precio

    Escribir "El costo total a pagar es: ", total
Fin

**Codigo** 

```py
cantidad = int(input("Ingrese la cantidad de lápices a comprar: "))

if cantidad >= 1000:
    precio = 85
else:
    precio = 90

total = cantidad * precio

print(f"El costo total a pagar es: ${total}")
```
## Un almacén de ropa tiene una promoción: por compras superiores a $250 000 se les aplicará un descuento de 15%, de caso contrario, sólo se aplicará un 8% de descuento. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar en dicho almacén y de cuánto es el descuento que obtendrá. Represéntelo mediante el pseudocódigo y el diagrama de flujo

## Pseudocodigo 
Inicio
    Escribir "Ingrese el valor de la compra:"
    Leer compra

    Si compra > 250000 Entonces
        descuento <- compra * 0.15
    Sino
        descuento <- compra * 0.08
    FinSi

    precio_final <- compra - descuento

    Escribir "El descuento aplicado es: ", descuento
    Escribir "El precio final a pagar es: ", precio_final
Fin

**Codigo**
```py 
compra = float(input("Ingrese el valor de la compra: "))

if compra > 250000:
    descuento = compra * 0.15  # 15% de descuento
else:
    descuento = compra * 0.08  # 8% de descuento

precio_final = compra - descuento

print("El descuento aplicado es:", descuento)
print("El precio final a pagar es:", precio_final)
```
### El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús es de $4000.00, sin importar el número de alumnos

### Pseudocodigo 
Inicio
    Escribir "Ingrese la cantidad de alumnos:"
    Leer alumnos

    Si alumnos >= 100 Entonces
        costo_por_alumno <- 65
        total_a_pagar <- alumnos * costo_por_alumno
    Sino Si alumnos >= 50 Entonces
        costo_por_alumno <- 70
        total_a_pagar <- alumnos * costo_por_alumno
    Sino Si alumnos >= 30 Entonces
        costo_por_alumno <- 95
        total_a_pagar <- alumnos * costo_por_alumno
    Sino
        costo_por_alumno <- 4000 / alumnos
        total_a_pagar <- 4000
    FinSi

    Escribir "El costo por alumno es: ", costo_por_alumno
    Escribir "El total a pagar a la compañía de viajes es: ", total_a_pagar
Fin

**Codigo**
```py
alumnos = int(input("Ingrese la cantidad de alumnos: "))

if alumnos >= 100:
    costo_por_alumno = 65
    total_a_pagar = alumnos * costo_por_alumno
elif alumnos >= 50:
    costo_por_alumno = 70
    total_a_pagar = alumnos * costo_por_alumno
elif alumnos >= 30:
    costo_por_alumno = 95
    total_a_pagar = alumnos * costo_por_alumno
else:
    total_a_pagar = 4000
    costo_por_alumno = total_a_pagar / alumnos

print("El costo por alumno es:", costo_por_alumno)
print("El total a pagar a la compañía de viajes es:", total_a_pagar)
```
#### Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10% anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años?

#### Pseudocodigo 

Inicio
    Definir salario Como Real
    salario <- 1500

    Escribir "Año 0:", salario

    Para año <- 1 Hasta 6 Hacer
        salario <- salario + (salario * 0.10)  // Incremento del 10%
        Escribir "Año", año, ":", salario
    FinPara

    Escribir "Salario final después de 6 años:", salario
Fin

**Codigo**
```py 
salario = 1500

print("Año 0:", salario)

for año in range(1, 7):
    salario += salario * 0.10  # Incremento del 10%
    print("Año", año, ":", salario)

print("Salario final después de 6 años:", salario)
