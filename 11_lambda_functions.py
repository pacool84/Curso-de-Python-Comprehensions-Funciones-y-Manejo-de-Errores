#Las funciones lamda son consideradas funciones anonimas 
#Su sintaxis es la siguiente 
'''
lambda "parametros de entrada" : "parametros de salida"
'''

#Ejemplo de funcion normal
def increment(x):
  return x + 1

result = increment(10)
print(result)

#Ahora haciendolo con una funcion lambda

increment_v2 = lambda x : x + 1

result2 = increment_v2(20)
print(result2)

#Otro Ejemplo, utilizando varios parametros

full_name = lambda name, lastName : f'Mi nombre completo es {name.title()} {lastName.title()}' #.title() lo usamos para pasar a mayusculas la primera letra

name = full_name('sebas', 'lopez')
print(name)