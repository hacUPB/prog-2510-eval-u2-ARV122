# Escribe un párrafo explicando en tus propias palabras cómo se representan los datos en una computadora. 
Por ejemplo, ¿cómo se ingresan números, letras, imágenes a una computadora?

## Respuesta:
Los datos se representan atraves de ciertas combinaciones de ceros y unos, lo que conocemos como sistema binario
Cada letra, imagen o numero se convierte en estas combinaciones que la maquina logra entender 

## ¿Cuántos estados diferentes pueden ser representados por N variables binarias?

# Respuesta:
Como lo mencionamos en clase cada variable puede tener solo dos digitos 0 o 1,  si teos N variables cada una de ellas puede combinarse de 
diferentes formas pero en numero total de combinaciones posibles serian de 2^N 

## ¿Cuáles son las unidades de almacenamiento de datos que se utilizan en computación?
Crea una tabla donde muestres estas unidades con sus prefijos. 
En este caso me refiero a KiloByte, MegaByte, etc 

|Unidad|Tamaño|
|------|------|
|Bit||
|Byte  B |8 Bits|
|Kilobyte  KB |1024 B|
|Megabyte  MB |1024 KB|
|Gigabyte  GB |1024 MB|
|Terabyte  TB |1024 GB|


## Ejercicio 2
Ahora es tu turno de intentar usar el método. Te voy a proponer varios números binarios y tú vas a convertirlos a decimales utilizando la tabla 3. 
Recuerda que el subíndice 2 significa que el número es binario (base 2)

- $1010101010_2 
- 11111_2
- 10000000_2
- 100100100_2

# Solucion

1010101010_2 = 512 + 128 + 32 + 8 + 2 = 682_10


11111_2 = 16 + 8 + 4 + 2 + 1 = 31_10 

10000000_2 = 128 = 128_10 

100100100_2 = 256 ´+ 32 + 4 = 292_10 

## Ejercicio 3
Ahora es tu turno. Vas a convertir los siguientes  números decimales a binarios. Recuerda que el subíndice 10 significa que el número es decimal (base 10)

- 127_10 
- 246_10
- 1025_10
- 354_10

$127_(10)$
​  |128|64|32|16|8|4|2|1|
  |   |  |  |  | | | | |
  |0|1|1|1|1|1|1|1|

$127_(10)=1111111_2$
​
$246_10$

  |128|64|32|16|8|4|2|1|
  |   |  |  |  | | | | |
  |1|1|1|1|0|1|1|0|

$246_(10)=11110110_2$
​
$1025_(10)$
|1024|512|256|128|64|32|16|8|4|2|1|
|    |   |   |   |  |  |  | | | | |
  |1|0|0|0|0|0|0|0|0|0|1|

$1025_(10)=10000000001_2$
​
$354_(10)$

 |256|128|64|32|16|8|4|2|1|
 |   |   |  |  |  | | | | |
  |1|0|1|1|0|0|0|1|0|

$354_(10)=101100010_2$


# Actividad investigación 
Investiga los diferentes tipos de datos que se utilizan en varios lenguajes de programación (por ejemplo, C, Java, Python). Ten en cuenta cómo cada lenguaje define los números enteros, los decimales (o flotantes), las letras del alfabeto, las cadenas de texto, valores booleanos, entre otros. Investiga qué nombres se asignan y qué abreviaciones se utilizan en cada lenguaje

## Tipado del tipo de dato Enteros en diferentes lenguajes:
# C y C++:
En C y C++, los enteros se representan con los tipos int (para enteros con signo) y unsigned int (para enteros sin signo). Además, hay tipos como short e int que representan enteros con diferentes tamaños.
# Java:
En Java, los enteros se representan con el tipo de dato int para enteros con signo y long para enteros de mayor tamaño.
# Python:
En Python, no hay límite fijo en el tamaño de los enteros. El tipo int se ajusta dinámicamente según sea necesario.
# JavaScript:
En JavaScript, todos los números son de punto flotante, pero se pueden utilizar operaciones y notaciones para lograr el comportamiento de enteros.
# C#:
En C#, los enteros se representan con los tipos int para enteros con signo y uint para enteros sin signo. También hay tipos como short, long, etc.
# Swift:
En Swift, los enteros se representan con los tipos Int para enteros con signo y UInt para enteros sin signo. Los tamaños pueden variar en plataformas diferentes.
# Ruby:
En Ruby, los enteros no tienen límite fijo en su tamaño. La clase Integer se utiliza para representar enteros.
# PHP:
En PHP, los enteros se representan con el tipo de dato int. PHP utiliza un sistema dinámico de tipos, por lo que no es necesario declarar el tipo de dato.

# Tipado del tipo de dato «punto flotante» en diferentes lenguajes:
# C y C++:
En C y C++, el tipo de dato para números de punto flotante se representa con float (para precisión simple) o double (para precisión doble).
# Java:
En Java se representa con float (precisión simple) o double (precisión doble).
# Python:
En Python se representa con float.
# JavaScript:
En JavaScript, todos los números, incluidos los de punto flotante, se representan con el tipo de dato Number.
# C#:
En C# se representa con float (precisión simple) o double (precisión doble).
# Swift:
En Swift, el tipo de dato para números de punto flotante se representa con Float (precisión simple) o Double (precisión doble).
# Ruby:
En Ruby se representan simplemente como Float.
# PHP:
En PHP se representa con float o double.

