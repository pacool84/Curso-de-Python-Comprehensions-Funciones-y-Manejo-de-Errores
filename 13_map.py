#MAP su funcion principal es realizar transformaciones a una lista dada de elementos
#Cuando se realiza la tranformacion de obtiene el mismo numero de elementos
#MAP cumple con la caracteristica de HOF
#Se debe de trabajar con MAP para hacer una interpretacion correcta ya 
# que directamente la funcion MAP envia una referencia por lo que se debe de transofrmarlo en una lista 

numbers = [1,2,3,4,5]
numbers_v2 = []

#Transformacion tradicional 

for i in numbers:
  numbers_v2.append( i * 2)

print(numbers_v2)

#Realizando tranformacion con MAP y lambda functions

numbers_v3 = list(map(lambda i : i*2, numbers))
print(numbers_v3)

#Tranformando mulitples lista de diferentes dimensiones con MAP
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

result = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(result)
