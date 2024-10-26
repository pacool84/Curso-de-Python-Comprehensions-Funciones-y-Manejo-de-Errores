#Dictionary Comprehension
#Su sintaxis es:
'''
{key: value for var in iterable}
'''
dict = {}
for i in range(0,11):
  dict[i] = i*2

print(dict)

dic_comp = {i: i*2 for i in range(0,11)}
print(dic_comp)

#Generando un diccionario a partir de una lista 
import random
countries = ['col', 'mex', 'bol', 'per']
population = {}

for country in countries:
  population[country] = random.randint(1, 100)

print(population)
print(type(population))

#Utilizando Dictionary Comprehension

population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

##Iterando sobre dos listas para generar un diccionario
names = ['Sebastian', 'Brenda', 'Paco']
ages = [9, 34, 40]

union_list = zip(names, ages) #La funcion ZIP hace la union de dos listas sin embargo el output de esta funcion es un id de referencia
transform_to_list = list(union_list)
print(transform_to_list)

#Ahora utilizando comprehension

new_dic = {name: age for (name, age) in zip(names, ages)}
print(new_dic)

#Dictionary Comprehension con condicionales 
'''
Su sintaxis es:

{key: value for var in iterable if condition}
'''

population_v3 = {country: random.randint(1,100) for country in countries}
print(population_v3)

#Agregando la condicional 
result = {country: population for (country, population) in population_v3.items() if population > 60}
print(result)

#Otro Ejemplo 

text = 'Hola Soy Sebastian'
unique_text = {caracter: caracter.upper() for caracter in text if caracter in 'aeiou'}
print(unique_text)