## Tipado del tipo de dato cadenas de caracteres en diferentes lenguajes:
# C y C++:
En C y C++, las cadenas de caracteres se representan como arreglos de caracteres (char[]) o como punteros a caracteres (char*). No hay un tipo de dato de cadena incorporado como en algunos lenguajes de más alto nivel.
# Java:
En Java, el tipo de dato para cadenas de caracteres se representa con String.
# Python:
En Python se representa con str.
# JavaScript:
En JavaScript se representa con String.
# C#:
En C# se representa con string.
# Swift:
En Swift representa con String.
# Ruby:
En Ruby se representa con String.
# PHP:
En PHP se representa con string

# Tipado del tipo de dato boolean en diferentes lenguajes:
# C y C++:
El tipo de dato booleano se representa con bool.
# Java:
En Java se representa con boolean.
# Python:
En Python se representa con bool, y los valores son True y False.
# JavaScript:
En JavaScript se representa con boolean, y los valores son true y false.
# C#:
En C# se representa con bool.
# Ruby:
En Ruby se representa con true y false.
# PHP:
En PHP, el tipo de dato booleano se representa con bool, y los valores son true y false.

## Tipado del tipo de dato caracteres en diferentes lenguajes:
# C: 
El tipo de dato char se utiliza para representar un solo carácter alfanumérico. Se almacena como un número entero de 1 byte (generalmente ASCII).
# C++: 
El tipo de dato char funciona de manera similar a C y se utiliza para almacenar caracteres individuales.
# Java: 
El tipo de dato char también se utiliza para representar caracteres alfanuméricos. Se almacena como un número entero de 2 bytes en Unicode.
# Python: 
No existe un tipo de dato char específico. Un solo carácter es simplemente una cadena de longitud 1.
# JavaScript: 
En JavaScript, los caracteres individuales no tienen un tipo de dato específico. Se pueden representar como cadenas de longitud 1.
# C#: 
El tipo de dato char representa un solo carácter Unicode y se almacena como un número entero de 2 bytes.
# Swift: 
El tipo de dato Character se utiliza para representar un solo carácter Unicode.
# Ruby: 
En Ruby, los caracteres son tratados como cadenas de longitud 1 y no tienen un tipo de dato char específico.
# PHP: 
El tipo de dato char no existe como tal. Los caracteres son simplemente parte de las cadenas de texto.

# Otros tipos de datos que existen en programación:
Hasta aquí nombramos los tipos de datos más usados y fundamentales en la programacion. Aunque también existen muchos más, a continuación nombro alguno de ellos:

# Punteros:
Almacena la dirección de memoria de otra variable.
Enumeraciones (Enum):
Define un conjunto de constantes con nombre.
Tipo de Dato Vacío (Void):
Indica que no hay tipo de datos o valor presente.
# Tipo de Datos Abstracto (ADT):
Representa un tipo de datos definido por el usuario con sus operaciones asociadas.
# Tipo de Datos Compuesto:
Combina varios tipos de datos en una sola unidad, como las estructuras en C o los objetos en lenguajes orientados a objetos.
# Tipo de Datos Genérico:
Permite trabajar con variables de cualquier tipo, proporcionando flexibilidad en la programación.
# Tipo de Datos Fecha/Hora:
Almacena información de fecha y hora.
# Tipo de Datos Byte:
Almacena datos en formato de byte.
# Tipo de Datos BigDecimal:
Utilizado para representar números de punto flotante con precisión arbitraria.
# Tipo de Datos Carácter Unicode:
Representa caracteres utilizando el estándar Unicode.
# Tipo de Datos Boleano de Tres Estados:
Puede tener tres valores: verdadero, falso o nulo.

[**Fuente**](https://www.apinem.com/tipos-de-datos-programacion/)


# Ejericio de calculo de memoria 

identificador numerico | -> (numero entero) -> 4 Bytes |
una temperatura        | ->  (numero punto flotante) -> 4 Bytes |
un valor logico        |-> (Booleano: True or false) -> 1 Byte |
un texto de 10 carecteres |-> (cada caracter ocupa 1 byte) -> 10 bytes |

4+4+1+10 = 19 bytes 

En cada conjunto ocupamos 19 bytes en la memoria 

## Determinamos la frecuencia de almacenamiento 

Se guardan cada 10 seg durante 24 hrs 

primero vamos a calcular cuantas veces se almacenan los datos en una hora 

seg en una hora = 60 x 60 = 3600 
Numero de registros por hora = 3600/1o = 360 

lo vamos a multiplicar por 24 horas que tiene el dia 

numero de registros en 24 hrs = 360 x 24 = 8640 

Para calcular el espacio total necesario 

cada registro ocupa -> 19 Bytes 
se almacenan 8640 registros en 24 hrs 

Para obtener el total en Bytes 

8640 x 19 = 164, 160 Bytes 

Paso final es para convertir a unidades mas grande 

para convertir de Bytes -> KB 
1 KB = 1024 Bytes 

De KB a MB 
1 MB = 1024 KB 

160.31 / 1024 = 0.5165 MB 