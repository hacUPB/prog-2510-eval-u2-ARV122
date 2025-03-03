#Ejericio de calculo de memoria 

identificador numerico -> (numero entero) -> 4 Bytes 
una temperatura        -> (numero punto flotante) -> 4 Bytes 
un valor logico        -> (Booleano: True or false) -> 1 Byte 
un texto de 10 carecteres -> (cada caracter ocupa 1 byte) -> 10 bytes 

4+4+1+10 = 19 bytes 

En cada conjunto ocupamos 19 bytes en la memoria 

2. Determinamos la frecuencia de almacenamiento 

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