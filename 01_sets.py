# Definición de un set con países
sets_countries = {'col', 'mex', 'bol'}
print(sets_countries)  # Imprime el set de países
print(type(sets_countries))  # Muestra el tipo de datos (set)

# Definición de un set de números (los sets no permiten duplicados)
set_numbers = {1, 2, 3, 4, 4, 5, 6, 7}  
# El número 4 duplicado se elimina automáticamente
print(set_numbers)  # Muestra el set sin elementos repetidos
print(type(set_numbers))  # Muestra el tipo de datos (set)

# Set con datos mixtos: entero, string, booleano y flotante
set_mixData = {1, 'hola', False, 13.45 }
print(set_mixData)  # Muestra los elementos mezclados en el set
print(type(set_mixData))  # Muestra el tipo de datos (set)

# Creación de un set a partir de un string
set_from_string = set('Hola Mi Amigo Python')  
# El método set() divide la cadena en caracteres únicos
print(set_from_string)  # Muestra el set con caracteres únicos
print(type(set_from_string))  # Muestra el tipo de datos (set)

# Creación de un set a partir de una tupla (los duplicados se eliminan)
set_from_tuple = set(('sebastian', 'brenda', 'paco', 'paco'))
print(set_from_tuple)  # Muestra el set sin duplicados
print(type(set_from_tuple))  # Muestra el tipo de datos (set)

# Creación de un set a partir de una lista (elimina duplicados)
numbers = [1, 2, 3, 1, 2, 3, 4, 5]
set_numbers = set(numbers)  # Convierte la lista en un set
print(set_numbers)  # Muestra el set sin duplicados

# Convertir el set de nuevo en una lista para mantener solo elementos únicos
unique_numbers = list(set_numbers)  
print(unique_numbers)  # Muestra la lista con elementos únicos
print(type(unique_numbers))  # Muestra el tipo de datos (list)