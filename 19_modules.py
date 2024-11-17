import sys
print(sys.path) #Nos dira en que path se encuentra ejecutandose el archivo actual de python 

import re #Este modulo te permite trabajar con expresiones regulares
text = 'Hola, mi numero de telefono es 53-28-35-00'
result = re.findall('[0-9]+', text) #findall nos permite identificar solo el criterio de la expresion regular que en este caso son para numeros del 0 al 9
print(result)

import time #Este modulo te permite trabajar con horas y fechas
timeStamp = time.time() #Este metodo te muestra el horario en formato "unix"
print(timeStamp)

format_time = time.localtime() #localtime() te brinda un formato mas entendible de la hora en el sistema
print(format_time)

another_format = time.asctime(format_time) #Esta fecha esta formateada con ASCII
print(another_format)

import collections #Este modulo te permite el manejo de listas 
numbers = [1,4,7,1,5,1,9,4,2,1,9,1]

counter = collections.Counter(numbers) #Podemos sacar la frecuencia que se repite un numero 
print(counter)