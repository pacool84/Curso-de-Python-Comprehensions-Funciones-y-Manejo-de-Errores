set_countries = {'mex', 'col', 'bol'}
print(set_countries)

#Tamaño de un set
size_set = len(set_countries)
print(f'EL tamaño de este SET es de: {size_set}')

#Preguntar por un valor en un set 
print('mex' in set_countries) #SI hace parte del conjunto
print('per' in set_countries) #NO hace parte del conjunto

#Agregar un elemento a un set 
set_countries.add('per')
print(set_countries, len(set_countries))

#Actualizar un set
set_countries.update({'arg', 'brz'})
print(f'El SET actualizado es: {set_countries}')

#Remover un elemento de un set 
set_countries.remove('brz')
print(set_countries)

#Otra forma de remover un elemento, más recomendado
set_countries.remove('bol')
print(set_countries)

#Eliminar TODOS los elementos de un set
set_countries.clear()
print(set_countries)